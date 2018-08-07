# coding=utf-8

from django.conf.urls import url

from .views import CourseList, CourseDetailView, CourseInfoView, CourseCommentView, AddCommentView

urlpatterns = [
    # 课程列表
    url(r'^list/$', CourseList.as_view(), name="course_list"),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    # 章节详情页
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CourseCommentView.as_view(), name="course_comments"),

    # 添加课程评论
    url(r'^add_comment/$', AddCommentView.as_view(), name="add_comment"),
]
