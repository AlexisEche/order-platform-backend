from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import AvailableResourceManager


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)
    published_at = models.DateTimeField(
        _("published_at"), blank=True, null=True)
    archived_at = models.DateTimeField(_("archived_at"), blank=True, null=True)
    deleted_at = models.DateTimeField(_("deleted_at"), blank=True, null=True)

    # managers

    objects = models.Manager()
    availables = AvailableResourceManager()

    # properties

    @property
    def is_visible(self):
        return self.published_at is not None and self.archived_at is None and self.deleted_at is None

    # methods
    def is_visible_admin(self):
        return self.is_visible

    class Meta:
        abstract = True

    is_visible_admin.boolean = True
    is_visible_admin.short_description = _("is_visible")
