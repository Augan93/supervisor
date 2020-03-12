from django.shortcuts import render
import psutil
from django.contrib.auth.decorators import login_required


@login_required
def load_average(request):
    load1, load5, load15 = psutil.getloadavg()

    context = {
        'load1': load1,
        'load5': load5,
        'load15': load15,
    }

    return render(
        request,
        'supervisor/load_average.html',
        context=context
    )


@login_required
def ram(request):
    total, available, used_percent, used, free = psutil.virtual_memory()

    context = {
        'total': total,
        'available': available,
        'used_percent': used_percent,
        'used': used,
        'free': free
    }

    return render(
        request,
        'supervisor/ram.html',
        context=context
    )


