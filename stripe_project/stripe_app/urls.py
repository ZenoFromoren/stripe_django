from django.contrib import admin
from django.urls import path
from items.views import (
    CreateStripeCheckoutSessionView,
    ItemView,
    SuccessView,
    CancelView,
    MainView,
)

urlpatterns = [
    path("item/<int:pk>/", ItemView.as_view(), name="items"),
    path(
        "buy/<int:pk>/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),
    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
    path("admin/", admin.site.urls),
    path("", MainView.as_view(), name="main"),
]
