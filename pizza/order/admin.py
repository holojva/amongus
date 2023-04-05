from django.contrib import admin
from .models import PizzaModel
from django.contrib import messages
from django.utils.translation import ngettext
# Register your models here.
from .models import OrderModel, OrderProxy
@admin.action(description="Set orders to delivered status")
def set_delivered(modeladmin, request, queryset):
    queryset.update(delivery_status="DEL")

class OrderInline(admin.TabularInline) :
    model = OrderProxy
    verbose_name = "order"
    verbose_name_plural = "Create order"
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    exclude = ("pizza_order", )
    list_display = ("address", "time", "all_orders", "delivery_status")

    @admin.action(description="Set orders to delivered status")
    def set_delivered(self, request, queryset):
        updated = queryset.update(delivery_status="DEL")
        self.message_user(request, ngettext("%d order was successfully marked as delivered", "%d orders were successfully marked as delivered",
        updated,
        ) % updated, messages.SUCCESS)
        
    actions = [set_delivered]
                                                         
admin.site.register(OrderModel, OrderAdmin)