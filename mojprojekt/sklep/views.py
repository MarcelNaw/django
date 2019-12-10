from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import OrderForm, ComplaintForm
from .models import Product, Order, Complaint, OrderedProduct


def product_list(request):
    products = Product.objects.order_by('id')
    context = {'products': products}

    return render(
        request,
        "sklep/list.html",
        context
    )


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(
        request,
        "sklep/details.html",
        context
    )


def index(request):
    return render(
        request,
        "sklep/index.html"
    )


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order(
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                delivery=form.cleaned_data['delivery']
            )
            order.save()
            return HttpResponseRedirect('/order/'+str(order.id))
    else:
        form = OrderForm()
    return render(request, "sklep/order_form.html", {"form": form})


#def order_details(request, order_id):
   # order = get_object_or_404(Order, pk=order_id)
    #total_price = order.get_total_price()
    #return HttpResponse(total_price)

def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    total_price = order.get_total_price()
    return render(
        request,
        "sklep/order.html",
        {'total_price': total_price, 'products': OrderedProduct.objects.filter(order=order_id)}
    )

def complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = Complaint(
                name=form.cleaned_data['name'],
                message=form.cleaned_data['message']
                )
            complaint.save()
            return HttpResponseRedirect('/complaint/'+str(complaint.id))
    else:
        form = ComplaintForm()
    return render(request, "sklep/complaint_form.html", {"form": form})


def complaint_details(request, complaint_id):
    complaint = get_object_or_404(Complaint, pk=complaint_id)
    context = {'complaint':complaint}
    return render(
        request,
        "sklep/complaint.html",
        context
    )