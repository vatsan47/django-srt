from django.http import HttpResponse
from django.shortcuts import render

from .forms import UploadFileForm
from django.views.decorators.csrf import ensure_csrf_cookie
from .cmd import *
from .s3 import *
from .sub import *
from .db import *
from .a import look
import re

@ensure_csrf_cookie
def upload_display_video(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            #print(file.name)
            handle_uploaded_file(file)
            return render(request, "upload-display-video.html", {'filename': file.name})
    else:
        form = UploadFileForm()
    return render(request, 'upload-display-video.html', {'form': form})

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    name = re.sub('.mp4', '', f.name)
    run_parallel(srt(f.name), upload_to_aws(f.name, 'mybucket106'), create_table(name))
    add_subtitles(name)
    
def search(request):
    if request.method == 'POST':
        key = request.POST.get('textfield')
        res = look("video", key)
    return render(request, 'search-res.html', {'res': res})

def run_parallel(*functions):
    '''
    Run functions in parallel
    '''
    from multiprocessing import Process
    processes = []
    for function in functions:
        proc = Process(target=function)
        proc.start()
        processes.append(proc)
    for proc in processes:
        proc.join()