from django.db import models

# Create your models here.

class AuthorModel(models.Model):
     first_name=models.CharField(max_length=50)
     last_name=models.CharField(max_length=50)
     email=models.EmailField(null=True)
     def __str__(self):
          return (f'{self.first_name} {self.last_name}')
     


class TagModel(models.Model):
     tag=models.CharField(max_length=20)
     def __str__(self):
          return (f'{self.tag}')
     



class PostsModel(models.Model):
    
      titlee=models.CharField(max_length=50)
      author= models.ForeignKey(AuthorModel,on_delete=models.CASCADE, null=True)
      date= models.DateField()
      img=models.ImageField(upload_to='posts', null=True)
      slug=models.SlugField(unique=True, db_index=True)
      summary= models.CharField(max_length=200)
      content=models.TextField()
      tags=models.ManyToManyField(TagModel)
      def __str__(self):
          return (f'{self.titlee} by {self.author.first_name} {self.author.last_name}')

class CommentModel(models.Model):

     user_name= models.CharField(max_length=100)
     user_email= models.EmailField()
     text=models.TextField()
     post=models.ForeignKey(PostsModel, on_delete=models.CASCADE, related_name='comments')