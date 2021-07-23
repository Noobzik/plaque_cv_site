# Create your views here.
from __future__ import division
import numpy as np
import socket
import struct
from django.shortcuts import render
from .models import Vehicule
import cv2
import threading
from django.views.decorators import gzip
from django.http import StreamingHttpResponse


def vehicules(request):
    vehicules = Vehicule.objects.all()
    return render(request=request, template_name="main/liste.html", context={'vehicules': vehicules})

@gzip.gzip_page
def webcam(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'webcam.html')

#capture video
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    frame = camera.get_frame()
    yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
