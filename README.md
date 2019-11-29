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