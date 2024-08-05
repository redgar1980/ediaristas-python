from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status as status_htpp
from rest_framework import permissions

class Logout(APIView):
    def post(self, request):
        permission_classes = [permissions.IsAuthenticated]

        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status_htpp.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status_htpp.HTTP_400_BAD_REQUEST)