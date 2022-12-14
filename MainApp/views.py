# Django imports
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.conf import settings
from django.core.files import File


# python imports
import csv
import os
import json

# In app imports
from MainApp.models import CSVFile, Candlestick
from MainApp.forms import CSVFileForm


# Create your views here.

# ---------------------------------------------------------------------------- #
#                                CSVFileListView                               #
# ---------------------------------------------------------------------------- #

class CSVFileListView(ListView):
    """
    To display the list of uploaded csv files
    """
    model = CSVFile
    template_name = 'MainApp/csvfile_list.html'
    success_url = reverse_lazy('MainApp:csvfile_list')
    
    
# ---------------------------------------------------------------------------- #
#                               CSVFileCreateView                              #
# ---------------------------------------------------------------------------- #

class CSVFileCreateView(CreateView):
    """
    To upload the csv file and store timframe and create candlestick objects
    """
    model = CSVFile
    template_name = 'MainApp/csvfile_create.html'
    form_class = CSVFileForm
    success_url = reverse_lazy('MainApp:csvfile_list')
    
    def post(self, *arg, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            csv_obj = CSVFile.objects.all().first()
            timeframe = csv_obj.timeframe
            file = open(os.path.join(settings.BASE_DIR) + csv_obj.csv_file.url)
            reader = csv.DictReader(file)
            count = 0
            total_rows = 0
            
            banknifty_list = []
            date_list = []
            time_list = []
            open_list = []
            high_list = []
            low_list = []
            close_list = []
            volume_list = []
            
            count = 0
            for row in reader:
                banknifty_list.append(row['BANKNIFTY'])
                date_list.append(row['DATE'])
                time_list.append(row['TIME'])
                open_list.append(row['OPEN'])
                high_list.append(row['HIGH'])
                low_list.append(row['LOW'])
                close_list.append(row['CLOSE'])
                volume_list.append(row['VOLUME'])
                count += 1
                
                if count == timeframe:
                    count = 0
                    banknifty = banknifty_list[0]
                    date = date_list[0]
                    time = time_list[0]
                    open_value = open_list[0]
                    high = max(high_list)
                    low = min(low_list)
                    close = close_list[-1]
                    volume = volume_list[-1]
                
                    create_candlestick = Candlestick.objects.create(
                        csv = csv_obj,
                        banknifty = banknifty,
                        date = date,
                        time = time,
                        open_value = open_value,
                        high = high,
                        low = low,
                        close = close,
                        volume = volume
                    )
                    
                    banknifty_list.clear()
                    date_list.clear()
                    time_list.clear()
                    open_list.clear()
                    high_list.clear()
                    low_list.clear()
                    close_list.clear()
                    volume_list.clear()
                    
            try:
                candles_list = list(Candlestick.objects.filter(csv=csv_obj).values(
                        'csv__csv_file',
                        'banknifty',
                        'date',
                        'time',
                        'open_value',
                        'close',
                        'high',
                        'low',
                        'volume'
                    )
                )
                if len(candles_list) > 0:
                    temp_file = open(f'{csv_obj.sys_id}.json', 'w')
                    json_obj = json.dumps(candles_list)
                    temp_file.write(json_obj)
                    temp_file.close()
                    temp_file = open(f'{csv_obj.sys_id}.json')
                    csv_obj.json_file.save(f"{csv_obj.sys_id}.json", File(temp_file))
                    temp_file.close()
                    os.remove(os.path.abspath(temp_file.name)) 
            except:
                pass
                    
        return redirect(self.success_url)
    
    
# ---------------------------------------------------------------------------- #
#                               CSVFileDetailView                              #
# ---------------------------------------------------------------------------- #


class CSVFileDetailView(DetailView):
    """
    To display the list of uploaded csv files
    """
    model = CSVFile
    template_name = 'MainApp/csvfile_detail.html'
    success_url = reverse_lazy('MainApp:csvfile_list')
    extra_context = {}
    
    def get_queryset(self, *args, **kwargs):
        queryset = super(self.__class__, self).get_queryset(*args, **kwargs)
        candles = Candlestick.objects.filter(csv_id=self.kwargs['pk'])
        self.extra_context = {'candles': candles}
        return queryset
                    
            