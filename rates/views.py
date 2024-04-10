from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rates.models import Rate
from .forms import RateForm
from django.http import HttpRequest

@login_required
def list_rates(request):
    rates = Rate.objects.filter(user=request.user)
    return render(request, 'list_rates.html', {'rates': rates})

@login_required
def add_rate(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.save()
            return redirect('list_rates')
    else:
        form = RateForm()
    return render(request, 'rate.html', {'form': form})

def update_rate(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id, user=request.user)
    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return redirect('list_rates')
    else:
        form = RateForm(instance=rate)
    return render(request, 'rate.html', {'form': form})  

def delete_rate(request, rate_id):
    rate = get_object_or_404(Rate, id=rate_id, user=request.user)
    if request.method == 'POST':
        rate.delete()
        return redirect('list_rates')
    return render(request, 'rate.html', {'rate': rate})

def rates_list(request):
    rates = Rate.objects.all()
    context = {'rates': rates}
    return render(request, 'rate.html', context)




            



