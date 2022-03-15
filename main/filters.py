from django.forms import TextInput
import django_filters
from .models import Notes

class NotesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
            lookup_expr="icontains",
            widget=TextInput(
                    attrs={"placeholder":"Search Notes"}
                )
            )

    class Meta:
        model = Notes
        fields = ["title"]



