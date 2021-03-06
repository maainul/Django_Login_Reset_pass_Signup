# Django_Login_Reset_pass_Signup

### Part-1(Only login and logout)

## 1. Create Project
```
    mkdir dev && cd dev
    mkdir login && cd login
    virtualenv -p python3 .
    source bin/activate
    pip install django==2.0.7
    mkdir src && cd src
    django-admin startproject login .
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
```
## Edit Settings:
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],#new for templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only


LOGIN_REDIRECT_URL = 'home'
```
## Create Template
```
    cd dev/login
    source bin/activate
    cd src
    mkdir templates
    touch templates/base.html
    touch templates/home.html
    mkdir templates/registration
    touch templates/registration/login.html
    touch templates/registration/logged_out.html

```
## Edit Urls.py
```

    from django.contrib import admin
    from django.urls import path
    from django.contrib.auth import views as auth_views #new
    from django.views.generic.base import TemplateView #new

    urlpatterns = [
    	path('admin/', admin.site.urls),

    	# home page or redirect page
    	path('',TemplateView.as_view(template_name='home.html'),name='home'),
    	#login page url
     	path('login/', auth_views.login, name='login'),# new
      path('logout/', auth_views.logout,{'next_page':'/'}, name='logout'),#new
    ]
```
## Add code to the templates

## registration/login.html
```
    {% extends 'base.html' %}

    {% block title %}Login{% endblock %}

    {% block content %}
      <h2>Login</h2>
      <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
      </form>
    {% endblock %}
```
## logged_out.html

```
{% extends 'base.html' %}

{% block title %}See you!{% endblock %}

{% block content %}
  <h2>Logged out</h2>
  <p>You have been successfully logged out.</p>
  <p><a href="{% url 'login' %}">Log in</a> again.</p>
{% endblock %}
```


##   base.html
```
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{% block title %}Django Simple Login{% endblock %}</title>
</head>
<body>
  <header>
    <h1>Django Simple Login</h1>
    {% if user.is_authenticated %}
      Hi {{ user.username }}!
      <a href="{% url 'logout' %}">logout</a>
    {% else %}
      <a href="{% url 'login' %}">login</a>
    {% endif %}
  </header>
  <hr>
  <main>
    {% block content %}
    {% endblock %}
  </main>
  <hr>
  <footer>
    <a href="http://simpleisbetterthancomplex.com">simpleisbetterthancomplex.com</a>
  </footer>
</body>
</html>
```

## home.html

```
{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
  <h2>Home</h2>
{% endblock %}
```

### Part-2 (Reset Password)
## Add html file to the templates

```
    touch templates/registration/password_reset_form.html
    touch templates/registration/password_reset_email.html
    touch templates/registration/password_reset_done.html
    touch templates/registration/password_reset_confirm.html
    touch templates/registration/password_reset_complete.html
    touch templates/registration/password_reset_subject.txt

```
## Edit urls.py

```
  from django.contrib import admin
  from django.urls import path
  from django.contrib.auth import views as auth_views #new
  from django.views.generic.base import TemplateView #new

  urlpatterns = [
  	path('admin/', admin.site.urls),
  	path('',TemplateView.as_view(template_name='home.html'),name='home'),
   	path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout,{'next_page':'/'}, name='logout'),
  	path('password_reset/', auth_views.password_reset, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
  ]     
````

## Add code to the html pages


## registration/password_reset_form.html
```
    {% extends 'base.html' %}

    {% block content %}
      <h3>Forgot password</h3>
      <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
      </form>
    {% endblock %}
```

## registration/password_reset_email.html

```
    {% autoescape off %}
    To initiate the password reset process for your {{ user.get_username }} TestSite Account,
    click the link below:

    {{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

    If clicking the link above doesn't work, please copy and paste the URL in a new browser
    window instead.

    Sincerely,
    The TestSite Team
    {% endautoescape %}
```

## registration/password_reset_done.html

```
    {% extends 'base.html' %}

    {% block content %}
      <p>
        We've emailed you instructions for setting your password, if an account exists with the email you entered.
        You should receive them shortly.
      </p>
      <p>
        If you don't receive an email, please make sure you've entered the address you registered with,
        and check your spam folder.
      </p>
    {% endblock %}
```

## registration/password_reset_confirm.html

```
{% extends 'base.html' %}

{% block content %}
  {% if validlink %}
    <h3>Change password</h3>
    <form method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit">Change password</button>
    </form>
  {% else %}
    <p>
      The password reset link was invalid, possibly because it has already been used.
      Please request a new password reset.
    </p>
  {% endif %}
{% endblock %}
```

## registration/password_reset_complete.html

```
{% extends 'base.html' %}

{% block content %}
  <p>
    Your password has been set. You may go ahead and <a href="{% url 'signin' %}">sign in</a> now.
  </p>
{% endblock %}
```

## registration/password_reset_subject.txt

```
TestSite password reset

```

## Settings.py
```

    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'testsite_app'
    EMAIL_HOST_PASSWORD = 'mys3cr3tp4ssw0rd'
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'TestSite Team <noreply@example.com>'
```
### Part-3(SignUp_Basic)
```
	create a app name account
	django-admin startapp account
```
## Add code to the Urls.py
```

	from django.contrib import admin
	from django.urls import path
	from django.contrib.auth import views as auth_views #new
	from django.views.generic.base import TemplateView #new
	from django.conf.urls import include
	from account import views as core_views

	urlpatterns = [
		path('admin/', admin.site.urls),
		path('',TemplateView.as_view(template_name='home.html'),name='home'),
	 	path('login/', auth_views.login, name='login'),
	    	path('logout/', auth_views.logout,{'next_page':'/'}, name='logout'),
		path('password_reset/', auth_views.password_reset, name='password_reset'),
	    	path('password_reset/done/', auth_views.password_reset_done, name='password_reset_done'),
		path('reset/<uidb64>/<token>/',auth_views.password_reset_confirm, name='password_reset_confirm'),
	    	path('reset/done/', auth_views.password_reset_complete, name='password_reset_complete'),
		path('signup/', core_views.signup, name='signup'),
	]

```

## account/views.py
```
	from django.contrib.auth import login, authenticate
	from django.contrib.auth.forms import UserCreationForm
	from django.shortcuts import render, redirect

	def signup(request):
	    if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
		    form.save()
		    username = form.cleaned_data.get('username')
		    raw_password = form.cleaned_data.get('password1')
		    user = authenticate(username=username, password=raw_password)
		    login(request, user)
		    return redirect('home')
	    else:
		form = UserCreationForm()
	    return render(request, 'signup.html', {'form': form})
```
## templates/signup.html
```
	create a file name signup.html

	{% extends 'base.html' %}

	{% block content %}
	  <h2>Sign up</h2>
	  <form method="post">
	    {% csrf_token %}
	    {{ form.as_p }}
	    <button type="submit">Sign up</button>
	  </form>
	{% endblock %}
```
OR
```
	{% extends 'base.html' %}

	{% block content %}
	  <h2>Sign up</h2>
	  <form method="post">
	    {% csrf_token %}
	    {% for field in form %}
	      <p>
		{{ field.label_tag }}<br>
		{{ field }}
		{% if field.help_text %}
		  <small style="color: grey">{{ field.help_text }}</small>
		{% endif %}
		{% for error in field.errors %}
		  <p style="color: red">{{ error }}</p>
		{% endfor %}
	      </p>
	    {% endfor %}
	    <button type="submit">Sign up</button>
	  </form>
	{% endblock %}
```

### Part-4(SignUp With Extra Fields)

## Add file name forms.py in the account folder
```

	from django import forms
	from django.contrib.auth.forms import UserCreationForm
	from django.contrib.auth.models import User


	class SignUpForm(UserCreationForm):
	    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	    last_name  = forms.CharField(max_length=30, required=False, help_text='Optional.')
	    email      = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	    class Meta:
		model  = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
```
## Edit Views.py
```
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from account.forms import SignUpForm

@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
```

### Part-5(Sign Up With Profile Model)
## models.py
```
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user 	   = models.OneToOneField(User, on_delete=models.CASCADE)
    bio        = models.TextField(max_length=500, blank=True)
    location   = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
```
## forms.py
```
	from django import forms
	from django.contrib.auth.forms import UserCreationForm
	from django.contrib.auth.models import User


	class SignUpForm(UserCreationForm):
	    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	    last_name  = forms.CharField(max_length=30, required=False, help_text='Optional.')
	    email      = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

	    class Meta:
		model  = User
		fields = ('username', 'first_name', 'last_name', 'email','birth_date', 'password1', 'password2', )

```
## views.py
```

	from django.contrib.auth import login, authenticate
	from django.shortcuts import render, redirect
	from account.forms import SignUpForm

	def signup(request):
	    if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
		    user = form.save()
		    user.refresh_from_db()  # load the profile instance created by the signal
		    user.profile.birth_date = form.cleaned_data.get('birth_date')
		    user.save()
		    raw_password = form.cleaned_data.get('password1')
		    user = authenticate(username=user.username, password=raw_password)
		    login(request, user)
		    return redirect('home')
	    else:
		form = SignUpForm()
	    return render(request, 'signup.html', {'form': form})

```











