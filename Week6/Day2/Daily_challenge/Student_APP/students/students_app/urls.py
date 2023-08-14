from django.urls import path
from .views import StudentMixinView, StudentDetail

urlpatterns = [
    path('students/', StudentMixinView.as_view(), name='student_list'),
    path('student/<int:pk>', StudentDetail.as_view(), name='student-detail'),
    # path('students/?date_joined=<date>', StudentsMixinByDate.as_view(), name='filtered_by_date')
]