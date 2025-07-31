from django.contrib import admin
from django.urls import path
from items.views import (
    CreateStripeCheckoutSessionView,
    ItemView,
    SuccessView,
    CancelView,
    MainView,
)
from orders.views import CreateStripeCheckoutSessionOrderView, OrderView


urlpatterns = [
    path("item/<int:pk>/", ItemView.as_view(), name="items"),
    path(
        "buy/<int:pk>/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
    path("order/<int:pk>/", OrderView.as_view(), name="orders"),
    path("buy/order/<int:pk>/", CreateStripeCheckoutSessionOrderView.as_view(), name="create-order-checkout-session"),
    path("admin/", admin.site.urls),
    path("", MainView.as_view(), name="main"),
]
