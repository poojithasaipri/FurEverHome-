
    
from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    SPECIES_CHOICES = (
        ("Dog", "Dog"),
        ("Cat", "Cat"),
        ("Parrot", "Parrot"),
        ("Fish", "Fish"),
        ("Hamster", "Hamster"),
        ("Other", "Other"),
    )

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    age = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)

    # New fields
    microchip_number = models.CharField(max_length=100, blank=True, null=True)
    vaccination_date = models.DateField(blank=True, null=True)
    is_adopted = models.BooleanField(default=False)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AdoptionRequest(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    )

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='requests')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.full_name} -> {self.pet.name}"


