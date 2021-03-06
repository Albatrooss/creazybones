from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from ..models import Crazybone, Profile, Cb_Profile
from django.contrib.auth import login

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      new_profile = Profile.objects.create(user=user)
      for z in range(10):
        rand_cb = Crazybone.objects.order_by('?')[0]
        if(rand_cb in new_profile.cb.all()):
          cb2P=Cb_Profile.objects.get(cb=rand_cb, profile=new_profile)
          cb2P.qty+=1
          cb2P.save()
        else:
          new_profile.cb.add(rand_cb)
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)