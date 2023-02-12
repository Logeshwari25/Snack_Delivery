from django.shortcuts import render,redirect

from .models import blog,orders
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def before_home(request):
    return render(request,"login/login.html")

def signup(request):
    return render(request,"login/signup.html")

def login_usr(request):
    usr_name = request.POST.get('user')
    password = request.POST.get("password")
    print(usr_name,password)
    user = authenticate(username=usr_name, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect(home)
    else:
        return render(request,"login/login.html")

def home(request):
    return render(request,"index.html")

def create_user(request):
    datas = ['#usr_name','#email','#password','#confirm-password']
    usr_name = request.POST.get(datas[0])
    mail = request.POST.get(datas[1])
    password = request.POST.get(datas[2])
    con_pass = request.POST.get(datas[3])
    print(mail,usr_name)
    if password == con_pass :
        user = User.objects.create_user(mail, usr_name, password)
        user.save()
        print("user added sucessfully..........")

    return render(request,"login/login.html")



def get_blog():
    images = blog.objects.all()
    cat = []
    temp = []
    items = []
    for i in images:
        cat.append(i.categories)
    for i in list(set(cat)):
        temp = []
        for j in images:
            if i == j.categories :
                temp.append(j)
        items.append(temp)
    for x,i in enumerate(items):
        items[x] = i[::-1]
    return items
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def view_order(request):
    obj = orders.objects.all()

    return render(request,"order/view_order.html",{"orders":obj})

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def make_order(request):
    cost = request.POST.get('#cost')
    number = request.POST.get('#number')
    address = request.POST.get('#address')
    food_details = request.POST.get('#food_details')
    foodname = request.POST.get('#foodname')
    fullname = request.POST.get('#fullname')

    obj = orders(Full_Name=fullname,Food_Name=foodname,Number=number,Food_Details=food_details,Your_Address=address,How_Much=cost)
    obj.save()


    return render(request,"order/view_order.html")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def blog_edit(request):
    return render(request,"blog/blog_edit.html")

def save_blog(request):
    ids = ['#title','#description','#content','#Category','#Thumbnail']
    title = request.POST.get(ids[0])
    description = request.POST.get(ids[1])
    content = request.POST.get(ids[2])
    Category = request.POST.get(ids[3])
    Thumbnail = request.POST.get(ids[4])

    obj = blog(title=title,description=description,content=content,categories=Category,blog_profile_img=Thumbnail)
    obj.save()
    ob = blog.objects.all()
    for i in ob:
        print(i.blog_profile_img,i.title,i.content)

    return render(request,"blog/blog_edit.html")

def save_edit_blog(request,pk):
    ids = ['#title','#description','#content','#Category','#Thumbnail']
    title = request.POST.get(ids[0])
    description = request.POST.get(ids[1])
    content = request.POST.get(ids[2])
    Category = request.POST.get(ids[3])
    Thumbnail = request.POST.get(ids[4])

    obj = blog.objects.get(id=pk)
    obj.content = content
    obj.title = title
    obj.description = description
    obj.categories = Category
    obj.blog_profile_img = Thumbnail
    obj.save()

    print("Saved...........")

    return render(request,"blog/blog_edit.html")


def list_blog(request):
    items = get_blog()
    return render(request,"blog/blog.html",{'blogs':items})

def view_blog(request,pk):
    page = blog.objects.get(id=pk)
    items = get_blog()
    return render(request,"blog/content.html",{'blog':page,'item':items,'blogs':items})

def delete_blog(request):
    bl_id = request.GET.get("id")
    page = blog.objects.get(id=bl_id)
    page.delete()
    return render(request,"blog/view_blog.html",{'blog':page})


def list_edit_blog(request):
    items = get_blog()
    return render(request,"blog/edit_blog_list.html",{'blogs':items})

def edit_blog(request,pk):
    obj = blog.objects.get(id=pk)
    return render(request,"blog/blog_re_edit.html",{'obj':obj})
