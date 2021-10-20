from django.shortcuts import render,HttpResponse,redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .forms import LeaveMessage

from django.contrib.sites.shortcuts import get_current_site


def index(request):
    images = []
    for i in range(1,20):
        loc = f"img/areaphotos/{i}.jpg"
        images.append(loc)

    if request.method == 'POST':
        form = LeaveMessage(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']

            mail_subject = 'New client information'
            message = render_to_string('leavemessagetoemail.html',{
                'name':name,
                'phone':phone,
                'email':email,
            })

            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
            print(form)
            return redirect('index')
    else:
        form = LeaveMessage()

    context = {'images': images, 'form': form,}
    return render(request,'index.html',context)