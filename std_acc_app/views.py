from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from std_acc_app.forms import RegisterForm

# Create your views here.
from std_acc_app.models import Advertisement, User


def home(request):
    return render(request, 'index.htm')


def advertisement(request):
    # fetch and list all the advertisements
    ads = Advertisement.objects.all()
    context = {'ads': ads}
    return render(request, 'advertisement.htm', context)


def reports(request):
    # display the report based on different queries
    # 11 means November because it is the 11th month
    # if `Dubai` was used in address it'll count it
    no_user = User.objects.all().count()
    no_d_users = User.objects.filter(date_joined__month=11).count()
    no_s_users = 3  # currently user locations are not attached
    no_ads = Advertisement.objects.all().count()
    no_d_ads = Advertisement.objects.filter(date__month=11).count()
    no_s_ads = Advertisement.objects.filter(address__contains='Dubai').count()
    context = {'no_user': no_user,
               'no_d_users': no_d_users,
               'no_s_users': no_s_users,
               'no_ads': no_ads,
               'no_d_ads': no_d_ads,
               'no_s_ads': no_s_ads, }
    return render(request, 'report.htm', context)


def user_registration(request):
    # view for handling user-registration using custom forms and models
    if request.user.is_authenticated:
        context = {'is_login': True}
        return render(request, 'login.htm', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'registration.htm')


def user_login(request):
    # this function is for handling the login functionality of app
    if request.user.is_authenticated:
        context = {'is_login': True}
        return render(request, 'login.htm', context)
    if request.method == 'POST':
        uname = request.POST.get('usrname')
        passwd = request.POST.get('pwd')
        person = authenticate(request, username=uname, password=passwd)
        if person is not None:
            login(request, person)
            return redirect('login')
    return render(request, 'login.htm')


@login_required(login_url='login')
def user_logout(request):
    # this function is used to logout the landlord or student
    logout(request)
    return redirect('login')


def manage_ad_ll(request):
    # this function only show ads that are by relevant landlord
    user = request.user
    c_user_ads = Advertisement.objects.filter(add_by=user)
    context = {'ads': c_user_ads}
    return render(request, 'manage_ad_lanlord.htm', context)


def del_ad(request, pk):
    # function for deleting the advertisements based on their id
    current_ad = Advertisement.objects.get(id=pk)
    current_ad.delete()
    return redirect('manage_ad_ll')


def manage_ad_mod(request):
    return render(request, 'manage_ad_moderator.htm')


def post_ad(request):
    # this function is used for posting an advertisement. This can be done by landlords not students
    if request.method == 'POST':
        desc = request.POST.get('desc')
        address = request.POST.get('address')
        week_rent = request.POST.get('week_rent')
        a_from = request.POST.get('a_from')
        bond = request.POST.get('bond')
        img = request.POST.get('img')
        c_user = request.user
        ad = Advertisement(description=desc, address=address,
                           weekly_rent=week_rent, available_from=a_from,
                           bond_amount=bond, img=img, add_by=c_user)
        ad.save()
        return redirect('advertise')
    return render(request, 'post_ad.htm')
