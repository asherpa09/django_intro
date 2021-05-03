from django.shortcuts import render,  redirect
from time import gmtime, strftime, localtime
import random

# Create your views here.
def index(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
        request.session['goldCounter'] = 0
    return render(request, 'index.html')


def process_money(request):
    if request.method == 'POST':
        
        if request.POST['item'] == 'farm':       
            request.session['goldAmount'] = random.randint(10,20)
            request.session['goldCounter'] += request.session['goldAmount']
            request.session['time'] = strftime("%Y/%m/%d %I:%M %p")
            request.session['activities'].insert(0,"Earned " + str(request.session['goldAmount']) + " from the farm! ("+ str(request.session['time']) + ")")
        
        if request.POST['item'] == 'cave':      
            request.session['goldAmount'] = random.randint(5,10)
            request.session['goldCounter'] += request.session['goldAmount']
            request.session['time'] = strftime("%Y/%m/%d %I:%M %p")
            request.session['activities'].insert(0, "Earned " + str(request.session['goldAmount']) + " from the cave! ("+ str(request.session['time']) + ")")

        if request.POST['item'] == 'house':        
            request.session['goldAmount'] = random.randint(2,5)
            request.session['goldCounter'] += request.session['goldAmount']
            request.session['time'] = strftime("%Y/%m/%d %I:%M %p")
            request.session['activities'].insert(0,"Earned " + str(request.session['goldAmount']) + " from the house! ("+ str(request.session['time']) + ")")

        if request.POST['item'] == 'casino':
            request.session['goldAmount'] = random.randint(-50,50)
            if request.session['goldAmount'] < 0:           
                request.session['goldCounter'] += request.session['goldAmount']
                request.session['time'] = strftime("%Y/%m/%d %I:%M %p")
                request.session['activities'].insert(0,"Entered a casino and lost " + str(request.session['goldAmount']) + " Ouch.. ("+ str(request.session['time']) + ")")
            else:
                request.session['goldCounter'] += request.session['goldAmount']
                request.session['time'] = strftime("%Y/%m/%d %I:%M %p")
                request.session['activities'].insert(0,"Entered a casino and earned " + str(request.session['goldAmount']) + " ("+ str(request.session['time']) + ")")
        
        return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')



