from django.shortcuts import render, redirect
from django.http import HttpResponse
from medicine.models import Medicine_Type, Medicine_Detail
from medicine.forms import MedicineDetail_Form, MedicineType_Form


# Create your views here.
def index(request):
    medicine_type_list = Medicine_Type.objects.order_by('created')[:5]
    medicine_detail_list = Medicine_Detail.objects.order_by('created')[:5]
    context_dict = {'medicine_type_list': medicine_type_list,
                    'medicine_detail_list': medicine_detail_list}
    return render(request, 'index.html', context_dict)


def medicine(request, medicine_type):
    context_dict = {'medicine_type': medicine_type}
    medicine_type_details = Medicine_Type.objects.get(medicine_type=medicine_type)
    medicine_detail_list = Medicine_Detail.objects.filter(medicine_type=medicine_type_details)
    context_dict['medicine'] = medicine_type_details
    context_dict['medicine_detail_list'] = medicine_detail_list
    return render(request,'medicine.html', context_dict)


def add_medicine_type(request):
    if request.method == 'POST':
        form = MedicineType_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = MedicineType_Form()
    return render(request, 'add_medicine_type.html', {'form': form})

def add_medicine_detail(request, medicine_type):
    if request.method == 'POST':
        form = MedicineDetail_Form(request.POST)
        if form.is_valid():
            medicine_detail = form.save(commit=True)
            try:
                medicine_type_details = Medicine_Type.objects.get(medicine_type=medicine_type)
                medicine_detail.medicine_type = medicine_type_details
            except Medicine_Type.DoesNotExist:
                return render(request, 'add_medicine_detail.html', {})
            medicine_detail.save()
            return medicine(request, medicine_type)
        else:
            print(form.errors)
    else:
        form = MedicineDetail_Form()
    return render(request, 'add_medicine_detail.html', {'form': form,
                                                        'medicine_type': medicine_type})
