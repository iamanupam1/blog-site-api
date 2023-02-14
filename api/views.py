from .models import Article, Contact, Comments, Category
from .serializers import ArticleSerializer, ContactSerializer, CommentsSerializer, CategorySerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'ListArticle':'/article-list/',
		'ListFeaturedArticle':'/article-featured/',
        'ArticleDetail':'/article-detail/<pk>/',
        'ListComments':'/comments/',
		'ContactInquiry':'/contact-inquiry/',
		'List Category':'/category-list/',
		}

	return Response(api_urls)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def articleList(request):
	article = Article.objects.filter(status=1).order_by('-created_date')
	serializer = ArticleSerializer(article, many=True)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def articleFeaturedList(request):
	article = Article.objects.filter(is_featured=True, status=1).order_by('-created_date')
	serializer = ArticleSerializer(article, many=True)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def articleDetail(request, pk):
	article = Article.objects.get(slug=pk, status=1)
	serializer = ArticleSerializer(article, many=False)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def commentList(request, pk):
	specificArticle = Article.objects.get(id=pk)
	comments = Comments.objects.filter(article=specificArticle.id).order_by('-created_date')
	
	serializer = CommentsSerializer(comments, many=True)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def commentAdd(request):
    if request.method == "POST":
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentsSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def categoryList(request):
	category = Category.objects.all().order_by('-id')
	serializer = CategorySerializer(category, many=True)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def contactInquiry(request):
    if request.method=='POST':
        inquiry_data=JSONParser().parse(request)
        inquiry_serializer = ContactSerializer(data=inquiry_data)
        if inquiry_serializer.is_valid():
            inquiry_serializer.save()
            return JsonResponse(inquiry_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(inquiry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
