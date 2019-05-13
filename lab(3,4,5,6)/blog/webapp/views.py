from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import UserReg
from .models import Post

def index(request):
	post = Post.objects.filter()
	return render(request, 'webapp/index.html', {"posts": post})

def articles(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'webapp/articles.html', {"post": post})

def authorization(request):
	return render(request, 'webapp/authorization.html')

def registration(request):
	if request.method == "POST":
		form = UserReg(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'{username} успешно зарегистрирован!')
			return redirect('authorization')
	else:
		form = UserReg()
	return render(request, 'webapp/registration.html', {'form': form})

def create(request):
	if not request.user.is_anonymous:
		if request.method == "POST":
			form = {
				'text': request.POST["text"],
				'title': request.POST["title"]
			}
			if form["text"] and form["title"]:
				Post.objects.create(text=form["text"], title=form["title"], author=request.user)
				post = Post.objects.get(title=form['title'])
				return redirect('articles', pk=post.id)
			else:
				form['errors'] = u"Не все поля заполнены"
				return render(request, 'post/create.html', {'form': form})
		else:
			return render(request, 'webapp/create.html', {})
	else:
		raise Http404