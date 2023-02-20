from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""<h1>Hello Django Unchained ! Djangooo Djangoooo</h1>
                            <p>Our favourite bands are :<p>
                            <ul>
                                <li>{bands[0].name}</li>
                                <li>{bands[1].name}</li>
                                <li>{bands[2].name}</li>
                            </ul>
                        """)

def about(request):
    return HttpResponse('<h1>About us !</h1><p>We are Django Unchained fans & sell merchandising</p>')

def movies_list(request):
    return HttpResponse("""<h1>List of famous films</h1>
                            <li>Django Unchained</li>
                            <li>Kill Bill Vol I & Vol II</li>
                            <li>Inglourious Basterds</li>
                            <li>The Hateful Eight</li>""")