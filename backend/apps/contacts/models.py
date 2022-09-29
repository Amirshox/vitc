from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(BaseModel):
    title = models.CharField(max_length=63)

    def __str__(self):
        return self.title


class Contact(BaseModel):
    MALE = "male"
    FEMALE = "female"

    GENDER_CHOICES = (
        (MALE, "male"),
        (FEMALE, "female"),
    )

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12, validators=[phone_regex])
    email = models.EmailField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=MALE)

    tags = models.ManyToManyField(Tag, related_name="contacts", blank=True)

    father = models.ForeignKey("self", on_delete=models.SET_NULL, related_name='contacts_father', null=True, blank=True)
    mother = models.ForeignKey("self", on_delete=models.SET_NULL, related_name='contacts_mother', null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.full_name
