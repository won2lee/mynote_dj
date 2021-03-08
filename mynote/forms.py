from django import forms


from .models import Note, First_Category, Second_Category


class NoteForm(forms.ModelForm):
    first_cat   = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "First_category of your note"}))
    second_cat  = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={"placeholder": "Second_category of your note"}))
    memo        = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Your memo",
                                    "class": "new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "rows": 10,
                                    'cols': 40
                                }
                            )
                        )
    
    class Meta:
        model = Note
        fields = [
            'first_cat',
            'second_cat',
            'memo'
        ]
