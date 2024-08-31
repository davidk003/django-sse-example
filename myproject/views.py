import datetime
import random
import time
from django.http import StreamingHttpResponse, HttpResponse


name = "David"

def stream(request):
    def event_stream():
        progress = 0
        while True:
            time.sleep(1)
            if progress >= 100:
                yield "data: 100\n\n"
                break
            yield f"data: {progress}\n\n"
            progress += random.randint(1, 25)

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

def my_view(request):  
    if request.method == 'GET':  
        # Retrieve data from the server  
        data = name
        return HttpResponse(data)  