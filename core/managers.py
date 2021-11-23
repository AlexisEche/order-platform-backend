from django.db import models
from django.db.models.query_utils import Q


class AvailableResourceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(~Q(published_at=None) & Q(archived_at=None) & Q(deleted_at=None))
