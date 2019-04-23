from django.core.validators import RegexValidator
from django.db import models


PHONE_REGEX_VALIDATOR = RegexValidator(regex=r'^\d{10}$',
                                       message="Please select a valid phone number.")


class ModelBase(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TeamMember(ModelBase):
    REGULAR = 0
    ADMIN = 1
    ROLE_TYPE = (
        (REGULAR, 'REGULAR'),
        (ADMIN, 'ADMIN'),
    )

    first_name = models.CharField(max_length=251)
    last_name = models.CharField(max_length=251)
    phone_number = models.CharField(validators=[PHONE_REGEX_VALIDATOR], max_length=10)
    email = models.EmailField()
    role = models.CharField(max_length=64, choices=ROLE_TYPE)

    class Meta:
        db_table = "team_member"
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return "{0} {1}".format(self.first_name, self. last_name)
