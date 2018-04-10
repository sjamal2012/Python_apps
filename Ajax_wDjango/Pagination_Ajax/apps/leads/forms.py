from django.forms import ModelForm
from django.forms.extras import SelectDateWidget

class SurveyFormA(forms.ModelForm):

    registered_datetime = forms.DateField(widget=extras.SelectDateWidget(), required=False)
