from django.conf.urls import url
from apps.goods.views import IndexView

# 登录装饰器
from django.contrib.auth.decorators import login_required
from apps.goods.views import DetailView, ListView

# /index
urlpatterns = [
    # 跳转到首页显示
    url(r'^index$', IndexView.as_view(),name='index'),
    url(r'^goods/(?P<sku_id>\d+)$', DetailView.as_view(), name='detail'), # 详情页
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(), name='list'), # 列表页

]