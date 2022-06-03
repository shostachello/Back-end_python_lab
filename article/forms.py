from django import forms

from article.models import ArticleImage


class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'multiple':
                True}))


class Meta:
    model = ArticleImage
    fields = '__all__'
