from django import forms

class LeaveMessage(forms.Form):
    name = forms.CharField(label='name')
    phone = forms.CharField(label='phone')
    email = forms.EmailField()

    def __init__(self,*args,**kwargs):
        super(LeaveMessage, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'הכנס שם פרטי/מלא'
        self.fields['phone'].widget.attrs['placeholder'] = 'הכנס טלפון'
        self.fields['email'].widget.attrs['placeholder'] = 'הכנס אימייל'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
