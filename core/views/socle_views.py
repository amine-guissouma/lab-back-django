from rest_framework.response import Response
from rest_framework.views import APIView

from config.config_lab import EXPERIENCE_NAME, LAB_NAME


class LabView(APIView):
    def get(self, request):
        return Response(
            {
                "lab": LAB_NAME,
                "experience": EXPERIENCE_NAME,
            }
        )
