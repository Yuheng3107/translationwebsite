from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator
class Genre(models.Model):
    # Defines Genres in the database
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name

class WordType(models.Model):
    # Defines the Category a Translated Word belongs to
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type



class Record(models.Model):
    # One Record of a Translated Word
    word_type = models.ForeignKey(WordType, on_delete=models.CASCADE)
    original_word = models.CharField(max_length=100, unique=True)
    translated_word = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="updated_by")
    comments = models.TextField()

    def __str__(self):
        return f"Original Word: {self.original_word}\n Translated Word: {self.translated_word}"


class Novel(models.Model):
    # Allows us to store data for a specific Novel in the database
    title = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(5, "Title must be longer than 5 characters")])
    synopsis = models.TextField()
    genres = models.ManyToManyField(Genre, related_name="genres")
    raws = models.FileField(upload_to='translators/parsing_stuff/')
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=256, null=True, help_text='The MIMEType of the file') 

    def __str__(self):
        return self.title

class Chapter(models.Model):
    # Allows us to store data for a specific chapter of a novel in the database
    name = models.CharField(max_length=100, unique=True)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    content = models.TextField()
    translator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='translator_name', null=True)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='editor_name', null=True)

    def __str__(self):
        return f"Chapter Name: {self.name}"














