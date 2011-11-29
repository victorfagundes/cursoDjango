from django.shortcuts import render
from models import Post, Comment
from forms import CommentForm

def posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", locals())

def post(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm()
    comments = Comment.objects.filter(post = post, approved = True)
    teve_comentario = False
    if request.method == 'POST':
        comment = Comment(post=post)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            teve_comentario = True
            form.save()
    return render(request, "post.html", locals()) 
    
