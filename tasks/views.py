from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
import json
from django.http import JsonResponse
import plotly.express as px
from .models import Task
from notifications.models import Notification

# Task List View
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Task Create View
def task_create(request):
    if request.method == 'POST':
        # Assume you have a form to create a task
        form = TaskForm(request.POST)
        if form.is_valid():
            # Save the task
            task = form.save()
            
            # Create a notification for the user assigned to the task
            new_notification = Notification.objects.create(
                user=task.assignee,  # Assuming the task has an assignee field
                message=f"You have been assigned a new task: {task.title}",
            )

            # Redirect or render the success page
            return redirect('task_list')  # Replace with your redirect URL

    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})

# Task Edit View
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# Task Delete View
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


def kanban_board(request):
    to_do_tasks = Task.objects.filter(status='to_do')
    in_progress_tasks = Task.objects.filter(status='in_progress')
    done_tasks = Task.objects.filter(status='done')

    return render(request, 'tasks/kanban_board.html', {
        'to_do_tasks': to_do_tasks,
        'in_progress_tasks': in_progress_tasks,
        'done_tasks': done_tasks,
    })

def update_task_status(request, task_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_status = data.get('status')

        task = Task.objects.get(pk=task_id)
        task.status = new_status
        task.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False}, status=400)


from notifications.models import Notification


def update_task_status(request, task_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_status = data.get('status')

        task = Task.objects.get(pk=task_id)
        task.status = new_status
        task.save()

        # Create a notification
        Notification.objects.create(
            user=task.assignee,
            message=f'Task "{task.title}" status changed to {task.get_status_display()}'
        )

        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)



from django.shortcuts import render
from django.http import JsonResponse
import plotly.graph_objects as go
from .models import Task

# Function to determine task color based on status and priority
def determine_task_color(task):
    if task.status == 'done':
        return 'green'
    elif task.status == 'in_progress':
        return 'orange'
    elif task.status == 'to_do':
        return 'red'

    # Priority-based colors
    if task.priority == 'high':
        return 'darkred'
    elif task.priority == 'medium':
        return 'orange'
    elif task.priority == 'low':
        return 'lightgreen'

    return 'blue'  # Default color

# View to render the Gantt chart
import plotly.graph_objects as go
from datetime import timedelta

def gantt_chart(request):
    tasks = Task.objects.all()

    task_data = []
    for task in tasks:
        task_data.append({
            "title": task.title,
            "start_date": task.start_date,
            "project": task.project.name if task.project else "Unassigned",
            "end_date": task.end_date,
            "status": task.get_status_display(),
            "priority": task.priority,
            "progress": task.progress,
            "assignee": task.assignee.name if task.assignee else 'Unassigned',
            "assignee_image": task.assignee.profile_picture.url if task.assignee and task.assignee.profile_picture else '/static/default-avatar.png',
            "dependencies": [dep.title for dep in task.dependencies.all()],
            "color": determine_task_color(task),
        })

    # Create Plotly Gantt chart
    fig = go.Figure()
    
    for task in task_data:
        start_date = task['start_date']
        end_date = task['end_date']
        task_duration = (end_date - start_date).days  # Total duration in days
        
        # Step width can be adjusted based on the granularity you want (e.g., daily, weekly)
        step_width = 1  # Each step will represent one day
        
        # Create a list of bar segments (each representing one step)
        x_values = [start_date + timedelta(days=i) for i in range(task_duration)]
        y_values = [task['title']] * task_duration  # All segments belong to the same task
        
        # Add each segment as a bar
        for i in range(task_duration):
            fig.add_trace(go.Bar(
                x=[x_values[i]],  # One step per task
                y=[y_values[i]],
                orientation='h',
                marker=dict(color=task['color']),
                text=f"{task['title']} ({task['status']} - {task['progress']}% done)",
                hoverinfo="text"
            ))

    fig.update_layout(
        title="Task Management Gantt Chart",
        xaxis_title="Dates",
        yaxis_title="Tasks",
        barmode='stack',
        showlegend=False,
        height=500,
        xaxis=dict(
    tickformat="%b %d, %Y",  # Date format
),
    )

    # Convert Plotly figure to HTML
    chart_html = fig.to_html(full_html=False)

    return render(request, 'tasks/gantt_chart.html', {'chart_html': chart_html, 'tasks': task_data})


def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    # Mark task as completed
    task.status = 'done'
    task.save()

    # Create a notification for the task creator
    new_notification = Notification.objects.create(
        user=task.creator,  # Assuming the task has a creator field
        message=f"Your task '{task.title}' has been marked as completed.",
    )

    return redirect('task_list')