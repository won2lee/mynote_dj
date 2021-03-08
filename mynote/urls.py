from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.NoteListView.as_view(), name='notes'),
	path('note/<int:id>/', views.record_view, name='note-detail'),
	path('create/', views.note_create_view, name='note-create'),
]