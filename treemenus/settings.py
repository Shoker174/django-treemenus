from django.conf import settings

NAMES = getattr(settings, 'TREEMENUS_NAMES', dict())
