from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import login_table, police_station, report_table


def admin_home(request):
    return render(request,'ADMIN/admin home.html')

def login(request):
    return render(request,'ADMIN/login.html')

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    a=login_table.objects.get(username=username,password=password)
    request.session['lid']=a.id
    if a.type=='admin':
        return HttpResponse('''<script>alert('admin logined..');window.location='/admin_home'</script>''')
    elif a.type=='police':
        return HttpResponse('''<script>alert('police logined..');window.location='/police_home'</script>''')
    else:
        return HttpResponse('''<script>alert('invalid..');window.location='/'</script>''')


def manage_police_station(request):
    return render(request, "ADMIN/manage police station.html")

def add_new(request):
    return render(request,'ADMIN/add police.html')


def add_new_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    district = request.POST['textfield5']
    email = request.POST['textfield6']
    phone = request.POST['textfield7']
    latitude = request.POST['textfield8']
    longitude = request.POST['textfield9']
    username = request.POST['textfield10']
    password = request.POST['textfield11']

    a = login_table()
    a.username = username
    a.password = password
    a.type = 'police'
    a.save()

    C = police_station()
    C.name = name
    C.place = place
    C.post = post
    C.pin = pin
    C.district = district
    C.email = email
    C.phone = phone
    C.longtitude = longitude
    C.langtitude = latitude
    C.LOGIN = a
    C.save()
    return HttpResponse('''<script>alert('added police station..');window.location='/'</script>''')


def view_complaint(request):
    return render(request, 'ADMIN/view complaints.html')

def view_police_station(request):
    return render(request,'ADMIN/view police station.html')

def view_user(request):
    return render(request,'ADMIN/view user.html')

def reply_send(request):
    return render(request,'ADMIN/send rply.html')

def police_home(request):
    return render(request,'POLICE/police home.html')

def police_view_report(request):
    ob=report_table.objects.filter(POLICE_STATION__LOGIN_id=request.session['lid'])
    return render(request, 'POLICE/police view report.html',{'val':ob})

def reply_police(request):
    return render(request,'POLICE/replay police.html')

def send_reply(request):
    return render(request,'POLICE/send rply.html')

def complaint_police(request):
    return render(request,'POLICE/view complaint police.html')
