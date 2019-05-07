import datetime

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
    if request.method == "POST":
        notes = request.POST['detail']
        date = request.POST['date']
        capture.due_date = date
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

def logbook(request):
    all_done_list = Capture.objects.filter(status=1).order_by('-capture_date')
    amount = Capture.objects.filter(status=0, category=0).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'all_done_list': all_done_list,
        'amount': amount,
        'bin_amount': bin_amount,
               }
    return render(request, 'capture/logbook.html', context)

def log_item(request,capture_id =None):
    object = Capture.objects.get(id=capture_id)
    object.status = 1
    object.save()
    return HttpResponseRedirect(reverse('capture:index', args=None))

def today(request):
    all_today_list = Capture.objects.exclude(category=8).filter(status=0, due_date__startswith=datetime.date.today()).order_by('-capture_date')
    amount = Capture.objects.filter(status=0, category=0).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'all_today_list': all_today_list,
        'amount': amount,
        'bin_amount': bin_amount,
               }
    return render(request, 'capture/today.html', context)

def calendar(request):
    all_calendar_items = Capture.objects.exclude(category=8).filter(status=0, due_date__range=[datetime.date.today(), "9011-01-31"]).order_by('due_date')
    amount = Capture.objects.filter(status=0, category=0).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'all_calendar_items': all_calendar_items,
        'amount': amount,
        'bin_amount': bin_amount,
               }
    return render(request, 'capture/calendar.html', context)