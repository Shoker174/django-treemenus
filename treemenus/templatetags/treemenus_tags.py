# -*- coding: utf-8 -*-
from django import template
from django.template.loader import render_to_string
from treemenus.models import Menu
from django.templatetags.static import PrefixNode


register = template.Library()


@register.simple_tag
def get_treemenus_static_prefix():
    return PrefixNode.handle_simple("STATIC_URL") + 'img/treemenus'


@register.simple_tag(takes_context=True)
def show_menu(context, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name).get_cache_data()
        context['menu'] = menu
        return render_to_string(['treemenus/%s/menu.html' % menu['name'], 'treemenus/menu.html'], context.flatten())
    except Exception:
        return ''


@register.simple_tag(takes_context=True)
def show_menu_item(context, menu_item):
    menu = context.get('menu')
    if menu and menu_item['show']:
        context['item'] = menu_item
        return render_to_string(['treemenus/%s/menu_item.html' % menu['name'], 'treemenus/menu_item.html'], context.flatten())
    else:
        return ''
