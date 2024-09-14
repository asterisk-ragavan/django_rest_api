from rest_framework.response import Response
from .models import Items
from .serializer import Itemserializer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.
class item_list(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        items=Items.objects.all()
        ser=Itemserializer(items,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        ser=Itemserializer(data=request.data)
        if ser.is_valid():
            bc=ser.validated_data['barcode']
            if Items.objects.filter(barcode=bc).exists():
                return Response({"inventory": b"inventory with this barcode already exists"},status=status.HTTP_400_BAD_REQUEST)
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            item=Items.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class item_sort(APIView):
    def get(self,request):
        items=Items.objects.all().order_by("-price")
        ser=Itemserializer(items,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)
    
class item_query(APIView):
    def get(self,request,cat):
        items=Items.objects.filter(category=cat)
        ser=Itemserializer(items,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)