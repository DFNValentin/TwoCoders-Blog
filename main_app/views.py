from django.shortcuts import render, redirect

from django.http import HttpResponse

from blog.models import Post, Resources

from django.core.mail import send_mail

from blog.forms import ContactForm

from django.template.loader import render_to_string


# Create your views here.


def index(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, "index.html", {
        'posts': posts
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'New message on Two Coders Blogs '

            html = render_to_string('contactForm.html', {
                'name': name,
                'email': email,
                'message': message
            })

            send_mail(subject, message, 'valentin@two-coders.site',
                      ['valentin@two-coders.site'], html_message=html)

            return redirect('index')

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


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
