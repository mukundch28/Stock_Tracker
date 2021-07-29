from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponse
from .models import Stock_Name
from nsetools import Nse


def index(request): #the index view
    stocks = Stock_Name.objects.all()      #quering all todos with the object manager
    nse = Nse()

    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            ticker = request.POST["description"] #title
            #if(Stock_Name.objects.filter(ticker=ticker).exists()):
            #    raise forms.ValidationError(('Stock Aready Present.'))

            q = nse.get_quote(ticker)
            name = q['companyName'] 
            price = q['lastPrice']
            open_price = q['open']

            Stock_detail = Stock_Name(ticker=ticker, name=name, price=price,open=open_price)
            Stock_detail.save() 
            return redirect("/") #reloading the page       
        
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for stockname in checkedlist:
                stock = Stock_Name.objects.get(id=int(stockname))     #getting todo id
                stock.delete() #deleting todo

    return render(request, "index.html", {"Stocks": stocks })


#def update_prices(request):
#    stocks = Stock_Name.objects.all()
#    nse = Nse()
#    for stock in stocks:
#        q = nse.get_quote(stock.ticker)
#        stock.price = q['lastPrice']
#        stock.save()

#    return render(request, "index.html", {"Stocks": stocks })







