from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from pizza.models import PizzaModel
class OrderModel(models.Model):
    class DeliveryStatus(models.TextChoices) :
        PENDING = "PEN", _("Pending")
        DELIVERED = "DEL", _("Delivered")
    address = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    pizza_order = models.ManyToManyField(PizzaModel)
    delivery_status = models.CharField(
        max_length=3,
        choices=DeliveryStatus.choices,
        default=DeliveryStatus.PENDING
    )
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
    def all_orders(self):
        return "\n".join([order.name for order in self.pizza_order.all()])
    def __str__(self):
        return "Address: " + self.address + ", Order: " + ", ".join(i.name for i in self.pizza_order.all())
class OrderProxy(OrderModel.pizza_order.through):
    class Meta :
        proxy = True
    def __str__(self):
        return str(self.ordermodel)