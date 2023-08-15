from django.shortcuts import render, get_object_or_404

from django.db.models import Q

from . models import Post, Category

# Create your views here.


def detail(request, slug, category_slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    return render(request, 'detail.html', {
        'post': post
    })


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    return render(request, 'category.html', {
        'category': category,
        'posts': posts
    })


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(
        intro__icontains=query) | Q(body__icontains=query))  # ma duci acolo te rog

    return render(request, 'search.html', {
        'posts': posts,
        'query': query,
    })
