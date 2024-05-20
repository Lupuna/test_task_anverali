from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from account.models import Employee, Client, Customer


class ClientProfile(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'account/client_profile.html'
    context_object_name = 'client'
    login_url = reverse_lazy('registration:login')

    def get_object(self, queryset=None):
        return Client.objects.get(id=self.request.user.id)


class UpdateClientProfile(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['first_name', 'last_name', 'email', 'phone']
    success_url = reverse_lazy('account:client_profile')
    template_name = 'account/update_client_profile.html'
    login_url = reverse_lazy('registration:login')

    def get_object(self, queryset=None):
        return Client.objects.get(id=self.request.user.id)


class EmployeeProfile(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'account/employee_profile.html'
    context_object_name = 'employee'
    login_url = reverse_lazy('registration:login')

    def get_object(self, queryset=None):
        return Employee.objects.get(client=self.request.user.id)


class CustomerProfile(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'account/customer_profile.html'
    context_object_name = 'customer'
    login_url = reverse_lazy('registration:login')

    def get_object(self, queryset=None):
        return Customer.objects.get(client=self.request.user.id)
