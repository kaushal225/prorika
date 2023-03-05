from django.urls import include,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('',views.index,name='home'),
    path('create',views.create_problem,name='create-problem'),
    path('problem/<id>',views.problem_detail,name='problem'),
    path('problem-delete/<id>',views.problem_delete,name='delete-problem'),
    path('problem-update/<id>',views.problem_update,name='update-problem'),
    path('searchproblems',csrf_exempt(views.search_problems),name='search_problems')
]

