
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from .models import Email
from .serializers import EmailSerializer

from django.core.files.storage import default_storage


from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class EmailViewSet(APIView):

    def get(self, request, *args, **kwargs):
        return Response("Hello", status=status.HTTP_200_OK)
       
    #@action(detail=True, methods=['post'])
    def post(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email_data = serializer.validated_data

            email = EmailMessage(
                subject=email_data['Subject'],
                body=email_data['Content'],
                from_email=email_data['From'],
                to=email_data.get('To', '').split(','),
                cc=email_data.get('Cc', '').split(','),
                bcc=email_data.get('Bcc', '').split(','),
            )

            # Send the email
            try:
                email.send()
                # send_mail(
                #     subject=email_data['Subject'],
                #     message=email_data['Content'],
                #     from_email=email_data['From'],
                #     recipient_list=email_data.get('To', '').split(','),
                #     cc=email_data.get('Cc', '').split(','),
                #     bcc=email_data.get('Bcc', '').split(','),
                #     fail_silently=False,
                # )
                return Response({'status': 'Email sent successfully'})
            except Exception as e:
                return Response({'status': f'Error sending email: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

