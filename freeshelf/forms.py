from django import forms
from freeshelf.models import Book


# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ('name', 'author', 'description', 'date_added')


class SearchForm(forms.Form):
    fiction = forms.BooleanField(
        label="Fiction", required=False, label_suffix="")
    nonfiction = forms.BooleanField(
        label="Nonfiction", required=False, label_suffix="")
    classic = forms.BooleanField(
        label="Classic", required=False, label_suffix="")

    def search(self):
        if not self.is_valid():
            return None

        data = self.cleaned_data
        books = Book.objects.all()
        if data['fiction']:
            books = books.filter(fiction=True)
        if data['nonfiction']:
            books = books.filter(nonfiction=True)
        if data['classic']:
            books = books.filter(classic=True)
        return books
