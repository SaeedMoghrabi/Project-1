from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),

   
    # entryy view
    path('wiki/<str:title>/', views.entry, name='entry'),

    #  search requests
    path("search/", views.search, name="search"),

    #  to create new page
    path("new/", views.new_page, name="new_page"),

    #   for entryy editss
    path("edit/", views.edit, name="edit"),

    #  for edit saves
    path("save_edit", views.save_edit, name="save_edit"),

    #  for a random page "rand vieww"
    path("rand/", views.rand, name="rand")
]
