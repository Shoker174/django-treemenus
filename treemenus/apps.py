from django.apps import AppConfig
from django.utils.translation import ugettext as _


class TreemenusAppConfig(AppConfig):

    name = 'treemenus'
    try:
        verbose_name = _('Menus')
    except:
        pass

    def ready(self):
        from . import signals