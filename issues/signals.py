from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Issue

@receiver(post_save, sender=Issue)
def notify_issue_update(sender, instance, **kwargs):
    #send notifi to the assignee or manager
    pass


from django.db.models.signals import post_save
from django.core.mail import send_mail
from .models import Issue

@receiver(post_save, sender=Issue)
def send_issue_notification(sender, instance, created, **kwargs):
    if created:
        subject = f'New Issue: {instance.title}'
        message = f'{instance.description}'
        send_mail(subject, message, 'admin@example.com', [instance.assignee.email])
