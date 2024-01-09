from django.urls import path,include
from Api.views import CollegeViewSet,StudentViwSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'colleges',CollegeViewSet)
router.register(r'students',StudentViwSet)

urlpatterns = [
    path('',include(router.urls))
]