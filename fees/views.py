from django.shortcuts import render , redirect
from .forms import mainFieldsForm , signup_form , login_form
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login , logout
# Create your views here.
def homeView(request):

    context = {

    }

    return render(request, 'fees/home.html', context)

def fesscalc(request):
    feesForm = mainFieldsForm()
    profit = None
    paypal_fees_d = None
    paypal_fees = None
    ebay_fees = None
    ebay_fees_d = None
    ebay_fees_d = 0
    context = {
        'feesForm':feesForm,
    }
    try:
        if request.method == 'POST':
            feesForm = mainFieldsForm(request.POST)
            if feesForm.is_valid():     
                buying_cost = feesForm.cleaned_data['buying_cost']
                silling_price = feesForm.cleaned_data['silling_price']
                stor_type = feesForm.cleaned_data['stor_type']
                product_category = feesForm.cleaned_data['product_category']
                listing_type = feesForm.cleaned_data['listing_type']
                Paypal_rate = feesForm.cleaned_data['Paypal_rate']
                quantity = feesForm.cleaned_data['quantity']
                Shipping_cost = feesForm.cleaned_data['Shipping_cost']
                Shipping_price = feesForm.cleaned_data['Shipping_price']
                top_rated = feesForm.cleaned_data['top_rated']
                net_profit = feesForm.cleaned_data['net_profit']

                if quantity == None:
                    quantity = 1
                if Shipping_cost == None:
                    Shipping_cost = 0
                if Shipping_price == None:
                    Shipping_price = 0


                print('quantuty',quantity , 'buying_cost',buying_cost)

                # stor type is None
                if listing_type :
                    if listing_type == 'F':
                        if top_rated:
                            if stor_type:
                                if stor_type == 'N':
                                    if product_category :
                                        if product_category == 'BM':
                                            ebay_fees = 0.1080
                                        elif product_category == 'GB':
                                            ebay_fees = 0.018
                                        elif product_category == 'HE':
                                            ebay_fees = 0.018
                                            ebay_fees_d = 20
                                        else :
                                            ebay_fees = 0.09
                                else :
                                    if product_category :
                                        if product_category == 'BM':
                                            ebay_fees = 0.1080
                                        elif product_category == 'MI':
                                            ebay_fees = 0.06435
                                        elif product_category == 'GB':
                                            ebay_fees = 0.0315
                                        elif product_category == 'HE':
                                            ebay_fees = 0.0135
                                            ebay_fees_d = 20
                                        elif product_category == 'CF':
                                            ebay_fees = 0.05535
                                        elif product_category == 'CP':
                                            ebay_fees = 0.05535
                                        elif product_category == 'CT':
                                            ebay_fees = 0.036
                                        elif product_category == 'MP':
                                            ebay_fees = 0.07335
                                        else :
                                            ebay_fees = 0.09
                        else :
                            if stor_type:
                                if stor_type == 'N':
                                    if product_category :
                                        if product_category == 'BM':
                                            ebay_fees = 0.12
                                        elif product_category == 'GB':
                                            ebay_fees = 0.035
                                        elif product_category == 'HE':
                                            ebay_fees = 0.02
                                            ebay_fees_d = 20
                                        else :
                                            ebay_fees = 0.1
                                else :
                                    if product_category :
                                        if product_category == 'BM':
                                            ebay_fees = 0.12
                                        elif product_category == 'MI':
                                            ebay_fees = 0.0715
                                        elif product_category == 'GB':
                                            ebay_fees = 0.035
                                        elif product_category == 'HE':
                                            ebay_fees = 0.015
                                            ebay_fees_d = 20
                                        elif product_category == 'CF':
                                            ebay_fees = 0.0615
                                        elif product_category == 'CP':
                                            ebay_fees = 0.0615
                                        elif product_category == 'CT':
                                            ebay_fees = 0.04
                                        elif product_category == 'MP':
                                            ebay_fees = 0.0815
                                        else :
                                            ebay_fees = 0.0915
                    

                if Paypal_rate :
                    # paypal rate = Domestic
                    if Paypal_rate == 'DM':
                        paypal_fees_d = 0.30
                        paypal_fees = 0.029
                    # paypal rate = International
                    elif Paypal_rate == 'IN':
                        paypal_fees_d = 0.30
                        paypal_fees = 0.044
                    # paypal rate = None profit
                    elif Paypal_rate == 'NP':
                        paypal_fees_d = 0.30
                        paypal_fees = 0.022
                    # paypal rate = Micropayment
                    elif Paypal_rate == 'MP':
                        paypal_fees_d = 5
                        paypal_fees = 0.005

                    
                ebay_fees_calc = round((silling_price * quantity * ebay_fees ) + ebay_fees_d ,2)
                paypal_fees_calc = round(((silling_price * quantity * paypal_fees) + paypal_fees_d  ),2)
                costs = round((ebay_fees_calc + paypal_fees_calc + Shipping_cost +(buying_cost*quantity)),2)
                profit = round(((silling_price + Shipping_price - (buying_cost + Shipping_cost)) * quantity - (ebay_fees_calc + paypal_fees_calc)),2 )
                proceeds = (silling_price*quantity) + Shipping_price
            
                       
                context.update({
                    'profit':profit,
                    'Shipping_price':Shipping_price,
                    'ebay_fees':ebay_fees_calc,
                    'paypal_fees':paypal_fees_calc,
                    'costs':costs,
                    'silling_price':silling_price*quantity,
                    'proceeds':proceeds,
                    'buying_cost':buying_cost*quantity,
                    'Shipping_cost':Shipping_cost,
                    })                
                # return JsonResponse(variable_date, safe=False)
    except :
        messages.warning(request, 'Something went wrong please try again later')
        return redirect('home')
    
    return render(request , 'fees/feescalc.html', context)

def SignupVeiw(request):
    form = signup_form
    if request.method == 'POST':
        form = signup_form(request.POST)
        form.save()
        messages.info(request,'cobgrats you was succesfully registered')
        return redirect('home')
    return render(request,'fees/signup.html',{'form':form,})

def LoginVeiw(request):
    form = login_form
    if request.method == 'POST':
        form = login_form(request.POST)  
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username , password=password)
            if user is not None:
                login(request, user)
                messages.info(request,'you was succesfully login')
                return redirect('home')
    return render(request,'fees/login.html',{'form':form})

def LogOutVeiw(request):
    logout(request)
    messages.info(request,'logout successfully')
    return redirect('home')