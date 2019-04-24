from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404

from .models import Capture

# Create your views here.
def index(request):
    all_capture_list = Capture.objects.order_by('-capture_date')[:5]
    context = {'all_capture_list': all_capture_list}
    return render(request, 'capture/index.html', context)
    
    return HttpResponse("Hello, world. You're at the capture index.")

def detail(request, capture_id):
        text = get_object_or_404(Capture, id=capture_id)
        return render(request, 'capture/detail.html', {'text': text})    

def all(request):
    all_capture_list = Capture.objects.order_by('-capture_date')[:5]
    output = ', '.join([c.capture_text for c in all_capture_list])
    return HttpResponse(output)