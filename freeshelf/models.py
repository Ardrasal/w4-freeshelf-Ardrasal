from django.db import models
from django.template.defaultfilters import slugify

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField()
    date_added = models.DateField()
    # category = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    # def get_categories(self):
    #     categories = []
    #     if self.fiction:
    #         categories.append("Fiction")
    #     if self.classic:
    #         categories.append("Classic")
    #     if self.non_fiction:
    #         categories.append("Nonfiction")
    #     return categories

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
            super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# class Categories(models.Model):
#     book = models.ForeignKey(to='Book', related_name='type', on_delete=models.CASCADE)
#     type = models.ManyToManyField(Book)
#     slug = models.SlugField(unique=True)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = slugify(self.book)
#             super(Categories, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.type
