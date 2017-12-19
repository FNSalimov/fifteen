from django.forms import ModelForm
from english.models import Word

class WordForm(ModelForm):
	class Meta:
		model = Word
		fields = ['title', 'defenition', 'belongs']