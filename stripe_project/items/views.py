import stripe
from django.conf import settings
from items.models import Item
from django.views import View
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 


@csrf_exempt
class CreateStripeCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        item = Item.objects.get(id=self.kwargs["pk"])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
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
            ],
            metadata={"product_id": item.product_id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return JsonResponse({"checkout_session_id": checkout_session["id"]})


@csrf_exempt
class ItemView(View):
    def get(self, request, *args, **kwargs):
        item = model_to_dict(Item.objects.get(id=self.kwargs["pk"]))
        BACKEND_DOMAIN = settings.BACKEND_DOMAIN
        STRIPE_PUBLISHABLE_KEY = settings.STRIPE_PUBLISHABLE_KEY

        data = {
            "id": item["id"],
            "name": item["name"],
            "description": item["description"],
            "price": item["price"],
            "image": item["image"],
            "BACKEND_DOMAIN": BACKEND_DOMAIN,
            "STRIPE_PUBLISHABLE_KEY": STRIPE_PUBLISHABLE_KEY,
        }

        return render(request, "items/item.html", context=data)


class SuccessView(TemplateView):
    template_name = "stripe/success.html"


class CancelView(TemplateView):
    template_name = "stripe/cancel.html"
