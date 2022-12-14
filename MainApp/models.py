from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator

# Create your models here.

# ---------------------------------------------------------------------------- #
#                                    CSVFile                                   #
# ---------------------------------------------------------------------------- #

class CSVFile(models.Model):
    """
    To get the CSV File and store it
    """ 
    csv_file = models.FileField(
        _('CSV File'),
        upload_to = 'csvfiles/',
        validators = [FileExtensionValidator(['csv'])],
        help_text = "Please upload only .csv file"
    )
    
    timeframe = models.IntegerField(
        _('Timeframe'),
        blank = True,
        null = True,
        help_text = 'Please enter the timefram in minutes and should be grater than 1 minute'
    )
    
    json_file = models.FileField(
        _('JSON File'),
        upload_to = 'jsonfiles/',
        validators = [FileExtensionValidator(['json'])],
        help_text = "Please upload only .json file",
        null = True,
        blank = True
    )
    
    created_at = models.DateTimeField(
        _('Created At'),
        auto_now_add = True
    )
    
    updatedAt = models.DateTimeField(
        _('Updated At'),
        auto_now = True
    )
    
    class Meta:
        ordering = ('-id', )
        
    @property
    def sys_id(self):
        str_id = str(self.id).zfill(5)
        return f"CSV{str_id}"
    
    def __str__(self):
        return self.sys_id
    
    
# ---------------------------------------------------------------------------- #
#                                  Candlestick                                 #
# ---------------------------------------------------------------------------- #

class Candlestick(models.Model):
    """
    To store the candlestick data
    """
    csv = models.ForeignKey(
        CSVFile,
        on_delete = models.CASCADE,
        verbose_name = _('CSV File'),
        related_name = 'candlestick',
    )
    
    banknifty = models.CharField(
        _('Bank Nifty'),
        max_length = 50,
        blank = True,
        null = True
    )
    
    date = models.CharField(
        _('Date'),
        max_length = 20,
        blank = True,
        null = True
    )
    
    time = models.CharField(
        _('Time'),
        max_length = 10,
        blank = True,
        null = True
    )
    
    open_value = models.FloatField(
        _('Open'),
        blank = True,
        null = True
    )

    high = models.FloatField(
        _('High'),
        blank = True,
        null = True
    )
    
    low = models.FloatField(
        _('Low'),
        blank = True,
        null = True
    )
    
    close = models.FloatField(
        _('Close'),
        blank = True,
        null = True
    )
    
    volume = models.FloatField(
        _('Volume'),
        blank = True,
        null = True
    )
    
    created_at = models.DateTimeField(
        _('Created At'),
        auto_now_add = True
    )
    
    updatedAt = models.DateTimeField(
        _('Updated At'),
        auto_now = True
    )
    
    class Meta:
        ordering = ('-id', )
        
    @property
    def sys_id(self):
        str_id = str(self.id).zfill(5)
        return f"CDL{str_id}"
    
    def __str__(self):
        return self.sys_id
    