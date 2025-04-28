from django import forms
from posts.models import Category, Tag
from posts.models import Post

class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField()
    content = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())


    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if (title and content) and (title.lower() == content.lower()):
            raise forms.ValidationError (message = "title and content should not be same")
        return cleaned_data
    

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError(message="title cant be eqial to python")
        return title
    
    
class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "tags"]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if (title and content) and (title.lower() == content.lower()):
            raise forms.ValidationError (message = "title and content should not be same")
        return cleaned_data
    

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == "python":
            raise forms.ValidationError(message="title cant be eqial to python")
        return title


class SearchForm(forms.Form):
    search_q = forms.CharField(required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    orderings = (
        ("title", "По названию"),
        ("-title", "По названию в обратном порядке"),
        ("rate", "По рейтингу"),
        ("-rate", "По рейтингу в обратном порядке"),
        ("created_at", "По дате создания"),
        ("-created_at", "По дате создания в обратном порядке"),
        ("updated_at", "По дате обновления"),
        ("-updated_at", "По дате обновления в обратном порядке"),
        (None, None),
    )

    ordering = forms.ChoiceField(choices=orderings, required=False)