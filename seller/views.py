from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


# 전체 product에서 특정 user(판매자)의 product만 가져오기
@login_required # 로그인이 되어있어야 작동되는 함수
def seller_index(request):
  product = TravelProduct.objects.filter(user=request.user)
  context = {
    'product_list':product,
  }
  return render(request, 'seller/seller_index.html', context)

@login_required
def add_product(request):
  # get
  if request.method == 'GET':
    return render(request, 'seller/seller_add_product.html')
  # post
  elif request.method == 'POST':
    # 폼에서 전달되는 각 값을 뽑아와서 DB에 저장
    # product_name, price, description
    # category = Category.objects.get(name=request.POST['category'])  
    user = request.user

    uploaded_file = request.FILES['img_file']
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name, uploaded_file)
    url = fs.url(name)
    TravelProduct.objects.create(user=user, name=request.POST['productname'], price=request.POST['productprice'], description=request.POST['context'] , Image_url=url)
    return redirect('seller:seller_index')
  
def product_detail(request, pk):
  product = TravelProduct.objects.get(pk=pk)
  context = {
    'product': product
  }
  return render(request, 'seller/seller_product_detail.html', context)

def product_delete(request, pk):
  product = TravelProduct.objects.get(pk=pk)
  product.delete()
  return redirect('seller:seller_index')