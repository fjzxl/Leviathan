# -*- coding: utf-8 -*-
from django import forms


# Forms
class RegisterForm(forms.Form):
    username = forms.CharField(min_length=4, label='用户名',widget=forms.TextInput(attrs={'class':"form-control form-control-solid placeholder-no-fix",'autocomplete':"off",'placeholder':"用户名",'name':"username",'type':"text"}))
    password = forms.CharField(min_length=4, label='密码',widget=forms.TextInput(attrs={'class':"form-control form-control-solid placeholder-no-fix",'autocomplete':"off",'placeholder':"密码",'name':"password",'type':"password"}))
    second_password = forms.CharField(min_length=4, label='再次输入密码',widget=forms.TextInput(attrs={'class':"form-control form-control-solid placeholder-no-fix",'autocomplete':"off",'placeholder':"再次输入密码",'name':"password",'type':"password"}))
    hospital=forms.CharField(min_length=4,label='医院名',widget=forms.TextInput(attrs={'class':"form-control form-control-solid placeholder-no-fix",'autocomplete':"off",'placeholder':"用户名",'name':"username",'type':"text"}))



class LoginForm(forms.Form):
    username=forms.CharField( label='用户名',widget=forms.TextInput(attrs={'class':"form-control form-control-solid placeholder-no-fix",'autocomplete':"off",'placeholder':"用户名",'name':"username",'type':"text"}))
    password = forms.CharField( label='用户名',widget=forms.TextInput(attrs={'class':"form-control form-control-solid placeholder-no-fix",'autocomplete':"off",'placeholder':"密码",'name':"password",'type':"password"}))