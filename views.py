# dashboard/views.py
from django.shortcuts import render, redirect
from .forms import DashboardItemForm
from .models import DashboardItem

def dashboard_view(request):
    if request.method == 'POST':
        form = DashboardItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_view')
    else:
        form = DashboardItemForm()

    items = DashboardItem.objects.all()
    return render(request, 'dashboard/dashboard.html', {'form': form, 'items': items})
