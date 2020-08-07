from django.shortcuts import render
from .models import blogModel
# Create your views here.
def index(request):
	bm = blogModel.objects.all()
	return render(request, 'blog/index.html', {'bm':bm})