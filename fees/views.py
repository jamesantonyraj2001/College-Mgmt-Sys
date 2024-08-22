from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm  # Create a form for adding payments
from django.contrib import messages
def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'fees/payment_list.html', {'payments': payments})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Paid Successfully")
            return redirect('add_payment')
    else:
        form = PaymentForm()
        
    return render(request, 'fees/add_payment.html', {'form': form})
