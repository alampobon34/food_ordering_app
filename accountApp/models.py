from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]


ADDRESS_CHOICES = [
    ('Home', 'Home'),
    ('Office', 'Office'),
]

CITY = [
    ('Dhaka', 'Dhaka'),
    ('Mymensign', 'Mymensign'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Barisal', 'Barisal'),
    ('Chottogram', 'Chottogram'),
    ('Khulna', 'Khulna'),
]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_staffuser(self, email, name, password):
    #     """
    #     Creates and saves a staff user with the given email and password.
    #     """
    #     user = self.create_user(
    #         email=self.normalize_email(email),
    #         name=name,
    #         password=password,
    #     )
    #     user.staff = True
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Email & Password are required by default.

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True



class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=255, choices=ADDRESS_CHOICES, null=True, blank=True)
    address = models.TextField(max_length=1000,null=True,blank=True)
    area = models.CharField(max_length=100,null=True,blank=True,choices=CITY)
    houseNo = models.CharField(max_length=100,null=True,blank=True)
    roadNo = models.CharField(max_length=100,null=True,blank=True)
    zipCode = models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.user.email


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    birthDate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,upload_to='user_img', default='pic.png')

    


    def __str__(self):
        return self.user.email





