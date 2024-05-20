from django.urls import path
from account.views import EmployeeProfile, CustomerProfile, ClientProfile, UpdateClientProfile

app_name = 'account'

urlpatterns = [
    path('employee', EmployeeProfile.as_view(), name='employee_profile'),
    path('customer', CustomerProfile.as_view(), name='customer_profile'),
    path('client-update', UpdateClientProfile.as_view(), name='update_client_profile'),
    path('', ClientProfile.as_view(), name='client_profile')
]
