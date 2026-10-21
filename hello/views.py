from django.shortcuts import redirect, render
from .entities.user import User
from .entities.work_order import Work_order
from .entities.work_order_history import Work_order_history

# Create your views here.
def index(request):
    users = User.get_all()
    return render(request, 'hello/index.html', {'users': users})

# Vistas de usuarios
def users(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        account = request.POST.get('account')
        profile = request.POST.get('profile')

        User.create(name=name, account=account, profile=profile)
        return redirect('/')

    users = User.get_all()
    return render(request, 'hello/user_view.html', {'users': users})

"""
def users(request):
    users = User.get_all()
    return render(request, 'hello/user_view.html', {'users': users})

"""

# Vistas de work_order
def work_orders(request):
    work_orders = Work_order.get_all()
    return render(request, 'hello/work_order_view.html', {'work_orders': work_orders})

# Vistas de work_order_history
def work_orders_history(request):
    work_orders_history = Work_order_history.get_all()
    return render(request, 'hello/work_order_history_view.html', {'work_orders_history': work_orders_history})