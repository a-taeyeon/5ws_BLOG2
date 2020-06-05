from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .form import BlogPost



#CRUD
# def create(request):  #form을 사용한 create
#     #새로운 데이터 블로그 글 저장하는 역할 == POST
#     if request.method == 'POST':
#         #입력된 블로그 글들을 저장해라
#         form = BlogPost(request.POST)
#         if form.is_valid:
#             post = form.save(commit=False)
#             post.pub_date = timezone.now()
#             post.save()
#             return redirect('home')

#     #글쓰기 페이지를 띄워주는 역할 == GET
#     else:
#         #단순히 입력받을 수 있는 form을 띄워줘라
#         form = BlogPost()
#         return render(request, 'create.html', {'form':form})

#     return

# def update(request, u_id): #아래의 update함수대신 이 함수를 쓰게되면 수정버튼을 누를경우 새 글이써진다....
#     #어떤 블로그를 수정할지 블로그 객체를 갖고오기
#     blog = get_object_or_404(Blog, pk = u_id)

#     #해당하는 블로그 객체 번호(pk)에 맞는 입력공간
#     form = BlogPost(request.POST, instance=blog)

#     if form.is_valid():
#         form.save()
#         return redirect('home')

#     return render(request, 'new.html', {'form':form})

def update(request, u_id):
    blog = get_object_or_404(Blog, pk = u_id)

    if request.method == 'POST':
        blog.title = request.POST['t']
        blog.body = request.POST['b']
        blog.save()
        return redirect('/blog/'+str(u_id))

    else:
        return render(request, 'update.html', {'blog2':blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('home')

##여기까지 CRUD    



def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details}) 

def new(request):
    return render(request, 'new.html')   

#얘가 있어야 http://127.0.0.1:8000/blog/new/ 가 제대로 돌아감   #form을 사용하지 않은 create
def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #객체.delete()하면 데이터베이스에서 지우는거임
    return redirect('/blog/'+str(blog.id))    #위에 있는 것 다 처리한 다음에 URL로 넘겨라   #blog.id는 int형인데 url은 항상 str형이기때문에 str형변환해줘야함

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