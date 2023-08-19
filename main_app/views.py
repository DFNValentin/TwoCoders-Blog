from django.shortcuts import render

from django.http import HttpResponse

from blog.models import Post, Resources

# Create your views here.


def index(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, "index.html", {
        'posts': posts
    })


def contact(request):
    return render(request, "contact.html")


def resources(request):
    resources = Resources.objects.all()
    return render(request, "resources.html", {
        'resources': resources
    })


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]

    return HttpResponse("\n".join(text), content_type="text/plain")
