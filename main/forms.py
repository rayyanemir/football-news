from django.forms import ModelForm
from main.models import News
#tambahan biar bisa commit
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "category", "thumbnail", "is_featured"]