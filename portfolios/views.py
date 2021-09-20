from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def profile(request):
  if request.method == 'POST':
    userform = UserForm(request.POST, instance=request.user)
    profileform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    if userform.is_valid and profileform.is_valid():
      userform.save()
      profileform.save()
      messages.success(request, 'Profile updated successfully')
    return redirect('profile')

  userform = UserForm()
  profileform = ProfileForm()
  curr_profile = Profile.objects.get(username = request.user)
  curr_projects = Projects.user_projects(request.user)
  params = {'curr_user': curr_profile, 
            'curr_project': curr_projects,
            'userform':userform,
            'profileform':profileform,
            }
  return render(request, 'profile/index.html', params)