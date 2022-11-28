from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    """
    Default custom user model for Baskin Robbins.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    name = None

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
