from django.shortcuts import render,HttpResponse
import pyqrcode
def index(request):
    return render(request, 'index.html')
def qr(request):
    if request.method == 'POST':
        url=request.POST.get('url')
        qr=pyqrcode.create(url)
        qr.svg("static/qr.svg", scale = 8)
        print(qr)
        di={qr:qr}
        return render(request, 'qr.html', {'qr': qr})
