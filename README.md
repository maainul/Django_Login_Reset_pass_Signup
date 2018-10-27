# Django_Login_Reset_pass_Signup

### Django Login part-1(Only login and logout)

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
```
#######   registration/login.html   ############
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

###########   logged_out.html   ###########


{% extends 'base.html' %}

{% block title %}See you!{% endblock %}

{% block content %}
  <h2>Logged out</h2>
  <p>You have been successfully logged out.</p>
  <p><a href="{% url 'login' %}">Log in</a> again.</p>
{% endblock %}



#########     base.html ##########

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


####### home.html ########


{% extends 'base.html' %}

{% block title %}Login{% endblock %}

{% block content %}
  <h2>Home</h2>
{% endblock %}


####
