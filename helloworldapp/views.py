from django.shortcuts import render
 
def display_page(request):
    context = {
        "response" : '{"message":"Hello World!"}',
    }
    return render(request, "helloworld.html", context)