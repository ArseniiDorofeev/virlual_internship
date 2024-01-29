from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .data_manager import DataManager


class SubmitDataView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        data = request.data

        try:
            pereval_id = DataManager.add_pereval(data)
            return Response({'status': 200, 'message': None, 'id': pereval_id}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 500, 'message': str(e), 'id': None},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
