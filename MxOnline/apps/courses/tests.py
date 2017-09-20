from django.test import TestCase
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View

from django.http import HttpResponse
from django.db.models import Q

from .models import Course, CourseResource
from operation.models import UserFavorite, CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin
# Create your tests here.
class CourseInfoView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.students += 1
        course.save()
    
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
    
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()
    
        user_cousers = UserCourse.objects.filter(course=course)
        user_ids = [user_couser.user.id for user_couser in user_cousers]
        return user_ids

k = get("chenmiao")
print(k)


# class courseinfoview:
#     def recommendation(id):
#         recommendation_course_list = []
#         k, nearuser = recommend("%s" % id)
#         for i in range(len(k)):
#             recommendation_course_list.append(k[1][0])
#         return recommendation_course_list[:3], nearuser[:3]



