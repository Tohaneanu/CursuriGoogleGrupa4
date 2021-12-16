from django import forms

from jobs.models import Job


class JobsForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

    def __init__(self, pk, *args, **kwargs):
        super(JobsForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        name_value = cleaned_data.get('name')
        customer_value = cleaned_data.get('customer')

        if self.pk:
            if Job.objects.filter(name__icontains=name_value, customer__name__icontains=customer_value,
                                  active=1).exclude(
                    id=self.pk).exists():
                self._errors['name'] = self.error_class(["Error"])
        else:
            if Job.objects.filter(name__icontains=name_value, customer__name__icontains=customer_value,
                                  active=1).exists():
                self._errors['name'] = self.error_class(["Error"])
        return cleaned_data
