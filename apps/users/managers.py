from django.contrib.auth.models import BaseUserManager

# ------------------------
class UserAccountManager(BaseUserManager):

    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
                username = username,
                email = self.normalize_email(email),
                **extra_fields
            )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, email, password, **extra_fields)
