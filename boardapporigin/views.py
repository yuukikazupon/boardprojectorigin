from django.shortcuts import render,redirect
from .models import BoardModel,Koushin
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def listfunc(request) :

    object_list=BoardModel.objects.all()
    params_list={"object_list":object_list}
    return render(request,"list.html",params_list)

@login_required
def detailfunc(request,pk):
    object = BoardModel.objects.get(pk=pk)
    params_detail = { "object" : object }

    return render(request,"detail.html",params_detail)


# class BoardCreate(CreateView):
#     model = BoardModel
#     template_name = "create.html"
#     fields = "__all__"
#
#     success_url = reverse_lazy("list")
@login_required
def createfunc(request) :

    if request.method == "POST" :
        print(request.POST)
        print(dir(request))
        try:
            form=BoardModel.objects.create(title=request.POST["title"],content=request.POST["content"],author=request.POST["author"],image=request.FILES["image"])
            print(form.title)
            return redirect("list")
        except:
            form=BoardModel.objects.create(title=request.POST["title"],content=request.POST["content"],author=request.POST["author"])
            return redirect("list")
    else :

        return render(request,"create.html")




# class BoardUpdate(UpdateView):
#     model = BoardModel
#     template_name = "update.html"
#     fields = "__all__"
#     success_url = reverse_lazy("list")
@login_required
def updatefunc(request,pk):
    print(request.POST)
    if request.method == "POST" :
        Koushin.objects.create()
        form = BoardModel.objects.get(pk=pk)
        try :
            form.title = request.POST["title"]
            form.content = request.POST["content"]
            form.author = request.POST["author"]
            form.image = request.FILES["image"]
            form.save()
            return redirect("list")
        except :
            form.save()
            return redirect("list")
    else :

        return render(request,"update.html")



# class BoardDelete(DeleteView):
#     model = BoardModel
#     template_name = "delete.html"
#     success_url = reverse_lazy("list")
@login_required
def deletefunc(request,pk):
    object = BoardModel.objects.get(pk=pk)
    object.delete()
    return redirect("list")


def goodfunc(request,pk):
    post = BoardModel.objects.get(pk=pk)
    post.good += 1
    post.save()
    return redirect("list")


def readfunc(request,pk):
    post = BoardModel.objects.get(pk=pk)
    post1 = request.user.get_username()

    if post1 in post.read_text :
        return redirect("list")

    else :
        post.read += 1
        post.read_text = post.read_text + "" + post1
        print(post.read_text)
        post.save()
        return redirect("list")


def loginfunc(request):
    if request.method == "POST" :
        username2 = request.POST["username"]
        password2 = request.POST["password"]

        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect("list")
        else :
            return redirect("login")
    else :
        return render(request,"login.html")

def logoutfunc(request):
    logout(request)
    return redirect("login")

def signupfunc(request):

    if request.method == "POST" :
        username2 = request.POST["username"]
        password2 = request.POST["password"]



        try:
            User.objects.get(username=username2)
            return render(request,"signup.html",{"message":"このユーザーは登録されています"})

        except:
            User.objects.create_user(username2,'',password2  )
            return redirect("list")
    else :
        return render(request,"signup.html")
