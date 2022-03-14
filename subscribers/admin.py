from .models import Subscribers

from wagtail.contrib.modeladmin.options import modeladmin_register, ModelAdmin

class SubscriberAdmin(ModelAdmin):
    model = Subscribers
    menu_label = 'Subscribers'
    menu_icon = 'placeholder'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('email', 'name',)
    search_fields = ('email', 'name',)
    # http://127.0.0.1:8000/admin/subscribers/subscribers/?q="sub1"
modeladmin_register(SubscriberAdmin)