from django.contrib import admin
from freeshelf.models import Book
# from freeshelf.models import Categories


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('name', 'author', 'description', 'date_added')
    prepopulated_fields = {'slug': ('name',)}


# class CategoriesAdmin(admin.ModelAdmin):
#     model = Categories
#     list_display = ('book', 'type')
#     prepopulated_fields = {'slug': ('book',)}

admin.site.register(Book, BookAdmin)
# admin.site.register(Categories, CategoriesAdmin)
