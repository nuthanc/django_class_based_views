# django_class_based_views

* After initial setup, do python manage.py migrate
* python manage.py runserver

### Class based views
* Changes made in views.py file 
* Also in urls.py file to show that class as a view

* Most frequent way of using ClassBasedViews is by inheriting TemplateView

* injectme in views.py is the context dictionary

* Need to register models in admin.py and then migrate using python manage.py migrate, python manage.py makemigrations basic_app, python manage.py migrate

* Create superuser using python manage.py createsuperuser

### New template paradigm
* school_list in school_detail.html is coming from views.py SchoolListView. 
* The ListView is creating from the model School. 
* The context dictionary created is of the form modelname_list
* Custom context dictionary in ListView is done by giving the attribute context_object_name your value.
* For e.g., context_object_name = 'schools'
* Advantage of using this new templates, no need to call Objects.get for models
* Update urls.py file of basic_app with the SchoolListView

### Where does .students come from in school_detail.html's for loop
* It is the related_name in Student model in models.py 

* re_path is used for regular expression patterns
* Video 161 time -2:40 explaining that bizarre pk in urls.py file
* It's basically taking the school_id as primary key and passing it to urls.py file to render that school's view

### CreateView
* Deliberately leaving out the fields attribute to see in Django debug mode in the website
* Also template is not given at first
* CreateView creates a default html template and for School model within SchoolCreateView, it's creating school_form.html
* form.instance.pk conditional in school_form is checking if an instance of the primary key exists or not

### ImproperlyConfigured at /basic_app/create/
* Working on this error
* No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
* import reverse to redirect to what pk of school to be created with

### UpdateView
* Create class in views.py
* Update urls.py
* Update the template file that relates to school detail

### DeleteView
* Create class in views.py
* Slightly different from what we have done so far for create and update
* Update urls.py
* Create the template file for delete