from django.contrib import admin
from.models import TagModel,AuthorModel,PostsModel
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
      
      prepopulated_fields={'slug':('titlee',)}

      list_display=['titlee','author','date']


admin.site.register(TagModel)
admin.site.register(AuthorModel)
admin.site.register(PostsModel,PostsAdmin)
 