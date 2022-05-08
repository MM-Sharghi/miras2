from Taksathi.models import ProductsOrders

def amount_purchased(user_id):
    products = ProductsOrders.objects.filter(product__user__id=user_id,payment_status=True).order_by('id').all()
    orders = sum([p.price for p in products])
    return orders
