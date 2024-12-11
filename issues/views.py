from django.shortcuts import render, redirect
from django_filters.views import FilterView
from .models import Issue
from .filters import IssueFilter
from django.core.paginator import Paginator

# IssueListView using Django Filters for both filtering and pagination
class IssueListView(FilterView):
    model = Issue
    filterset_class = IssueFilter
    template_name = 'issues/issue_list.html'
    context_object_name = 'issues'  # This will be the name of the context variable containing the filtered issues
    paginate_by = 10  # Number of issues per page

# Optionally, you can use this function-based view (if you prefer manual pagination and custom filtering logic)
def issue_list(request):
    issues = Issue.objects.all()
    filter = IssueFilter(request.GET, queryset=issues)
    paginator = Paginator(filter.qs, 10)  # Show 10 issues per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'issues/issue_list.html', {'page_obj': page_obj, 'filter': filter})


from django.shortcuts import render, redirect
from .forms import IssueForm

def issue_create(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new issue to the database
            return redirect('issue_list')  # Redirect to the issue list page
    else:
        form = IssueForm()

    return render(request, 'issues/issue_create.html', {'form': form})


