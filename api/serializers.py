from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Article, Contact, Comments, Category

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields ='__all__'

class CommentsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comments
		fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields ='__all__'

class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = '__all__'