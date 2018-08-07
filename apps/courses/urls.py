# coding=utf-8

from django.conf.urls import url

from .views import CourseList, CourseDetailView, CourseInfoView

urlpatterns = [
    # 课程列表
    url(r'^list/$', CourseList.as_view(), name="course_list"),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    # 章节详情页
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
]
