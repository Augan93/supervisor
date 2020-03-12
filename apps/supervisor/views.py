from django.shortcuts import render
import os
import sys
import psutil
from django.contrib.auth.decorators import login_required


def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


@login_required
def load_average(request):
    # if get_platform() == 'Windows':
    #     load1, load5, load15 = psutil.getloadavg()
    # elif get_platform() == 'Linux':

    # load1, load5, load15 = os.getloadavg()
    load1, load5, load15 = 0.35, 0.25, 0.5

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


