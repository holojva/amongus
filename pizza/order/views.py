from django.shortcuts import render, redirect
from pizza.models import PizzaModel
from .models import OrderModel
from django.forms import modelformset_factory
from .forms import CreateForm, CreateOrderModelForm
# Create your views here.
def create_model_order(request, *args, **kwargs):
    pizzas = PizzaModel.objects.all()
    # OrderFormSet = modelformset_factory(
    #     OrderModel,
    #     form= CreateOrderModelForm,
    #     extra=2
    # )
    model_form = CreateOrderModelForm(request.POST or None) #OrderFormSet(
        # queryset=OrderModel.objects.none(),
        # initial=[{"address":"modelformset street"}]
        # )
    # print(model_form.data)
    # if model_form.is_valid():
    #     model_form.save()
    #     return redirect("createmodelorder")
    context = {
        "pizzas": pizzas,
        "modelform": model_form
    }
    return render(request, "order/create_model_order.html", context=context)
def create_order(request, *args, **kwargs) :
    order_form = CreateForm(request.POST or None)
    print(order_form.data)
    if order_form.is_valid():
        address = order_form.cleaned_data.get("address")
        order = dict(order_form.data).get("choice")
        pizza_objects = [PizzaModel.objects.get(id=i) for i in order]
        print(pizza_objects)
        new_order = OrderModel.objects.create(address=address)
        # pizza = PizzaModel.objects.get(pk=order)
        new_order.pizza_order.add(*pizza_objects)
        new_order.save()
        return redirect("createorder")
        print(address, order)

    context = {"order": PizzaModel.objects.all(), "order_form": order_form}
    return render(request, "order/create_order.html", context=context)