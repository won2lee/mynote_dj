from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.index, name='index'),
	path('note/<int:id>/', views.record_view, name='note-detail'),
	path('create/', views.NoteCreateView.as_view(), name='note-create'),
	path('update/<int:pk>/', views.NoteUpdateView.as_view(), name='note-update'),
	path('delete/<int:pk>/', views.NoteDeleteView.as_view(), name='note-delete'),
]
#	path('create/', views.note_create_view, name='note-create'),
#   path('notes/', views.NoteListView.as_view(), name='notes'),