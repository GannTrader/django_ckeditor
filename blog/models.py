from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class blogModel(models.Model):
	title = models.CharField(max_length = 255)
	body = RichTextUploadingField()

	def __str__(self):
		return self.title