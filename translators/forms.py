from django import forms
from .models import Novel, Genre
from django.core.files.uploadedfile import InMemoryUploadedFile
from translators.humanize import naturalsize

class NovelForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'picture'
    
    class Meta:
        model = Novel
        fields = ['title', 'synopsis', 'genres', 'picture']
    
    genres = forms.ModelMultipleChoiceField(
        queryset = Genre.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < " + self.max_upload_limit_text + " bytes")

    def save(self, commit=True):
        instance = super(NovelForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()
            self.save_m2m()

        return instance



    
