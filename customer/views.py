from django.shortcuts import render
from seller.models import TravelProduct
from django.contrib.auth.decorators import login_required
from seller.models import *
from .models import *
from django.http import JsonResponse
from django.db.models import Sum


def customer_detail(request, pk):
  product = TravelProduct.objects.get(pk=pk)
  amount_list = [i for i in range(2, 11)]
  context = {
    'product': product,
    'amount_list': amount_list,
  }
  return render(request, 'customer/customer_detail.html', context)

@login_required
def customer_cart(request):
  # Cart에서 특정 user가 선택한 모든 product의 product_id를 리스트로 받기
  cart_product_id_list = [product.product_id for product in Cart.objects.filter(user=request.user)]
  # cart_product_id_list 안의 id에 대한 TravelProduct 쿼리셋 가져오기
  product_list = []
  for id in cart_product_id_list:
    product_list.append(TravelProduct.objects.get(id=id))
  context = {
    'product_list': product_list
  }
  return render(request, 'customer/customer_cart.html', context)


@login_required
def modify_cart(request):
  # 어떤 음식(food_id)에 amount를 amountChange만큼 변경하고
  product_pk = request.POST['productPK']
  product = TravelProduct.objects.get(pk=product_pk)
  cart, _= Cart.objects.get_or_create(user=request.user, product=product)
  cart.amount += int(request.POST['amountChange'])
  if cart.amount > 0:
    cart.save()
  elif cart.amount == 0:
    cart.delete()  # 장바구니에서 제품을 삭제합니다.
  else:
    # cart.amount가 0보다 작은 경우는 잘못된 요청으로 간주할 수 있습니다.
    return JsonResponse({'message': '잘못된 요청입니다.', 'success': False}, status=400)
  # 변경된 최종 결과를 반환(JSON)

  totalQuantity = request.user.cart_set.aggregate(total_amount=Sum('amount'))['total_amount']

  context = {
    'newQuantity':cart.amount,
    'totalQuantity': totalQuantity,
    'message':'수량이 성공적으로 업데이트됨.',
    'success':True
  }
  return JsonResponse(context)