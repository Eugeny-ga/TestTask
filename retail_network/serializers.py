from rest_framework import serializers

from retail_network.models import Factory, Retailer, Entrepreneur, Product, Contacts


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Factory
        fields = '__all__'


class RetailerSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    provider = FactorySerializer(read_only=True)

    class Meta:
        model = Retailer
        fields = '__all__'


class EntrepreneurSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    provider = RetailerSerializer(read_only=True)

    class Meta:
        model = Entrepreneur
        fields = '__all__'
