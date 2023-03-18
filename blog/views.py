from django.shortcuts import render, get_object_or_404
from datetime import date
from.models import PostsModel,AuthorModel,TagModel
from django.views.generic import TemplateView, ListView , DetailView
from django.views import View
from .forms import CommentsForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.




class HomeTemplateView(TemplateView):
    template_name='blog/home.html'
    def get_context_data(self, **kwargs):
        sorted_posts=PostsModel.objects.all().order_by('-date')
        latest_three=sorted_posts[:3]
        context=super().get_context_data(**kwargs)
        context["latest_three"]= latest_three
        return context
    


class PostsListView(ListView):
    template_name='blog/all_posts.html'
    model=PostsModel
    context_object_name='posts'
    ordering=['-date']
    


class PostView(View):
    def get(self,request,slug):
        post=get_object_or_404(PostsModel, slug=slug)
        stored_slugs=request.session.get('stored_slugs')
        if stored_slugs is not None:
            readlater= post.slug in stored_slugs
        else:
            readlater=False
        
        post_tags=post.tags.all()
        commentform=CommentsForm()
        comments=post.comments.all()

        return render(request,'blog/post_detail.html',{
            'post':post,
            'post_tags':post_tags,
            'commentform':commentform,
            'comments':comments,
            'readlater':readlater
        }
                      )
    def post(self,request,slug):
        
        submitted_comment=CommentsForm(request.POST)
        post=get_object_or_404(PostsModel, slug=slug)
        
        
        stored_slugs=request.session.get('stored_slugs')
        if stored_slugs is not None:
            readlater= post.slug in stored_slugs
        else:
            readlater=False
        comments=post.comments.all()
        if submitted_comment.is_valid():
            comment=submitted_comment.save(commit=False)
            comment.post=post
            comment.save()
            redirected_path=reverse('post-detail',args=[slug])
            return HttpResponseRedirect(redirected_path)
        
        post_tags=post.tags.all()
        commentform=CommentsForm(request.POST)
        

        return render(request,'blog/post_detail.html',{
            'post':post,
            'post_tags':post_tags,
            'commentform':commentform,
            'comments':comments,
            'readlater':readlater
        }
                      )


class ReadLaterView(View):
     def get(self,request):
        stored_slugs=request.session.get('stored_slugs')
        if  stored_slugs is None or len(stored_slugs)==0:
            has_posts=False
            posts=[]
        else:
            has_posts=True
            posts= PostsModel.objects.filter(slug__in=stored_slugs)


        return render(request, 'blog/read-later.html',{
                'posts':posts,
                'has_posts':has_posts 
        })
   
   
     def post(self,request):
        
        post_slug=request.POST['post_slug']
        stored_slugs=request.session.get('stored_slugs')
        if stored_slugs is None:
            stored_slugs=[]
        if post_slug not in stored_slugs:
            stored_slugs.append(post_slug)
            
        else:
            stored_slugs.remove(post_slug)
        request.session['stored_slugs']=stored_slugs
        return HttpResponseRedirect('/')
    
   
