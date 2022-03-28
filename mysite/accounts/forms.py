from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class UserCreateForm(UserCreationForm):
    template_name='accounts/signup.html'

    class Meta:
        fields =('username','email','password1','password2')

        def __init__(self,request,*args,**kwargs):
            self.fields['username'].label = 'Username'
            self.fields['email'].label ='Email Address'