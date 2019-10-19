from rest_framework import routers
from django.conf.urls import url, include
from .views import  AllProduct, AllDistrict, Areas, Orderstatus, OrderList, Order,Customcheckout

router = routers.DefaultRouter()
router.register(r'allproduct', AllProduct)
router.register(r'alldistrict', AllDistrict)
router.register(r'areas', Areas)
router.register(r'orderstatus', Orderstatus)
router.register(r'orderlist', OrderList)
router.register(r'allorder', Order)
router.register(r'customcheckout', Customcheckout)

urlpatterns = [
    url(r'^', include(router.urls)),
]
