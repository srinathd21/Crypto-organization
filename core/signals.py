from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Organization

@receiver(post_save, sender=Organization)
def log_organization_created(sender, instance, created, **kwargs):
    if created:
        print(f"✅ Organization Created: {instance.name} (ID: {instance.id})")

@receiver(post_delete, sender=Organization)
def log_organization_deleted(sender, instance, **kwargs):
    print(f"❌ Organization Deleted: {instance.name} (ID: {instance.id})")
