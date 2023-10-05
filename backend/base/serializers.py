from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Restaurant,Restaurantmenu,Order,OrderItem,ShippingAddress
from rest_framework_simplejwt.tokens import RefreshToken
class UserSerializer(serializers.ModelSerializer):
    name=serializers.SerializerMethodField(read_only=True)
    isAdmin=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['id','username','email','name','isAdmin']
    def get_name(self,obj):
        name=obj.first_name
        if name=="":
            name= obj.email
        return name
    def get_isAdmin(self,obj):
        return obj.is_staff

class UserSerializerWithToken(UserSerializer):
    token=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=User
        fields=['id','username','email','name','isAdmin','token']
    def get_token(self,obj):
        token=RefreshToken.for_user(obj)
        return str(token.access_token)

class RestaurantmenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurantmenu
        fields='__all__'
    


class RestaurantSerializer(serializers.ModelSerializer):
    content=RestaurantmenuSerializer(many=True,read_only=True)
    class Meta:
        model=Restaurant
        fields=['id','name','description','rating','time','price','path','content']

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    orderItems = serializers.SerializerMethodField(read_only=True)
    shippingAddress = serializers.SerializerMethodField(read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def get_orderItems(self, obj):
        items = obj.orderitem_set.all()
        serializer = OrderItemSerializer(items, many=True)
        return serializer.data

    def get_shippingAddress(self, obj):
        try:
            street = ShippingAddressSerializer(obj.shippingaddress, many=False).data
        except:
            street = False
        return street

    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user, many=False)
        return serializer.data