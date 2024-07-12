from django.apps import AppConfig


class IceCreamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ice_cream'
    verbose_name = 'Каталог мороженого'


class ToppingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topping'
    verbose_name = 'Топпинг'


class WrapperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wrapper'
    verbose_name = 'Обёртка'


class IceCreamAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ice_cream_admin'
    verbose_name = 'Мороженое'
