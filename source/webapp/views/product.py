from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product
from webapp.views import product


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    model = Product
    paginate_by = 10
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product


    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class ProductCreate(CreateView):
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})



class Product_Update_View(UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})




    #def test_func(self):
    #    return self.request.user.has_perm('webapp.del_task') or \
    #           self.get_object().author == self.request.user


class Delete_Product(DeleteView):
    template_name = 'product/delet.html'
    model = Product
    context_key = 'product'
    success_url = reverse_lazy('title')



