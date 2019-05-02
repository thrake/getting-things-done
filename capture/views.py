from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Capture

# Create your views here.
def index(request):
    all_capture_list = Capture.objects.order_by('-capture_date')
    amount = Capture.objects.filter(status=0).count()
    context = {'all_capture_list': all_capture_list,
               'amount': amount,}
    return render(request, 'capture/index.html', context)

def detail(request, capture_id):
    capture = get_object_or_404(Capture, id=capture_id)
    print(capture)
    print(capture.notes)
    if request.method == "POST":
        notes = request.POST['detail']
        print(notes)
        capture.notes = notes
        capture.save()
    context = {'capture': capture}
    return render(request, 'capture/detail.html', context)    

def all(request):
    all_capture_list = Capture.objects.order_by('-capture_date')
    output = ', '.join([c.capture_text for c in all_capture_list])
    return HttpResponse(output)

def capture(request):
    print("capture started")
    textinput = request.POST['capture']
    c = Capture(capture_text=textinput, capture_date=timezone.now())
    c.save()
    print(c, "saved!")
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('capture:index', args=None))