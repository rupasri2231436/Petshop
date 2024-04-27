from django.db import models
from PIL import Image
from django.contrib.auth.models import User
import uuid

class ResizableImageField(models.ImageField):
    def save(self, *args, **kwargs):
        image = super().save(*args, **kwargs)
        img = Image.open(image.path)

        # Set the desired size (1500x600)
        desired_size = (1500, 600)

        # Resize the image to fit within the desired dimensions without distorting the aspect ratio
        img.thumbnail(desired_size, Image.ANTIALIAS)

        # Save the resized image
        img.save(image.path)


class Products(models.Model):
    # Other fields you already have
    name = models.CharField(max_length=300, null=True)
    price = models.FloatField()
    description = models.TextField()
    digital = models.BooleanField(default=True, null=True, blank=False)
    image = ResizableImageField(null=True, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    life_expectancy = models.CharField(max_length=100, null=True, blank=True)

    # Add a 'category' field to distinguish between dogs and cats
    CATEGORY_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Rabbit', 'Rabbit'),
        ('Birds', 'Birds'),
        ('Fish', 'Fish'),
        ('Accessory', 'Accessory')
        # Add more categories if needed
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,
                                default='Dog')  # Set 'Dog' as the default value

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(null=True)


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)





# Create your models here.




class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total

    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity


class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    @property
    def price(self):
        new_price = self.product.price * self.quantity
        return new_price



