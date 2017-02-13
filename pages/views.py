from django.shortcuts import render, redirect
from article.models import Article
from pages.forms import ContactForm
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template


def index(request):
    article_list = Article.objects.all().order_by('-pub_date')
    context = {
        'article_list': article_list
    }
    return render(request, 'pages/index.html', context)


def search(request):
    if request.method == 'POST':
        search_input = request.POST.get('search')
        article_list = Article.objects.all().filter(
            title__contains=search_input)
        context = {
                'article_list': article_list,
                'search_input': search_input
        }
        return render(request, 'pages/index.html', context)


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            # Email the profile with the contact information
            template = get_template('pages/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "DiceGmaeTech" + '',
                ['adrien.marcenat@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('pages:contact')
    return render(request, 'pages/contact.html', {'form': form_class, })
