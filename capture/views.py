import datetime

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone

from .models import Capture

# Create your views here.
def index(request):
    all_capture_list = Capture.objects.filter(status=0, category=0).exclude(due_date__range=["2011-01-31","9011-01-31"]).order_by('-capture_date')
    amount = Capture.objects.filter(status=0, category=0).exclude(due_date__range=["2011-01-31","9011-01-31"]).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'all_capture_list': all_capture_list,
        'amount': amount,
        'bin_amount': bin_amount,
               }
    return render(request, 'capture/index.html', context)

def paper_bin(request):
    paper_bin_list = Capture.objects.filter(category=8).order_by('-capture_date')
    amount = Capture.objects.filter(status=0, category=0).exclude(due_date__range=["2011-01-31","9011-01-31"]).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'paper_bin_list': paper_bin_list,
        'amount': amount,
        'bin_amount': bin_amount,
               }
    return render(request, 'capture/index.html', context)

def detail(request, capture_id):
    all_project_items = Capture.objects.filter(status=0, category=1).order_by('project')
    capture = get_object_or_404(Capture, id=capture_id)
    amount = Capture.objects.filter(status=0, category=0).exclude(due_date__range=["2011-01-31","9011-01-31"]).count()
    bin_amount = Capture.objects.filter(category=8).count()
    if request.method == "POST":
        notes = request.POST['detail']
        if 'date' in request.POST:
            date = request.POST['date']
            if not date:
                date = None
            capture.due_date = date
        if 'anytime' in request.POST:
            capture.due_date = None
            capture.category = 7
        project = request.POST['project']
        if project:
            capture.project = request.POST['project']
            capture.category = 1
        capture.notes = notes
        capture.save()
        return HttpResponseRedirect(reverse('capture:index', args=None))
    context = {'capture': capture,
               'amount': amount,
               'bin_amount': bin_amount,
               'all_project_items': all_project_items}
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
        return redirect(request.META['HTTP_REFERER'])

def undelete(request,capture_id =None):
    object = Capture.objects.get(id=capture_id)
    if object.category == 8:
        object.category = 0
        object.status = 0
        object.save()
        return redirect(request.META['HTTP_REFERER'])
    elif object.status == 1:
        object.status = 0
        object.save()
        return redirect(request.META['HTTP_REFERER'])

def logbook(request):
    all_done_list = Capture.objects.exclude(category=8).filter(status=1).order_by('-capture_date')
    amount = Capture.objects.filter(status=0, category=0).exclude(due_date__range=["2011-01-31","9011-01-31"]).count()
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
    return redirect(request.META['HTTP_REFERER'])

def today(request):
    all_today_list = Capture.objects.exclude(category=8).filter(status=0, due_date__range=["2011-01-31",datetime.date.today()]).order_by('-capture_date')
    amount = Capture.objects.filter(status=0, category=0).exclude(due_date__range=["2011-01-31","9011-01-31"]).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'all_today_list': all_today_list,
        'amount': amount,
        'bin_amount': bin_amount,
               }
    return render(request, 'capture/today.html', context)

def calendar(request):
    all_calendar_items = Capture.objects.exclude(category=8).filter(status=0, due_date__range=[datetime.date.today(), "9011-01-31"]).order_by('due_date')
    amount = Capture.objects.filter(status=0, category=0).exclude(due_date__range=["2011-01-31","9011-01-31"]).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'all_calendar_items': all_calendar_items,
        'amount': amount,
        'bin_amount': bin_amount,
               }
    return render(request, 'capture/calendar.html', context)

def anytime(request):
    all_anytime_list = Capture.objects.filter(status=0, category=7).order_by('-capture_date')
    amount = Capture.objects.filter(status=0, category=0).exclude(due_date__range=["2011-01-31","9011-01-31"]).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'all_anytime_list': all_anytime_list,
        'amount': amount,
        'bin_amount': bin_amount,
               }
    return render(request, 'capture/anytime.html', context)

def projects(request):
    all_project_items = Capture.objects.filter(status=0, category=1).order_by('project')
    amount = Capture.objects.filter(status=0, category=0).exclude(due_date__range=["2011-01-31","9011-01-31"]).count()
    bin_amount = Capture.objects.filter(category=8).count()
    context = {
        'all_project_items': all_project_items,
        'amount': amount,
        'bin_amount': bin_amount,
               }
    return render(request, 'capture/projects.html', context)