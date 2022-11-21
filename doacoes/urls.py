from django.urls import path
from .views import DoacoesView, DoacoesCreateView, DoacoesDeleteView, DoacoesUpdateView
##from .migrations import views


urlpatterns = [
        path('doacoes/', DoacoesView.as_view(), name='doacoes.index'),
        path('novo/', DoacoesCreateView.as_view(), name='doacoes.novo'),
        path('editar/<int:pk>', DoacoesUpdateView.as_view(), name='doacoes.editar'),
        path('remover/<int:pk>', DoacoesDeleteView.as_view(), name='doacoes.remover'),
]