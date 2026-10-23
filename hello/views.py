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
        user_id = request.POST.get('id')

        if user_id:
            User.update(user_id, request.POST.get('name'), request.POST.get('account'), request.POST.get('password'), request.POST.get('profile'))
        else:
            User.create(request.POST.get('name'), request.POST.get('account'), request.POST.get('password'), request.POST.get('profile'))
        return redirect('/')

    edit_id = request.GET.get('edit')
    selected_user = None
    if edit_id:
        selected_user = User.get_by_id(edit_id)

    users = User.get_all()
    return render(request, 'hello/user_view.html', {'users': users, 'selected_user': selected_user})

"""
def users(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        account = request.POST.get('account')
        password = request.POST.get('password')
        profile = request.POST.get('profile')

        User.create(name=name, account=account, password=password, profile=profile)
        return redirect('/')

    users = User.get_all()
    return render(request, 'hello/user_view.html', {'users': users})


def user_update(request):
    if request.method == 'PUT':
        name = request.PUT.get('name')
        account = request.PUT.get('account')
        password = request.PUT.get('password')
        profile = request.PUT.get('profile')

        User.update(name=name, account=account, password=password, profile=profile)
        return redirect('/')

    users = User.get_all()
    return render(request, 'hello/user_view.html', {'users': users})
"""

# Vistas de work_order
def work_orders(request):
    if request.method == 'POST':
        order_id = request.POST.get('id')

        if order_id:
            Work_order.update(
                id=order_id,
                title=request.POST.get('title'),
                description=request.POST.get('description'),
            )
        else:
            Work_order.create(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
            )
        return redirect('work_orders')

    edit_id = request.GET.get('edit')
    selected_work_order = None
    if edit_id:
        selected_work_order = Work_order.get_by_id(edit_id)

    work_orders = Work_order.get_all()
    return render(request, 'hello/work_order_view.html', {
        'work_orders': work_orders,
        'selected_work_order': selected_work_order,
    })

# Vistas de work_order_history
def work_orders_history(request):
    work_orders_history = Work_order_history.get_all()
    return render(request, 'hello/work_order_history_view.html', {'work_orders_history': work_orders_history})
