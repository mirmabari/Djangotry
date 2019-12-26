from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
from mir.models import Post
from .models import Register
from reportlab.pdfgen import canvas
import csv
from django.core.mail import send_mail
from Mywebsite import settings

def index(request):
    post = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return  render(request,'mir/post_list.html', {'posts':post})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mir/post_detail.html', {'post': post})
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/mir', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mir/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #return  render(request,'mir/post_list', {'form': form})
            #return render(request, 'mir/post_list.html', {'post' : form})
            return redirect("/mir")
    else:
        form = PostForm(instance=post)
    return render(request, 'mir/post_edit.html', {'form': form})
def post_delete(request, pk):
        employee = Post.objects.get(id=pk)
        employee.delete()
        return redirect("/mir")
def csvf(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    writer = csv.writer(response)
    writer.writerow(['1001', 'John', 'Domil', 'CA','Developer'])
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', 'Testing'])
    writer.writerow(['101','Mir Bari','Kashmir','Software Engineer'])
    return response
def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    employees = Post.objects.all()
    writer = csv.writer(response)
    for employee in employees:
        writer.writerow([employee.id,employee.title,employee.text,employee.created_date,employee.published_date])
    return response
def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100,700, "Chetu ! ")
    p.showPage()
    p.save()
    return response
def email(request):
    subject = "Greetings"
    msg = "Congratulations for your success"
    to = "mirmabari@gmail.com"
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if (res == 1):
        msg = "Mail Sent Successfuly"
    else:
        msg = "Mail could not sent"
    return HttpResponse(msg)
def register(request):
    if request.method == "POST":
        MyLoginForm = PostForm(request.POST)
        if MyLoginForm.is_valid():
            post = MyLoginForm.save(commit=False)
            post.fname = request.user
            post.save()
            return redirect('/mir')
    else:
        MyLoginForm = Register()

    return render(request, 'mir/register.html', {'form': MyLoginForm})
def regget(request):
    post = Register(request.POST)
    return render(request, 'mir/reg_list.html', {'posts': post})


