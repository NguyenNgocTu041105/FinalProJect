from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count
from .models import Blog, Rates, Comments
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializers
# Create your views here.

@api_view(['GET'])
def blog_list_view(request):
    blog_list=Blog.objects.all().order_by('-created_at')
    paginator=Paginator(blog_list,3)
    page_number=request.query_params.get('page')
    blogs=paginator.get_page(page_number)
    serializer=BlogSerializers(blogs,many=True)
    return Response(
        {
            'total_pages':paginator.num_pages,
            'current_page':blogs.number,
            'previous':blogs.has_previous(),
            'next':blogs.has_next(),
            'blogs':serializer.data,
        }
    )
    
@api_view(['GET'])
def blog_detail_view(request,id):
    blog_item = get_object_or_404(Blog, id=id)
    serializer=BlogSerializers(blog_item)
    pre_blog = Blog.objects.filter(id__lt=blog_item.id).order_by('-id').first()
    next_blog = Blog.objects.filter(id__gt=blog_item.id).order_by('id').first()    

    rate_list=Rates.objects.filter(blog=blog_item) 
    total_votes=len(rate_list)
    
    sum_rate=sum([r.rates for r in rate_list])
    avg_rate=sum_rate/total_votes if total_votes>0 else 0
   
    comments = Comments.objects.filter(blog=blog_item,parent_comment=None).order_by('-created_at').values()
    
    context={
        'blog':serializer.data,
        'prev_blog': BlogSerializers(pre_blog).data if pre_blog else None,
        'next_blog': BlogSerializers(next_blog).data if next_blog else None,
        'rating': {
            'avg_rate':round(avg_rate,1),
            'total_votes':total_votes,
        },
        'comments': list(comments),
    }    
    return Response(context)
   
@api_view(['POST'])
def blog_rate(request):
    blog_id = request.data.get('blog_id')
    rate = request.data.get('rate')
    author_id = request.data.get('author_id')
    
    try:
        blog = Blog.objects.get(id=blog_id)
            
        if Rates.objects.filter(blog_id=blog_id, author_id=author_id).exists():
            return Response({'success': False, 'error': 'Bạn đã đánh giá bài viết này rồi!'},status=status.HTTP_400_BAD_REQUEST)
                
        Rates.objects.create(blog_id=blog_id, rates=int(rate), author_id=author_id)
        return Response({'success': True},status=status.HTTP_201_CREATED)
            
    except Blog.DoesNotExist:
        return Response({'success': False, 'error': 'Blog not found'},status=status.HTTP_404_NOT_FOUND)
            

@api_view(['POST'])
def blog_comment(request):
    blog_id=request.data.get('blog_id')
    comment=request.data.get('comment')
    parent_id=request.data.get('parent_id')
    
    if request.user.is_authenticated:
        data={
            'blog_id':blog_id,
            'comment':comment,
            'author_id':request.user.id,
            'author_name':request.user.username,
            'author_image':request.user.avatar,
        }
            
        if parent_id:
            data['parent_comment_id']=parent_id
        try:
            new_comment=Comments.objects.create(**data)
            comment_data=Comments.objects.filter(id=new_comment.id).values().first()
            return Response({'success':True,'comment':comment_data},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'success':False,'error': str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    return Response({'success':False,'error':'User chưa đăng nhập'},status=status.HTTP_401_UNAUTHORIZED)
