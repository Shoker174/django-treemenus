# -*- coding: utf-8 -*-
from django.db.models.signals import post_save, post_delete
from .models import Menu, MenuItem


def menu_change_handler(sender, instance, **kwargs):
    instance.delete_cache_data()


post_save.connect(menu_change_handler, Menu)
post_save.connect(menu_change_handler, MenuItem)
post_delete.connect(menu_change_handler, Menu)
post_delete.connect(menu_change_handler, MenuItem)
