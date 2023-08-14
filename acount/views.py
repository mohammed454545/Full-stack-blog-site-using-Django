from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import auth
from corse.models import Corses
import re

# Create your views here.
def profile (request):
    if request.user.is_authenticated:
        context={
            'full_name':request.user.userprofile.full_name,
            'name':request.user.username,
            'email':request.user.email,
            'age': request.user.userprofile.age,
            'job':request.user.userprofile.job,
            'img':request.user.userprofile.img
        }
    else:
        context=None
    return render(request, 'pges/profile.html',context)
def sign_in (request):
    if request.method == 'POST' and 'btnlogin' in request.POST:
        name=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request, user)
        else:
            messages.success(request, 'خطء في كلمة المرور او في اسم المستخدم')
        return redirect('sign_in')
    else:
        return render(request, 'pges/sign_in.html')
def sign_up (request):
    if request.method == 'POST'and 'btnlogup' in request.POST:
        # varieables for fields
        full_name=None
        name=None
        age=None
        job=None
        emaile=None
        password=None
        repass=None
        pro_img=None
        is_added=False
        # get values from the form
        if 'name' in request.POST : name =request.POST['name']
        else : messages.error(request, 'خطء في الاسم')
        if 'name' in request.POST : name =request.POST['name']
        else : messages.error(request, 'خطء في اسم المستخدم')
        if 'age' in request.POST : age =request.POST['age']
        else : messages.error(request, 'خطء في العمر')
        if 'job' in request.POST : job =request.POST['job']
        else : messages.error(request, 'خطء في العمل')
        if 'email' in request.POST : emaile =request.POST['email']
        else : messages.error(request, 'خطء في الايميل')
        if 'password' in request.POST : password =request.POST['password']
        else : messages.error(request, 'خطء في كلمة المرور')
        if 'pro_img' in request.POST : pro_img =request.POST['pro_img']
        else : messages.error(request, 'خطء في الصورة الشخصية')
        if 'repass' in request.POST : repass =request.POST['repass']
        else : messages.error(request, 'خطء في اعادة كلمة المرور')
        if name and age and job and emaile and password:
            if User.objects.filter(email=emaile).exists():
                messages.error(request, "عنوان بريد الكتروني مستخدم من قبل يرجى تسجيل الدخول")
            else:
                if User.objects.filter(username=name).exists():
                    messages.error(request, "هذا الاسم مستخدم من قبل")
                else:
                    if repass==password:
                        patt="^\w+([-+.']\w+)*@\w+([-.]\w)*\.\w+([-.]\w+)*$"
                        if re.match(patt,emaile):
                            user=User.objects.create_user(
                                username=name,email=emaile,password=password
                            )
                            user.save()
                            userprofile=UserProfile(user=user,age=age,job=job)
                            userprofile.save()
                            #clear
                            full_name=''
                            name=''
                            age=''
                            job=''
                            emaile=''
                            password=''
                            repass=''
                            pro_img=''
                            messages.success(request, "تم انشاء الحساب بنجاح")
                            is_added=True
                        else:
                            messages.error(request, "يرجى ادخال بريد الكتروني صالح")
                    else:
                        messages.error(request, "حقل كلمة المرور و حقل تأكيد كلمة المرور غير متطابقين")
        else:
            messages.error(request, "يرجى ملء جميع الحقول")
        return render(request, 'pges/sign_up.html',{
            'full_name':full_name,
            'name':name,
            'age':age,
            'job':job,
            'email':emaile,
            'password':password,
            'repass':repass,
            'is_added':is_added,
            'pro_img':pro_img
        })
    else:
        return render(request, 'pges/sign_up.html')
def logout (request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index')
def fav_cors (request,cors_id):
    corss=Corses.objects.all()
    if request.user.is_authenticated and not request.user.is_anonymous:
        cor_fav=Corses.objects.get(pk=cors_id)
        if UserProfile.objects.filter(user=request.user,cors_fav=cor_fav).exists():
            messages.success(request, 'تم اضافة الدورة مسبقا الى قائمة المفضلات')
        else:
            userprofile=userprofile.objects.get(user=request.user)
            userprofile.cors_fav.add(cor_fav)
            messages.success(request, 'تم اضافة الدورة الى المفضلات بنجاح' )
    return redirect('/corse/'+str(cors_id))