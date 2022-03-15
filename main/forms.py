from django import forms
from .models import Notes


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title","content","schedule"]


    def __init__(self,*args,**kwargs):
        super(NoteForm, self).__init__(*args,**kwargs)

        self.fields["title"].widget.attrs.update({"class":"form-control"})
        self.fields["content"].widget.attrs.update({"class":"form-control"})
        self.fields["schedule"].widget.attrs.update({"class":"form-control schedule-input",})

