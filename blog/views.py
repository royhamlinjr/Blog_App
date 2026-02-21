from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post,About
from django.core.paginator import Paginator
from .forms import ContactForm

# TESTING Purpose
logger = logging.getLogger("TESTING")

# Create your views here.

def index(request):

    # getting data from post model
    posts = Post.objects.all()
    
    # Pagination
    paginator = Paginator(posts,5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request,'blog/index.html',{'page_obj':page_obj})

def detail(request,slug):
     post = get_object_or_404(Post, slug=slug)
     related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)[:5]
     return render(request,'blog/detail.html',{'post':post,'related_posts':related_posts})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if form.is_valid():
            logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')                
            success_message = 'Your Email has been sent!'
            return render(request,'blog/contact.html',{'form':form,'success_message':success_message})

        else:
            logger.debug('Form Validation Error')
        return render(request,'blog/contact.html',{'form':form,'name':name,'email':email,'message':message})     
    return render(request,'blog/contact.html')

def about_page(request):
    about_content = About.objects.first().content
    return render(request,'blog/about.html',{'about_content':about_content})

# Redirection Pages
# def old_url(request):
#     return redirect(reverse('blog:newpage'))

# def new_url(request):
#     return HttpResponse("New Page is here")