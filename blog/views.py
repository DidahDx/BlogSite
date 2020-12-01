from django.shortcuts import render,redirect, get_object_or_404
from blog.models import BlogPost
from blog.forms import CreateBlogPostForm,UpdateBlogPost
from account.models import Account

# Create your views here.
def create_blog_view(request):
	context={}
	user=request.user

	if not user.is_authenticated:
		return redirect("must_authenticate")

	form=CreateBlogPostForm(request.POST or None, request.FILES or None)

	if form.is_valid():
		obj=form.save(commit=False)
		author=Account.objects.filter(email=request.user.email).first()
		obj.author=author
		obj.save()
		form=CreateBlogPostForm()
		context['form']=form
	return render(request,'blog/create_blog.html',context)


def detail_blog_view(request,slug):
	context={}
	blog_post= get_object_or_404(BlogPost,slug=slug)
	context['blog_post']=blog_post
	return render(request,'blog/detail_blog.html',context)

def edit_blog_view(request,slug):
	context={}

	user=request.user

	if not user.is_authenticated:
		return render("must_authenticate")
	
	blog_post=get_object_or_404(BlogPost,slug=slug)

	if request.POST:
		form=UpdateBlogPost(request.POST or None,request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj=form.save(commit=False)
			obj.save()
			context['success_message']="Update"
			blog_post=obj

	form=UpdateBlogPost(
		initial={
		  "title": blog_post.title,
		  "body":blog_post.body,
		  "image":blog_post.image
		})
	context['form']=form
	return render(request,'blog/edit_blog.html',context)