# views.py

from django.contrib.auth.decorators import login_required
from .models import Message

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse


@login_required
def send_message(request, receiver_id):
    context = {}

    if request.method == 'POST':
        content = request.POST['content']
        receiver = User.objects.get(pk=receiver_id)
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        
        receiver_id = 123  # Replace this with the actual receiver_id
        context = {'receiver_id': receiver_id}
    return render(request, 'communication/send_message.html', context)






@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'communication/inbox.html', {'messages': messages})



def show_profile(request, user_id):
    # Your view logic here

    # Use reverse to generate the URL for 'user_profile' view
    profile_url = reverse('user_profile', kwargs={'user_id': user_id})

    # Redirect to the user's profile page
    return HttpResponseRedirect(profile_url)
