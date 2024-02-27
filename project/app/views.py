from django.shortcuts import render
from .models import Customer, Queryt
from django.db.models import Q

# Create your views here.
def home(request):
    # return render(request,'app/base.html')
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')

def category(request):
    return render(request,'app/category.html')

def services(request):
    return render(request,'app/services.html')

def contact(request):
    return render(request,'app/contact.html')

def register(request):
    return render(request,'app/register.html')

def login(request):
    return render(request,'app/login.html')

def logout(request):
    return render(request,'app/login.html')

# p13

def savedata(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        user = Customer.objects.filter(email=email)

        if user: 
            message = "User already exist !!!"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = Customer.objects.create(fname=fname,lname=lname,email=email
                                    ,contact=contact,password=password,cpassword=cpassword)
                message = "User Registered Successfully"
                return render(request,"app/login.html",{'msg':message})
            

    return render(request,'app/login.html')

def dashlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = Customer.objects.filter(email=email)
        if user:
            data = Customer.objects.get(email=email)
            if data.password == password:
                fname=data.fname
                lname=data.lname
                email=data.email
                contact=data.contact

                user={
                    'fname':fname,
                    'lname':lname,
                    'email':email,
                    'contact':contact
                }
                return render(request,"app/dashboard.html",{'key':user})
            else:
                message= "Invalid email or password !!!"
                return render(request,"app/login.html",{'msg':message})
        else:
            message= "Create User"
            return render(request,"app/register.html",{'msg':message})
    else:
            message= "Change method from get to post !!!"
            return render(request,"app/register.html",{'msg':message})
    
def query(request):
    if request.method=='POST':
        email=request.POST['dsh_email']
        query=request.POST['dsh_query']
        OrderId=request.POST['orderid']

        Queryt.objects.create(QueryEmail=email, Query=query, OrderId=OrderId)
        data = Customer.objects.get(email=email)
        fname=data.fname
        lname=data.lname
        email=data.email
        contact=data.contact
        user={
            'fname':fname,
            'lname':lname,
            'email':email,
            'contact':contact
        }
        return render(request,'app/dashboard.html',{'key':user})
        # return render(request,'app/dashboard.html',{'key2':user})
    
def showdata(request,pk):
    # print(pk)

    data=Customer.objects.get(email=pk)
    fname=data.fname
    lname=data.lname
    email=data.email
    contact=data.contact

    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact
    }
    data=Queryt.objects.filter(QueryEmail=pk)
    return render(request,'app/showdata.html',{'key1':data,'user':user})

def delete(request,pk):
    data=Queryt.objects.get(id=pk)
    email=data.QueryEmail
    data.delete()
    data=Queryt.objects.filter(QueryEmail=email)
    return render(request,'app/showdata.html',{'key1':data})

def edit(request,pk):
    # print(pk)
    data=Queryt.objects.get(id=pk)
    id=data.id
    email=data.QueryEmail
    orderid=data.OrderId
    query=data.Query
    print(email)
    print(orderid)
    print(query)
    data1={
        'id':id,
        'email':email,
        'query':query,
        'order':orderid
    }
    data = Customer.objects.get(email=email)
    fname=data.fname
    lname=data.lname
    email=data.email
    contact=data.contact
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact
    }
    return render(request,'app/dashboard.html',{'key':user,'key2':data1})

def update(request,pk):
    print(pk)
    # data=Queryt.objects.get(id=pk)
    QueryEmail=request.POST['dsh_email']
    OrderId=request.POST['orderid']
    Query=request.POST['dsh_query']
    data=Queryt.objects.get(id=pk)
    data.QueryEmail=QueryEmail
    data.OrderId=OrderId
    data.Query=Query
    data.save()

    custdata = Customer.objects.get(email=QueryEmail)
    fname=custdata.fname
    lname=custdata.lname
    email=custdata.email
    contact=custdata.contact
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact
    }
    all_data=Queryt.objects.filter(QueryEmail=QueryEmail)
    return render(request,'app/showdata.html',{'key1':all_data,'key':user})

# def search(request,pk):
#     SQuery=request.POST['search']

#     data=Customer.objects.get(email=pk)
#     fname=data.fname
#     lname=data.lname
#     email=data.email
#     contact=data.contact

#     user={
#         'fname':fname,
#         'lname':lname,
#         'email':email,
#         'contact':contact
#     }
    
#     data=Queryt.objects.filter(Q(QueryEmail=email) & Q(Query=SQuery))

#     return render(request,'app/showdata.html',{'key1':data,'user':user})