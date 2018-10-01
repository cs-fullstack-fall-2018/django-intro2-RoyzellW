from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def sayHello(request, name):
    print("Hello ", name)
    return HttpResponse("Process competed! Check Console.Log")

def times(request, number):
    x = number*2
    return HttpResponse("The product times 2 is: ", x)

def iterate(request, number):
    counter = 0
    for x in range(o, number):
        print(x)
        counter += x

        return HttpResponse("The sum is: ", counter)