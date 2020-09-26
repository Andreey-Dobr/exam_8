from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Review, Product


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review/create.html'
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        return redirect('product_view', pk=product.pk)


class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'review/update.html'
    form_class = ReviewForm
    #permission_required = 'webapp.change_comment'

    #def has_permission(self):
    #    comment = self.get_object()
    #    return super().has_permission() or comment.author == self.request.user

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(DeleteView):
    model = Review
    #permission_required = 'webapp.delete_comment'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    #def has_permission(self):
    #    comment = self.get_object()
    #    return super().has_permission() or comment.author == self.request.user

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.product.pk})