from Derakhti.models import DerakhtiProductsOrders

def amount_purchased(user_id):
    products = DerakhtiProductsOrders.objects.filter(shopper__id=user_id,payment_status=True).order_by('id').all()
    orders = sum([p.price for p in products])
    return orders
