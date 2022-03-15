from django.shortcuts import get_object_or_404, render
from .forms import NoteForm
from .models import Notes
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
import  time
from django.core.mail import send_mail
from django.conf import Settings, settings
from django.utils import timezone
from datetime import date, datetime
from django.urls import reverse
# Create your views here.
import requests
from .filters import NotesFilter





def home(request):

    noteform = NoteForm(request.POST or None)

    if noteform.is_valid():
        noteform.save()
        noteform = NoteForm()
        return HttpResponseRedirect("/")      

    notes = Notes.objects.all().order_by("-created")
    
    filterForm = NotesFilter(request.GET,notes)


    today = timezone.now().strftime("%d/%m/%y %H:%M")
   
    return render(request,"main/home.html",{"form":noteform,"notes":notes,"today":today,"filter":filterForm})


def deleteNote(request,pk):
    data = request.POST.get("card_id")
    note = get_object_or_404(Notes,id=int(data))
    note.delete()
    return JsonResponse("deleted",safe=False)



def updateNote(request,pk):
    note = get_object_or_404(Notes,pk=pk)
    form = NoteForm(instance=note)
    notes = Notes.objects.all().order_by("-created")
    today = timezone.now().strftime("%d/%m/%y %H:%M")

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note.title = form.cleaned_data["title"]
            note.content = form.cleaned_data["content"]
            note.schedule = form.cleaned_data["schedule"]
            note.save()
            return HttpResponseRedirect(reverse("home"))
    return render(request,"main/update.html",{"form":form,"notes":notes,"today":today})

def sendMail(request):
    if request.method == "POST":
        id = request.POST.get("data_id")
        note = get_object_or_404(Notes,id=id)
        #Send to Pushover with max priority(2)(repeating message every 30 seconds for 300 seconds)
        response = requests.post(
            "https://api.pushover.net/1/messages.json",
            data={
                "token": settings.TOKEN,
                "user":settings.USER,
                "title":note.title,
                "message":note.content,
                "priority":"2",
                "expire":"300",
                "retry":"30"
            
            },
        )

       
    return HttpResponse("main sent!")
