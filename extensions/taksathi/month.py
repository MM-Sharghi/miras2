from Taksathi.models import ProductsOrders
import datetime

def month(user_id):
    date_now = str(datetime.datetime.now()).split(' ')[0].replace('-',',')
    date_spilt = date_now.split(',')
    date = datetime.date(int(date_spilt[0]),int(date_spilt[1]),int(date_spilt[2]))
    orders = []
    for i in range(30):
        days = datetime.timedelta(i)
        date_week = str(date - days).split('-')
        products = ProductsOrders.objects.filter(payment_date__year=date_week[0], payment_date__month=date_week[1],payment_date__day=date_week[2], product__user__id=user_id,payment_status=True).order_by('id').all()
        orders.append(sum([p.price for p in products]))
    return orders


