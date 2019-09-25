from django.contrib import admin
from accounts.models import Book

# 2.0以上使用装饰器
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('id', 'book_name', 'date_public')

admin.site.unregister(Book)
admin.site.register(Book, BookAdmin)
