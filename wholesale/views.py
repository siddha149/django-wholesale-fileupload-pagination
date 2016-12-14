from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Order, Customer, Document
from django.http import HttpResponse, Http404
from .extra import validate_file_upload, validate_file
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def loginpage(request):
    if request.user.is_authenticated:
        cust = get_object_or_404(Customer, Firstname=request.user.username)
        cid = cust.id
        return redirect('/wholesale/customer/' + str(cid) + '/')
    else:
        return render(request, 'wholesale/loginpage.html')


def loginauth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        cust = get_object_or_404(Customer, Firstname=username)
        cid = cust.id
        return redirect('/wholesale/customer/' + str(cid) + '/')

    else:
        return redirect('/wholesale/invalidlogin/')


def invalidlogin(request):
    if request.user.is_authenticated:
        cust = get_object_or_404(Customer, Firstname=request.user.username)
        cid = cust.id
        return redirect('/wholesale/customer/' + str(cid) + '/')
    else:
        return render(request, 'wholesale/invalidlogin.html')


def logoutpage(request):
    logout(request)
    return render(request, 'wholesale/logout.html')


def customerpage(request, cid):
    if request.user.is_authenticated:
        cust = get_object_or_404(Customer, id=cid)
        corders = Order.objects.filter(Cid=cust)
        products = Product.objects.all()
        documents = Document.objects.filter(Cid=cust)
        context = {'cust': cust, 'corders': corders, 'products': products, 'documents': documents}
        return render(request, 'wholesale/customerpage.html', context)
    else:
        return redirect('/wholesale/invalidlogin/')


def customerorder(request, cid):
    if request.user.is_authenticated:
        cust = get_object_or_404(Customer, id=cid)
        products = Product.objects.all()
        context = {'cust': cust, 'products': products}
        return render(request, 'wholesale/customerorder.html', context)
    else:
        return redirect('/wholesale/invalidlogin/')


def placeorder(request, cid):
    if request.user.is_authenticated:
        cust = get_object_or_404(Customer, id=cid)
        ans = request.POST['product']
        prod = get_object_or_404(Product, id=ans)
        qty = request.POST['quantity']
        o = Order(Pid=prod, Cid=cust, Qty=qty)
        o.save()
        return redirect('/wholesale/customer/' + str(cid) + '/')
    else:
        return redirect('/wholesale/invalidlogin/')


def deleteorder(request):
    if request.user.is_authenticated:
        if request.is_ajax():
            try:
                oid = int(request.POST['oid'])
            except KeyError:
                return HttpResponse('error')

            o = Order.objects.get(id=oid)
            o.delete()
            return HttpResponse(str(oid))
        else:
            raise Http404
    else:
        return redirect('/wholesale/invalidlogin/')


def changeorder(request):
    if request.user.is_authenticated:
        if request.is_ajax():
            try:
                oid = int(request.POST['oid'])
                qty = int(request.POST['qty'])
            except KeyError:
                return HttpResponse('error')

            o = Order.objects.get(id=oid)
            o.Qty = qty
            o.save()
            Amount = o.Amount
            return HttpResponse(str(qty) + " " + str(Amount))
        else:
            raise Http404
    else:
        return redirect('/wholesale/invalidlogin/')


def fileupload(request):
    if request.user.is_authenticated:
        return render(request, 'wholesale/fileupload.html')
    else:
        return redirect('/wholesale/invalidlogin/')


def fileuploadprocess(request):
    if request.user.is_authenticated:
        myfile = request.FILES['myfile']
        file_err = validate_file_upload(myfile)
        if file_err == 'No error':
            cust = get_object_or_404(Customer, Firstname=request.user.username)
            cid = cust.id
            doc = Document(Cid=cust, document=myfile)
            doc.save()
            return redirect('/wholesale/customer/' + str(cid) + '/')
        else:
            return render(request, 'wholesale/fileupload.html', {'file_err': file_err})

    else:
        return redirect('/wholesale/invalidlogin/')


def fileuploadvalidate(request):
    if request.user.is_authenticated:
        if request.is_ajax():
            try:
                file_type = request.POST['file_type']
                file_size = int(request.POST['file_size'])
            except KeyError:
                return HttpResponse('error')

            file_err = validate_file(file_type, file_size)
            if file_err == 'No error':
                return HttpResponse(" ")
            else:
                return HttpResponse(file_err)
        else:
            raise Http404
    else:
        return redirect('/wholesale/invalidlogin/')


def vieworders(request):
    order_list = Order.objects.all()
    paginator = Paginator(order_list, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        orders = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        orders = paginator.page(paginator.num_pages)

    return render(request, 'wholesale/vieworders.html', {'orders': orders})