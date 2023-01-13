from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from scrapui.forms import RegistrationForm ,Scrapform
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.


from scrapui.models import ScrapItem

def Home(request) :
    template = 'scrapui/index.html'
    context = {}
    scrap = ScrapItem.objects.all()[:5]
    context['scrap'] = scrap
    return render(request,template,context)


def register (request ) :
    template = 'scrapui/register.html'
    context = {}

    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST' :
        form = RegistrationForm(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, f'Your account has been created successfully!')    
            return redirect('signin')
    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, template, context)



def signin( request ) :
    template = 'scrapui/signin.html'
    context = {}

    if request.user.is_authenticated:
        return redirect('/')

    elif request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username, password=password)
        if user:
            login(request ,user)
            return redirect('/')
        else:
            messages.error(request , 'email and password is incorrect')
    return render(request, template, context)


def profile(request) :
    template = 'scrapui/profile.html'
    context = {}
    if not request.user.is_authenticated:
        return redirect('/')
    return render (request , template , context)

def logoutuser(request):
    logout(request)
    return redirect('signin')


def deactivate( request ) :
    if request.method == 'POST' :
        username = request.POST.get('name')
        if username == request.user.username :
            User.objects.get(username=username,email=request.user.email).delete()
            logout(request)
            return redirect('signin')
        else:
            messages.error(request , 'Username is incorrect')
            return redirect('profile')
    else :
        messages.error(request , 'unable to deactivate your account')
        return redirect('profile')

def addscrap(request ) :
    template = 'scrapui/createscrap.html'
    context = {}
    if request.method == 'POST' :
        form = Scrapform(request.POST , request.FILES)
        if form.is_valid() :
            print(request.user)
            
            print(request.FILES['images'])
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, f'Scrap adding successfully!')    
            return redirect('listscrap')
    else:
        form = Scrapform()

    context['form'] = form

    return render ( request , template , context )

def listscrap( request ) :
    template = 'scrapui/listscrap.html'
    context = {}
    scrap = ScrapItem.objects.all()
    page = Paginator(scrap , 1 )
    number_page = request.GET.get('page',1)

    try:
        p_n = page.get_page( number_page )
    except PageNotAnInteger :
        p_n = p.page(1)
    except Emptypage :
        p_n = p.page(p.num_pages)

    context['page'] = p_n

    if request.method == 'POST' :
        getdata = request.POST.getlist('data')
        print(getdata)
        for datas in getdata :
            ScrapItem.objects.filter(id=datas , user=request.user).delete()
        if len(getdata) <= 0:
            messages.info(request , "Please Selected,it's Empty! ")    
        return redirect('listscrap')

    context['scrap'] = scrap
    return render( request , template , context )

def viewscrap( request , id ) :
    template = 'scrapui/viewscrap.html'
    con = {}
    getid = get_object_or_404(ScrapItem , id=id)
    scrap = ScrapItem.objects.all()[:3]

    con['data'] = getid
    con['scrpa'] = scrap
    return render(request , template ,con )



def editscrap( request ,id  ) :
    template = 'scrapui/editscrap.html'
    context = {}
    user = User.objects.get(username=request.user.username,email=request.user.email)
    getid = get_object_or_404(ScrapItem , id=id)
    print( getid.user , request.user )

    if request.method == 'POST' :
        form = Scrapform(request.POST , request.FILES , instance=getid)
        if form.is_valid() :

            if getid.user == request.user:
                f = form.save(commit=False)
                f.user = request.user
                f.save()
                messages.success(request, f'Scrap adding successfully!')  
            else:
                messages.success(request, f'Unauthorized!')

            return redirect('listscrap')
    else:
        form = Scrapform(instance=getid)
    context['form'] = form

    return render( request , template , context )

def deletescrap ( request ) :
    getid = get_object_or_404(ScrapItem , id=id)
    return redirect('viewscrap')
    

from django.views.decorators.csrf import csrf_exempt, csrf_protect
# @csrf_exempt
# @csrf_protect
from django.views.decorators.csrf import requires_csrf_token

# @requires_csrf_token
@csrf_exempt
def chat( request ) :
    datas = [{'name': 'Peter', 'email': 'peter@example.org'},
            {'name': 'Julia', 'email': 'julia@example.org'}]
    template = 'scrapui/index.html'
    context = {
        'message' : 'hello'
    }
    if request.method == 'POST':
        data = request.GET.get('bot')
        print(data)
        return JsonResponse(context ,safe=False)
    
    return render(request,template,context)