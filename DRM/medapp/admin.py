from django.contrib import admin
from .admin import Company,MedicalDetails,Medicine,Employee,Customer,Bill,EmployeeSalary,BillDetails,CustomerRequest,CompanyAccount,Companybank,EployeeBank


# Register your models here.
admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(MedicalDetails)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(EmployeeSalary)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
admin.site.register(CompanyAccount)
admin.site.register(Companybank)
admin.site.register(EployeeBank)
