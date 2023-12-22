from django.urls import path, include

from main.views import view_item

urlpatterns = [
    path('item/<int:id>', view_item),
    # path('buy/<int:id>', ),
]