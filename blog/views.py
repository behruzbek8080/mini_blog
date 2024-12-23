from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, EditProfileForm, BlogForm
from .models import Blog, Comment

# Create your views here.
def home_view(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'index.html', context)


def blog_detail_view(request, id):
    blog = Blog.objects.get(id=id)
    context = {'blog': blog}
    return render(request, 'blog_detail.html', context)

def add_comment_view(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment=Comment(blog=blog,author=request.user  , content=comment)
        Comment.save()
        return redirect('blog_detail', id=id)
    return render(request, 'add_comment.html',)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def profile_view(request):
    user_blogs = Blog.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'user_blogs': user_blogs})


def logout_view(request):
    logout(request)
    return redirect('home')


def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

def blog_view(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


def blog_detail_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=blog)
    return render(request, 'blog_detail.html', {'blog': blog, 'comments': comments})


def create_blog_view(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)  # Rasmlarni qabul qilish uchun request.FILES
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('profile')  # Profilga qaytish
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})