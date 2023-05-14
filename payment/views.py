from django.shortcuts import *
from django.views import *
from video.models import *
from .cart import Cart


class CartDetailView(View):
    template_name = "payment/cart-detail.html"

    def get(self, request):
        return render(request, self.template_name, {'cart': Cart(request)})


class CartAddView(View):
    def post(self, request, pk):
        video = get_object_or_404(Video, id=pk)
        cart = Cart(request)
        cart.add(video)
        return redirect('payment:cart-detail')


class CartDeleteView(View):
    def get(self, request, pk):
        cart = Cart(request)
        cart.delete(pk)
        return redirect('payment:cart-detail')
