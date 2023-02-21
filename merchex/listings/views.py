from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Title

def hello_band(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/hello_band.html',
                  {'first_band':bands[0],
                  'second_band':bands[1],
                  'third_band':bands[2]
                  }
                  )

def hello_title(request):
    titles = Title.Objects.all()

    return render(request, 'listings/hello_title.html')

def about(request):
    return HttpResponse('<h1>About us !</h1><p>We are Django Unchained fans & sell merchandising</p>')

def movies_list(request):
    return HttpResponse("""<h1>List of famous films</h1>
                            <li>Django Unchained</li>
                            <li>Kill Bill Vol I & Vol II</li>
                            <li>Inglourious Basterds</li>
                            <li>The Hateful Eight</li>""")