# from rest_framework import serializers
#
# from .models import UserDetails
#
#
# class UserDetailsSerializers(serializers.ModelSerializer):
#     # username = serializers.CharField(max_length=20)
#     # first_name = serializers.CharField(max_length=20)
#     # last_name = serializers.CharField(max_length=60)
#     # DOB = serializers.DateField()
#
#     class Meta:
#         model = UserDetails
#         fields = "__all__"
#
#     def validate(self, attrs):
#         # name = attrs.get('username')
#         # queryset = LoginPage.objects.filter(username=name).first()
#         # if queryset is not None:
#         #     raise ValueError("name already exists")
#         return attrs
#
#     def create(self, validated_data):
#         UserDetails.objects.create(**validated_data)
#         return validated_data
