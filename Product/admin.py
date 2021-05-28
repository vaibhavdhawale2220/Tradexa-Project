from django.contrib import admin
from Product.models import Product
from User.models import User
from User.models import Post

# Register your models here.
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Post)



