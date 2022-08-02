from genericpath import exists
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from .models import Member
logined_id = None

def index(request):
    template = loader.get_template('index.html')
    if logined_id != None:
        context = {
            'logined_id':logined_id
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render({}, request))

def login(request):
    # template = loader.get_template('login.html')
    # return HttpResponse(template.render())
    return render(request, 'login.html')

def confirm_login(request):
    email = request.POST['email']
    pwd = request.POST['pwd']
    template = loader.get_template('login.html')
    
    status = 0
    ####### status 설명 #######
    # status = 0  :  default
    # status = 1  :  로그인 성공
    # status = 2  :  로그인 실패(패스워드 오류) 
    # status = 3  :  로그인 실패(회원정보 없음)
    try:
        m = Member.objects.get(email = email)
        if m.pwd == pwd:
            request.session['member_id'] = m.email
            global logined_id
            logined_id = m.name
            status = 1
        else:
            status = 2
    except Member.DoesNotExist:
        status = 3
        
    context = {
        'status':status
    }
    return HttpResponse(template.render(context, request))
    
def logout(request):
    try:
        del request.session['member_id'] # 세션의 특정 객체를 삭제
        # flush 세션 저장소를 삭제
        # clear 세션 저장소를 초기화
    except:
        pass
    return redirect(reverse('index'))

def test_1(request):
    members = Member.objects.all().values()
    # return render(request, 'template1.html')
    template = loader.get_template('template1.html')
    context = {
        'name':'Yuhyun',
        'members':members
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'template1.html')
    
def test_2(request):
    template = loader.get_template('template2.html')
    context = {
        'x': 2,
        'y': 2,
        'z':'tiger',
        'i':'tiger',
        'fruits': ['grape', 'strawberry', 'mandarine', 'cherry', 'mellon'],
        'fruits2': ['grape', 'strawberry', 'mandarine', 'cherry', 'mellon']
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse(template.render({}, request))