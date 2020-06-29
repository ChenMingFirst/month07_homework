from django.shortcuts import render
from rest_framework.views import APIView
from .models import UserModel
import jwt
from month07.settings import SECRET_KEY  # 导入 setting中的 秘钥
from rest_framework.response import Response


# 定义 登录接口开发
class LoginView(APIView):
    def post(self, request):
        # 获取传递来的用户名 密码
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 进行验证 是否正确是否存在
        user = UserModel.objects.filter(username=username, password=password).first()
        if user:
            info = {
                "uid": user.id,
                "username": user.username
            }
            # 验证通过，进行jwt令牌生成
            token = jwt.encode(info, SECRET_KEY)
            return Response({"msg": "登录成功", "token": token})
        else:
            # 验证失败
            return Response({"msg": "登录失败"}, status=401)


# 定义一个测试接口
class TestView(APIView):
    def get(self, request):

        uid = request.COOKIES.get("uid")
        if uid:
            return Response({"msg": "令牌有效"})
        else:

            return Response({"msg": "令牌无效"}, status=401)

    def post(self, request):
        uid = request.COOKIES.get("uid")
        if uid:
            return Response({"msg": "令牌有效"})
        else:
            return Response({"msg": "令牌无效"}, status=401)
