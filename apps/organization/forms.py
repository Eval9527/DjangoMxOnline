# coding=utf-8
import re
from django import forms

from operation.models import UserAsk


# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     phone = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, max_length=5, max_length=50)


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号是否合法
        :return: mobile
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号非法", code="mobile_invalid")

