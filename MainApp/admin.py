from django.contrib import admin
from MainApp.models import Candlestick, CSVFile


# Register your models here.


@admin.register(Candlestick)
class Candlestick(admin.ModelAdmin):
    list_display = ('id', 'csv', 'date', 'time', 'open_value', 'high', 'low', 'close', 'volume')
    
    
@admin.register(CSVFile)
class CSVFile(admin.ModelAdmin):
    list_display = ('id', 'csv_file', 'timeframe')
