from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound
from .serializers import FoodsSerializers,CategorySerializers
from .services import list_foods, one_food,list_category,one_category
from foods.models import Foods,Category
# get post put delete

class FoodsView(GenericAPIView):
    serializer_class = FoodsSerializers
    queryset = Foods.objects.all()

    def get_object(self,*args,**kwargs):
        try:
            if "pk" in kwargs and kwargs["pk"]:
                food = Foods.objects.get(pk=kwargs["pk"])
        except Exception as e:
            raise NotFound("not found foods")
        return food

    def get(self,request,*args,**kwargs):
        if "pk" in kwargs and kwargs["pk"]:
            result = one_food(request,kwargs["pk"])
        else:
            result = list_foods(request)
        print("keldi", result)
        return Response(result, status=status.HTTP_200_OK, content_type='application/json')
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        result = one_food(request, pk=data.id)
        return Response(result,status=status.HTTP_201_CREATED, content_type='application/json')

    def put(self,request,*args,**kwargs):
        data = self.get_object(*args, **kwargs)
        serializer = self.get_serializer(data=request.data, instance=data, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        result = one_food(request, pk=data.id)
        return Response(result, status=status.HTTP_200_OK, content_type='application/json')
    def delete(self,request,*args,**kwargs):
        data = Foods.objects.get(pk=kwargs["pk"])
        data.delete()
        data.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializers

    def get(self,request,*args,**kwargs):
        if 'pk' in kwargs and kwargs['pk']:
            result= one_category(request,kwargs["pk"])
        else:
            result=list_category(request)
        return Response(result, status=status.HTTP_200_OK, content_type='application/json')

    def post(self,request,*args,**kwargs):
        data = request.data
        cat = Category(name=data["name"],parent_id=data["parent"])
        root = cat.save()
        result = one_category(request, pk=cat.id)
        return Response(result,status=status.HTTP_201_CREATED, content_type='application/json')

    def put(self,request,*args,**kwargs):
        data = request.data
        if "pk" in kwargs and kwargs["pk"]:
            try:
                root = Category.objects.get(pk=kwargs["pk"])
            except Exception as e:
                raise NotFound("not found category")
            Category.objects.filter(pk=kwargs["pk"]).update(name=data["name"],parent_id=data["parent"])
        result = one_category(request, pk=kwargs["pk"])
        return Response(result, status=status.HTTP_200_OK, content_type='application/json')






