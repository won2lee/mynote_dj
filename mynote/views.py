from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse

# Create your views here.

from mynote.models import Note, First_Category, Second_Category
from .forms import NoteForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_notes = Note.objects.all().count()
    notes = Note.objects.all()
    # num_instances = BookInstance.objects.all().count()

    # # Available books (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    print(First_Category.objects.all())
    print(str(Note.objects.all()[0].created)[:10])

    #num_categories = sum([cat.objects.all().count() for cat in First_Category.objects.all()])

    # num_genre = Genre.objects.filter(name__icontains='fiction').count() #for test

    # # Number of visits to this view, as counted in the session variable.
    # num_visits = request.session.get('num_visits', 1)
    # request.session['num_visits'] = num_visits + 1

    context = {
        'num_notes': num_notes,
        'num_categories': 3,
        'notes': notes
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# def sidebar(request):
#     notes = Note.objects.all()
#     context = {'notes': notes}
#     return render(request, 'sidebar.html', context=context)

from django.views import generic

class NoteListView(generic.ListView):
    model = Note
    paginate_by = 2


# class NoteDetailView(generic.DetailView):
#     model = Note

def record_view(request, id):
 
    notes = Note.objects.all()

    # print(First_Category.objects.all())
    # print(str(Note.objects.all()[0].created)[:10])
    # print(notes.filter(pk=id))

    context = {
        'notes': notes,
        'note' : notes.filter(pk=id).__getitem__(0)
    }

    ## notes.filter(pk=id) ==> <class 'django.db.models.query.QuerySet'>
    ## notes[id]  ==> db의 아이디디(pk) 가 아니라 리스트의 아이디를 반영 
    ## .filter(pk=id).__getitem__(0) ==> db의 아이디를 유지하면서 queryset 이 아닌 아이템 생성

    # print(f'note ############ : {context["note"]}')
    return render(request, 'mynote/note_detail.html', context=context)

# def sidebar(request):
#     notes = Note.objects.all()
#     context = {'notes': notes}
#     return render(request, 'sidebar.html', context=context)

# notes = Note.objects.all()
# print(f"TYPE :::::: {type(notes)}, {type(notes.filter(pk=2))}, {type(notes[2])}")
# print(notes.filter(pk=4).__getitem__(0))
# print(f'abs_url : {notes[0].get_absolute_url}')
#print(f'content : {str(notes[0].objects)}')

def note_create_view(request):
    notes = Note.objects.all()
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NoteForm()
    context = {
        'form': form,
        'notes' : notes
    }
    return render(request, "mynote/note_create.html", context)
