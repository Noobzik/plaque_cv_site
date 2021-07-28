# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Vehicule
import cv2
import threading
import socket
import struct
import numpy as np
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
    return render(request, 'vebcam.html')


#capture video
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture('udp://127.0.0.1:50500', cv2.CAP_FFMPEG)
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
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def feed(request):
    try:
        return StreamingHttpResponse(feed_gen(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'vebcam.html')


def feed_gen():
    MAX_DGRAM = 2 ** 16
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = '0.0.0.0'
    port = 55055
    s.bind((addr, port))
    dat = b''
    while True:
        seg, addr = s.recvfrom(MAX_DGRAM)
        if struct.unpack("B", seg[0:1])[0] > 1:
            dat += seg[1:]
            print("No Data received")
        else:
            dat += seg[1:]
            feed = cv2.imdecode(np.frombuffer(dat, dtype=np.uint8), 1)
            _, img = cv2.imencode('.jpg', feed)
            img1 = img.tobytes()
            cv2.waitKey(1)
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img1 + b'\r\n\r\n')
            dat = b''
            #    frame = camera.get_frame()
    s.close()
