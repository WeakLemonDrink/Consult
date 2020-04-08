from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            user.profile.role = form.cleaned_data['role']
            #user.profile.organisation = form.cleaned_data.get('organisation') # figure out whether to select from drop down or free type field
            user.profile.house_name_no = form.cleaned_data['house_name_no']
            user.profile.street = form.cleaned_data['street']
            user.profile.town = form.cleaned_data['town']
            user.profile.county = form.cleaned_data.get('county')
            user.profile.postcode = form.cleaned_data.get('postcode')
            user.profile.tel = form.cleaned_data.get('tel')
            #user.profile.gdpr_consent = form.cleaned_data.get('gdpr_consent') #change field type to True / False
            
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})