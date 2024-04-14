# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


"""class BlogPostListcreate(generics.ListCreateAPIView):
   queryset=BlogPost.objects.all()
   serializer_class=BlogPostSerializer 
    

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer 
    
    """





@api_view(['POST','GET'])
def submit_blog_post(request):
    if request.method == 'POST':
        # Extract data from the form
        title = request.data.get('title')
        content = request.data.get('content')
        
        # Create a dictionary with the form data
        data = {'title': title, 'content': content}
        
        # Pass the data to the serializer for validation and saving
        serializer = BlogPostSerializer(data=data)
        
        if serializer.is_valid():
            # If data is valid, save the blog post
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            #value=BlogPost.objects.all()
            #blog_posts=BlogPostSerializer(value,many=True)
            #return render(request,'valueform.html',{'data_value':blog_posts.data})
        else:
            # If data is invalid, return error response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request,'data_form.html') 