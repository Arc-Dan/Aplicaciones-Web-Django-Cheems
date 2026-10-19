from django.shortcuts import render
from .entities.user import User
from .entities.work_order import Work_order
from .entities.work_order_history import Work_order_history

# Create your views here. ACTION: CREAR, SOLUCIONAR, CANCELAR
def index(request):
    users = User.get_all()
    return render(request, 'hello/index.html', {'users': users})

def work_orders(request):
    work_orders = Work_order.get_all()
    return render(request, 'hello/work_order_view.html', {'work_orders': work_orders})

def work_orders_history(request):
    work_orders_history = Work_order_history.get_all()
    return render(request, 'hello/work_order_history_view.html', {'work_orders_history': work_orders_history})