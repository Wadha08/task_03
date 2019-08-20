from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list" :[{ "restaurant_name":"Ashaz", "Food_type":"indian"},
    					   { "restaurant_name":"Fridays", "Food_type":"American"},
    					   { "restaurant_name":"Tacobeill", "Food_type":"Mixecoooooo"},

    ] }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { "my_object": {"restaurant_name":"freejsuwaileh", "Food_type":"Kuwaiti"}

    }
    return render(request, 'detail.html', context)
