from django import forms
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, UserChangeForm, UserCreationForm
from blog.models import Blog, ContactUs
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class':'field'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re enter your Password','class':'field'}))
    class Meta(UserCreationForm.Meta):
        # model = User
        fields = ('username','first_name','last_name','email')

        widgets = {'username': forms.TextInput(attrs={'placeholder':'Enter your Username','class':'field'}),
                   'first_name': forms.TextInput(attrs={'placeholder':'Enter your First Name','class':'field','required':True}),
                   'last_name': forms.TextInput(attrs={'placeholder':'Enter your Last Name','class':'field','required':True}),
                   'email': forms.EmailInput(attrs={'placeholder':'Enter your Email ID','class':'field','required':True})}
        
class LoggedInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your username','class':'field'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password','class':'field'}))

class ChangePassForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your new password','class':'field'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re enter your new password','class':'field'}))
    otp = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Enter the Otp','class':'field'}))

class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','content')

        widgets = {"title":forms.TextInput(attrs={'placeholder':'Enter your blog title','class':'field blogged-title',"required":True}),
                   'content':TinyMCE(attrs={'placeholder':'Enter your blog Content','class':'field blogged-content'})
                   }
    
    def clean(self):
        cleaned_data = super().clean()
        title = self.cleaned_data['title']
        if not title or len(title.strip())<20:
            raise ValidationError('Blog title contains atleast 20 words')
        
        content = self.cleaned_data['content']
        if not content or 0<len(content.strip())<100:
            raise ValidationError('Blog contains atleast 100 words')
        
class UserProfileForm(UserChangeForm):
    password = None
    date_joined = forms.DateTimeField(required=False,widget=forms.DateTimeInput(attrs={'placeholder':'Enter your Date Joined','class':'field nojs'}))
    last_login = forms.DateTimeField(required=False,widget=forms.DateTimeInput(attrs={'placeholder':'Enter your last login','class':'field nojs'}))
    username = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'Enter your username','class':'field nojs'}))

    class Meta(UserChangeForm.Meta):
        fields = ('username','first_name','last_name','email','date_joined','last_login')

        widgets = {'first_name':forms.TextInput(attrs={'placeholder':'Enter your first name','class':'field forjs'}),
                   'last_name':forms.TextInput(attrs={'placeholder':'Enter your last name','class':'field forjs'}),
                   'email':forms.EmailInput(attrs={'placeholder':'Enter your email id','class':'field forjs'})
                   }
        
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('title','description')

        widgets = {"title":forms.TextInput(attrs={'placeholder':'Enter your query title','class':'field blogged-title',"required":True}),
                'description':forms.Textarea(attrs={'placeholder':'Describe your query','class':'field blogged-content',"required":True})}
    

    def clean(self):
        cleaned_data = super().clean()
        title = self.cleaned_data['title']
        if not title or len(title.strip())<20:
            raise ValidationError('Query title contains atleast 20 words')
        
        content = self.cleaned_data['description']
        if not content or len(content.strip())<20:
            raise ValidationError('Query Description contains atleast 20 words')