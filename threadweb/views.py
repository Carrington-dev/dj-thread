from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def send_message(request):
    return Response({
        "message": "It's working as intended!"
    })