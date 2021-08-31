from django.shortcuts import render

# Create your views here.
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-pk') # pk값을 역순으로 정렬

    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        }
    )

def single_post_page(requst, pk):
    post = Post.objects.get(pk=pk)

    return render(
        requst,
        'blog/single_post_page.html',
        {
            'post':post,
        }
    )