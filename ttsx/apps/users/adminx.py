# _*_ coding:utf-8 _*_
__auther__ = "bobby"
__date__ = "2018/9/29 0:13"

import xadmin
from xadmin import views

from .models import Emallver, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕学管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"


class EmallverAdmin(object):
    list_display = ["code", "email", "send_type", "send_time"]
    search_fields = ["code", "email", "send_type"]
    list_filter = ["code", "email", "send_type", "send_time"]


class BannerAdmin(object):
    list_display = ["title", "image", "url", "index","add_time"]
    search_fields = ["title", "image", "url", "index"]
    list_filter = ["title", "image", "url", "index","add_time"]


xadmin.site.register(Emallver, EmallverAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)