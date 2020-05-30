from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details}) 

def new(request):
    return render(request, 'new.html')   

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #객체.delete()하면 데이터베이스에서 지우는거임
    return redirect('/blog/'+str(blog.id))    #위에 있는 것 다 처리한 다음에 URL로 넘겨라   #blog.id는 int형인데 url은 항상 str형이기때문에 str형변환해줘야함

# def blogpost(request):
#     if request.method == 'POST':
#         form = BlogPost(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.pub_date = timezone.now()
#             post.save() #post를 저장
#             return redirect('home')
#     else:
#         form = BlogPost()
#         return render(request, 'new.html', {'form':form})
def blogpost(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})