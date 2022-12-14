# Django imports
from django import forms

# In App Imports
from MainApp.models import CSVFile


# ---------------------------------------------------------------------------- #
#                                  CSVFileForm                                 #
# ---------------------------------------------------------------------------- #

class CSVFileForm(forms.ModelForm):
    """
    Model form to create/store csv file
    """
    class Meta:
        model = CSVFile
        fields = (
            'csv_file',
            'timeframe',
        )
        
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
                
    def clean(self, *args, **kwargs):
        cleaned_data = super(self.__class__, self).clean(*args, **kwargs)
        
        timeframe = cleaned_data.get('timeframe')
        if timeframe < 1:
            raise forms.ValidationError("Timeframe can not be less than 1 min")
        
        return cleaned_data
        