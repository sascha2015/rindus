from django.db import models
from localflavor.generic.models import IBANField
from django.contrib.auth.models import User

class UserData(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="First Name")
    last_name = models.CharField(max_length=200, verbose_name="Last Name")
    iban = IBANField(verbose_name="IBAN")
    cuser = models.ForeignKey (User, related_name="CUSER", null=True, on_delete=models.SET_NULL, editable=False,
                               verbose_name="Administrator")

    class Meta:
        verbose_name = "User Data"
        verbose_name_plural = "User Data"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

