from django.db import models

# Create your models here.

class WaterOrder(models.Model):
    WATER_TYPES = [
        ('normal', 'Normal Water'),
        ('cold', 'Cold Water'),
        ('hot', 'Hot Water'),
    ]

    water_type = models.CharField(max_length=10, choices=WATER_TYPES, default='normal')
    tap_id = models.CharField(max_length=50, default="tap_1")
    liters_requested = models.IntegerField()
    total_price = models.FloatField()

    is_paid = models.BooleanField(default=False)
    is_dispensed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Set tap_id based on water_type
        tap_mapping = {
            'normal': 'tap_1',
            'cold': 'tap_2',
            'hot': 'tap_3'
        }
        self.tap_id = tap_mapping.get(self.water_type, 'tap_1')
        self.total_price = self.liters_requested * 1  # ₹1 per liter
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.liters_requested}L {self.get_water_type_display()} - Paid: {self.is_paid}"