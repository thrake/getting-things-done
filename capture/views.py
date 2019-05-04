from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Capture

# Create your views here.
def index(request):
    all_capture_list = Capture.objects.filter(status=0, category=0).order_by('-capture_date')
    amount = Capture.objects.filter(status=0, category=0).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'all_capture_list': all_capture_list,
        'amount': amount,
        'bin_amount': bin_amount,
               }
    return render(request, 'capture/index.html', context)

def paper_bin(request):
    paper_bin_list = Capture.objects.filter(category=8).order_by('-capture_date')
    amount = Capture.objects.filter(status=0, category=0).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'paper_bin_list': paper_bin_list,
        'amount': amount,
        'bin_amount': bin_amount,
               }
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

# all is non-functional atm
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

def delete(request,capture_id =None):
    object = Capture.objects.get(id=capture_id)
    if object.category == 8:
        object.delete()
        return HttpResponseRedirect(reverse('capture:paper_bin', args=None))
    else:
        object.category = 8
        object.save()
        return HttpResponseRedirect(reverse('capture:index', args=None))