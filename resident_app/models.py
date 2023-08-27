from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Resident(models.Model):
    resident_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    email_id = models.EmailField()
    resident_building_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    token_amount = models.DecimalField(max_digits=10, decimal_places=2)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    move_in_date = models.DateField()
    move_out_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.resident_name
    
    def clean(self):

        if not self.contact_number.isdigit() or len(self.contact_number) != 10:
            raise ValidationError('Please enter 10 digit contact number')
        
        if self.contract_start_date > self.contract_end_date:
            raise ValidationError('contract start date should be less than end date')
        
        if self.move_in_date > self.move_out_date:
            raise ValidationError('move in date should be less than move out date')
        
        if self.token_amount < 0 or self.token_amount >= self.rent_amount:
            raise ValidationError('token amount should be positive and less than rent amount')

        if self.rent_amount < 0:
            raise ValidationError('Rent Amount should be positive')
        
        if self.date_of_birth >= timezone.now().date():
            raise ValidationError("Date of birth must be in the past.")


class CommunityEvent(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    event_description = models.TextField()

    def __str__(self):
        return self.event_name