# coding=utf-8

from django.conf.urls import url

from .views import CourseList

urlpatterns = [
    # 课程列表
    url(r'^list/$', CourseList.as_view(), name="course_list"),
]
