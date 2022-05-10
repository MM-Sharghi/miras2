from django.db import models
from Users.models import Users
from extensions.DateJalali import django_jalali
from extensions.optimization import photo_optimization


class MainUser(models.Model):
    admin = models.ForeignKey(Users,on_delete=models.CASCADE,default=1,verbose_name='Admin',related_name='mainUser_admin')
    Owner = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='Owner',related_name='mainUser_owner')
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='User')
    identifierـcode = models.CharField(max_length=30,verbose_name='Identifier code')
    places = models.IntegerField(default=1,verbose_name='Places')
    r_or_l = models.BooleanField(default=False,verbose_name='Ruser or Luser')
    payment_status = models.BooleanField(default=False,verbose_name='Payment Status')

    def RL_aLL(self):
        result = []
        m = MainUser.objects.filter(payment_status=True,Owner__id=self.Owner.id).all()

        if m is not None:
            for k in m:
                R = Rusers.objects.filter(main__user_id=k.user.id).first()
                if R is not None:
                    active_right = Rusers.objects.filter(main__Owner_id=R.main.user.id,main__payment_status=True).count()
                else:
                    active_right = None
                L = Lusers.objects.filter(main__user_id=k.user.id).first()
                if L is not None:
                    active_left = Lusers.objects.filter(main__Owner_id=L.main.user.id,main__payment_status=True).count()
                else:
                    active_left = None

                if R is not None and L is None:
                    result.append({f'{k.user.id}': {f'R': {'admin': R.main.admin.username, 'owner': R.main.Owner.username, f'user': k.user.username,'active_right': active_right},f'L': None}})

                elif L is not None and R is None:
                    result.append({f'{k.user.id}': {f'R': None,f'L': {'admin': L.main.admin.username, 'owner': L.main.Owner.username, f'user': k.user.username,'active_left': active_left}}})

                else:
                    result.append({f'{k.user.id}': {f'R': {'admin': R.main.admin.username, 'owner': R.main.Owner.username, f'user': k.user.username,'active_right': active_right},f'L': {'admin': L.main.admin.username, 'owner': L.main.Owner.username, f'user': k.user.username,'active_left': active_left}}})

            return result
        else:
            return None

    def __str__(self):
        return self.identifierـcode

class Rusers(models.Model):
    main = models.ForeignKey(MainUser,on_delete=models.CASCADE,verbose_name='Main')
    user = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='User')

    def __str__(self):
        return self.main.identifierـcode


class Lusers(models.Model):
    main = models.ForeignKey(MainUser, on_delete=models.CASCADE, verbose_name='Main')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return self.main.identifierـcode



class Contracts(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='User')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date')

    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return f'{self.user.id}-{self.user.username}'





class Cards(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='User')
    first_name = models.CharField(max_length=99,verbose_name='First name')
    last_name = models.CharField(max_length=99,verbose_name='Last name')
    accountـnumber = models.IntegerField(verbose_name='Account number')
    shaba_number = models.IntegerField(verbose_name='Shaba number')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date')

    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return f'{self.accountـnumber}'



#
# class ProductSubCategories_2(models.Model):
#     name = models.CharField(max_length=999, verbose_name='Name')
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# class ProductSubCategories_1(models.Model):
#     name = models.CharField(max_length=999, verbose_name='Name')
#     sub_categories2 = models.ManyToManyField(ProductSubCategories_2, blank=True, verbose_name='Sub Categories 2')
#
#     def __str__(self):
#         return f'{self.name}'
#
#
# class ProductMainCategories(models.Model):
#     name = models.CharField(max_length=999, verbose_name='Name')
#     image = models.ImageField(upload_to='ProductMainCategoriesImage', blank=True, null=True, verbose_name='Image')
#     sub_categories1 = models.ManyToManyField(ProductSubCategories_1, blank=True, verbose_name='Sub Categories 1')
#
#     def save(self, *args, **kwargs):
#         photo_optimization(self.image)
#         super(ProductMainCategories, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return f'{self.name}'
#
# class Products(models.Model):
#     user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='USer')
#     title = models.CharField(max_length=999,verbose_name='Title')
#     slug = models.CharField(max_length=999,verbose_name='Slug')
#     descriptions = models.CharField(max_length=999,verbose_name='Descriptions')
#     image = models.ImageField(upload_to='Products',verbose_name='Image')
#     image1 = models.ImageField(upload_to='Products',blank=True,null=True,verbose_name='Image1')
#     image2 = models.ImageField(upload_to='Products',blank=True,null=True,verbose_name='Image2')
#     image3 = models.ImageField(upload_to='Products',blank=True,null=True,verbose_name='Image3')
#     price = models.IntegerField(default=0)
#     maincategories = models.ManyToManyField(ProductMainCategories,blank=False,verbose_name='Main Category')
#     subCategories1 = models.ManyToManyField(ProductSubCategories_1,blank=False,verbose_name='Sub Category 1')
#     subCategories2 = models.ManyToManyField(ProductSubCategories_2,blank=False,verbose_name='Sub Category 2')
#     volume = models.CharField(max_length=999,verbose_name='Volume')
#     compounds = models.CharField(max_length=999,verbose_name='Compounds')
#     licenseـissuer = models.CharField(max_length=999,verbose_name='License issuer')
#     date = models.DateTimeField(auto_now_add=True)
#     limit = models.IntegerField(default=0,blank=False,null=False,verbose_name='Limit')
#     status = models.BooleanField(default=True)
#
#     def jdate(self):
#         return django_jalali(self.date)
#
#     def save(self, *args, **kwargs):
#         photo_optimization(self.image)
#         super(Products, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.title
#
# class ProductsComments(models.Model):
#     user = models.ForeignKey(Users,null=False, blank=False,on_delete=models.CASCADE,verbose_name='User')
#     product = models.ForeignKey(Products,null=False, blank=False, on_delete=models.CASCADE,verbose_name='Prodcut Id')
#     comment = models.TextField(null=False, blank=False,verbose_name='Comment')
#     status = models.BooleanField(default=False, verbose_name='Status')
#     date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date')
#
#     def user_fullname(self):
#         return f'{self.user.first_name} {self.user.last_name}'
#
#     def __str__(self):
#         return self.comment
#
#
#
#
#
# class ProductsCarts(models.Model):
#     user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Shoper')
#     payment_date = models.DateTimeField(auto_now_add=True,blank=True,null=True, verbose_name='Payment Date')
#     payment_status = models.BooleanField(default=False, verbose_name='Payment Status')
#
#     def jdate(self):
#         return django_jalali(self.payment_date)
#
#     def __str__(self):
#         return f'{self.user}'
#
#
# class ProductsOrders(models.Model):
#     cart = models.ForeignKey(ProductsCarts, on_delete=models.CASCADE,blank=True,null=True,verbose_name='Cart')
#     shopper = models.ForeignKey(Users, on_delete=models.CASCADE,blank=True,null=True,verbose_name='shopper')
#     title = models.CharField(blank=True,null=True,max_length=999, verbose_name='Title')
#     description = models.TextField(blank=True,null=True,verbose_name='Description')
#     price = models.IntegerField(blank=True, null=True, verbose_name='Price')
#     product = models.ForeignKey(Products,on_delete=models.CASCADE,blank=False, null=False, verbose_name='Product ')
#     payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Payment Date')
#     payment_status = models.BooleanField(default=False, verbose_name='Payment Status')
#
#     def product_image(self):
#         if self.product.image.url:
#             return self.product.image.url
#         else:
#             return None