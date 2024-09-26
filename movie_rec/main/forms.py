from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    file = forms.FileField(required=False)

    class Meta:
        model = Movie
        fields = "__all__"

    def save(self, commit=True):
        instance = super().save(commit=False)

        uploaded_file = self.cleaned_data.get("file")
        if uploaded_file:
            instance.thumbnail = uploaded_file.read()

        if commit:
            instance.save()

        return instance

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)