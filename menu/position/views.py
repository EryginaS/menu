from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from position.models import Position, Category


class PositionsListView(ListView):
    """Вывод списка блюд"""

    context_object_name = 'positions'
    model = Position

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class OrderView(View):
    """
    Вывод информации о заказе:
    - сумма заказа
    - список заказанных блюд
    - список аллергенов, которые содержаться в выбранных блюдах
    """

    def post(self, request):
        data = request.POST
        context = self.get_order_info(data)
        return render(request, 'position/order.html', context)

    @staticmethod
    def get_order_info(data):
        """
        Можно было и сделать через django forms,
        если бы существовала модель заказа
        Также, если бы модель заказа существовала, то
        жтот функционал отправился бы в модель (или сервис)

        """

        total_price = 0
        allergens = []
        order = []

        for key in list(data.keys()):

            if key == 'csrfmiddlewaretoken':
                continue

            position = Position.objects.get(name=key)
            total_price += position.price
            order.append(position.name)
            allergens += [item.name for item in position.allergens.all()]

        return {'order': order, 'price': total_price, 'allergens': set(allergens)}
