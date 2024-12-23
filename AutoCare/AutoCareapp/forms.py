from django import forms
from .models import Task, Car
 
#to pull active car in a form
class TastForm(forms.ModelForm):
    def__init__(self, *args,**kwargs):
    super(TaskForm,self).__init__(*args,**kwargs)
    self.fields['car'].queryset = Car.objects.filter(is_active= True)

    class Meta:
        model = Task
        fields = ['car', 'service_type', 'descriptions', 'cost']
        labels = {'car', 'Selected Car', 'service_type', 'Task_type', 'description':'Task Description', 'cost',:'Cost (in Tshs)',}
        