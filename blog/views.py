from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk' # pk값을 역순으로 정렬

class PostDetail(DetailView):
    model = Post

# def index(request):
#     posts = Post.objects.all().order_by('-pk') # pk값을 역순으로 정렬
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts' : posts,
#         }
#     )
#
# def single_post_page(requst, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         requst,
#         'blog/post_detail.html',
#         {
#             'post':post,
#         }
#     )