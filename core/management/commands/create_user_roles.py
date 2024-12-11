# core/management/commands/create_user_roles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Creates user roles for the project'

    def handle(self, *args, **kwargs):
        # Create groups for each role
        system_designer_group = Group.objects.get_or_create(name='System Designer')
        project_manager_group = Group.objects.get_or_create(name='Project Manager')
        system_analyst_group = Group.objects.get_or_create(name='System Analyst')
        developer_group = Group.objects.get_or_create(name='Developer')
        admin_group = Group.objects.get_or_create(name='Admin')

        self.stdout.write(self.style.SUCCESS('Successfully created user roles'))
