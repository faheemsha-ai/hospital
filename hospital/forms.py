from django import forms
from . models import Booking
from django.forms import TextInput, EmailInput ,Select,DateInput,TimeInput

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["name","email","phone","doc_name","date","time","message"]
        widgets={
            'name':TextInput(
                attrs={
                    "name":"name",
                    "type":"text",
                    "placeholder":"Name"
                }
            ),
            'email':EmailInput(
                attrs={
                    "name":"email",
                     "type":"email",
                     "placeholder":"Email"
                }
            ),
            'phone' :TextInput(
                attrs={
                    "name":"phone" ,
                    "type":"text",
                    "placeholder":"Phone"
                }
            ),
           'doc_name' :Select(
               attrs={
                   "name":"doctors",
                   "class":"form-select"
               }
            ),
            'date' : DateInput(
                attrs={
                    "type":"date",
                    "placeholder":"Date",
                    "id":"datepicker"
                }
            ),
            'time' : TimeInput(
                attrs={
                    "type":"time" ,
                    "placeholder":"time",
                    "id":"time",
                }
            
            )
        }