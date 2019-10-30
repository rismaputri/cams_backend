from django.shortcuts import render

# Create your views here.
import csv
from django.http import HttpResponse
from customerapp.models import  Customer

def customer_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=customerapp.csv'
    writer = csv.writer(response)
    customer = Customer.objects.all()

    writer.writerow(['Nama','Gaji','Jenis Kelamin','Existing','Occupation','Alamat','Kendaraan'])
    for customer in customer:
        writer.writerow([customer.nama, customer.gaji, customer.jk, customer.existing , customer.occupation,
                         customer.alamat, customer.kendaraan])

    return response