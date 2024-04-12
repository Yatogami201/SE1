from django.shortcuts import render,redirect
import uuid

from .models import UniqueUrl


def generate_url():
    unique_url=uuid.uuid4().hex[:12]
    while UniqueUrl.objects.filter(url=unique_url).exists():
        unique_url=uuid.uuid4().hex[:12]
    return unique_url

def create_url(request):
    if request.method=='POST':
        unique_url=generate_url()
        UniqueUrl.objects.create(url=unique_url)
        return redirect('unique_url_detail', unique_url=unique_url)
    return render(request, 'url_generator.html')

def unique_url_detail(request, unique_url):
    unique_url_object = UniqueUrl.objects.get(url=unique_url)
    return redirect(unique_url_object)

