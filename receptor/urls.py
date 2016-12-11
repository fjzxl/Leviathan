from django.conf.urls import url
from receptor import views as recViews
from django.conf import settings

urlpatterns = [
    url('^$',recViews.index),
    url('^login/$',recViews.login,name='login'),
    url('^logout/$',recViews.logout,name='logout'),
    url(r'^appointments/(\w+)*$',recViews.showAppoint,name='showAppointments'),
    url('^confirmAppointments/$',recViews.confirmAppointment,name='confirmAppointments'),
    url('^register/$',recViews.register,name='register'),
]