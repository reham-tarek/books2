
from django import forms

from books.models import books_list

class booksform(forms.ModelForm):
    class Meta:
        model = books_list
        fields = [ "name","publishdate","author","price","Appropriate","profile_pic"]




        
        
        #  [ "name","publishdate","author","price","age","Appropriate"]
