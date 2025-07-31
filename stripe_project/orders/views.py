import stripe
from django.views import View
from django.conf import settings
from items.models import Item
from django.http import JsonResponse
from orders.models import Order
from django.forms.models import model_to_dict
from django.shortcuts import render


class CreateStripeCheckoutSessionOrderView(View):
    def get(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        order = Order.objects.get(id=self.kwargs["pk"])

        items = order.to_dict()["items"]

        line_items = []

        for item_id in items:
            item = Item.objects.get(id=item_id)

            line_items.append(
                {
                    "price_data": {
                        "currency": "rub",
                        "unit_amount": int(item.price) * 100,
                        "product_data": {
                            "name": item.name,
                            "description": item.description,
                        },
                    },
                    "quantity": 1,
                }
            )

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            metadata={"product_id": item.product_id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )

        return JsonResponse({"checkout_session_id": checkout_session["id"]})


class OrderView(View):
    def get(self, request, *args, **kwargs):
        order = model_to_dict(Order.objects.get(id=self.kwargs["pk"]))

        order_items = order["items"]
        items = []

        for item_el in order_items:
            item = Item.objects.get(id=item_el.id)
            items.append({ "name": item.name, "price": item.price })

        BACKEND_DOMAIN = settings.BACKEND_DOMAIN
        STRIPE_PUBLISHABLE_KEY = settings.STRIPE_PUBLISHABLE_KEY

        data = {
            "id": order["id"],
            "items": items,
            "BACKEND_DOMAIN": BACKEND_DOMAIN,
            "STRIPE_PUBLISHABLE_KEY": STRIPE_PUBLISHABLE_KEY,
        }

        return render(request, "orders/order.html", context=data)