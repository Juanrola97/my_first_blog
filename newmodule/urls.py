from django.urls import path
from newmodule.views import AuthorCreate, AuthorDelete, AuthorUpdate

urlpatterns = [
    # ...
    path('author/add/', AuthorCreate.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
]