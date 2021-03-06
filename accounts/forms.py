"""
    Forms.py:
    This will handle user authenticationagainst our DB
"""
from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile


# This class will be responsible for handling the registration of a new user
class UserRegisterForm(forms.ModelForm):
    """
    password1: The users password to enter initially
    password2: The users password re-entered
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        """
        model: The user model
        fields: The fields we wish to provide the user with for registration/sign-up
        """
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        """
        clean_password: Here we check if the second password matches the first password
        entered, if they do not match we return a validation error message to the user
        """
        clean_pwd_data = self.cleaned_data
        if clean_pwd_data['password1'] != clean_pwd_data['password2']:
            raise forms.ValidationError('Sorry, the passwords do not match!')
        return clean_pwd_data['password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields["first_name"].required = False
        self.fields["last_name"].required = False
        self.fields["email"].required = True
        self.fields["password1"].required = True
        self.fields["password2"].required = True


# This class will be responsible for handling the user login
class UserLoginForm(forms.Form):
    """
    username: The users name input field
    password: The users password input field
    We use the widget here to display the passwords HTML input, it includes a
    type="password" attr
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EditUserForm(forms.ModelForm):
    """
    EditUserForm(forms.ModelForm):
        Handle the users details so they can edit them
    """
    class Meta:
        """
        model: the User model
        fields: allow users to edit first and last names as well as email address
        """
        model = User
        fields = ('first_name', 'last_name', 'email')


class EditProfileForm(forms.ModelForm):
    """
    EditProfileForm(forms.ModelForm):
        We want to allow the user to edit their profile
        so we provide a form
    """
    class Meta:
        """
        model: UserProfile model
        fields: allows the user to edit their dob and profile image
        """
        model = Profile
        fields = (
            'personal_site_url',
            'date_of_birth',
            'about_me',
            'fave_game',
            'facebook_url',
            'github_url',
            'twitter_url',
            'google_plus_url',
            'youtube_url',
            'profile_image',
            )
