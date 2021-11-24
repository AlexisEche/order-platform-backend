from django.db import models

from core.abstracts import TimeStampedModel
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Recipes(TimeStampedModel):
	name = models.CharField(verbose_name=_("name"), max_length=50, blank=True, default="")
	description = models.TextField(verbose_name=_("description"),blank=True, default="")
	image = models.URLField(verbose_name=_("image"), blank=True, default="")
	price = models.PositiveIntegerField(verbose_name=_("price"), default=0)
	category = models.CharField(verbose_name=_("category"), max_length=50, blank=True, default="")
	amount = models.PositiveIntegerField(verbose_name=_("amount"), default=0)

# Create your models here.
