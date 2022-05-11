from extensions.optimization import photo_optimization
from extensions.DateJalali import django_jalali
from django.db import models
from Users.models import Users


class ProductSubCategories_2(models.Model):
    name = models.CharField(max_length=999, verbose_name='Name')

    def __str__(self):
        return f'{self.name}'


class ProductSubCategories_1(models.Model):
    name = models.CharField(max_length=999, verbose_name='Name')
    sub_categories2 = models.ManyToManyField(ProductSubCategories_2, blank=True, verbose_name='Sub Categories 2')

    def __str__(self):
        return f'{self.name}'


class ProductMainCategories(models.Model):
    name = models.CharField(max_length=999, verbose_name='Name')
    image = models.ImageField(upload_to='ProductMainCategoriesImage', blank=True, null=True, verbose_name='Image')
    sub_categories1 = models.ManyToManyField(ProductSubCategories_1, blank=True, verbose_name='Sub Categories 1')

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(ProductMainCategories, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

class Products(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='USer')
    title = models.CharField(max_length=999,verbose_name='Title')
    slug = models.CharField(max_length=999,verbose_name='Slug')
    descriptions = models.CharField(max_length=999,verbose_name='Descriptions')
    image = models.ImageField(upload_to='Products',verbose_name='Image')
    image1 = models.ImageField(upload_to='Products',blank=True,null=True,verbose_name='Image1')
    image2 = models.ImageField(upload_to='Products',blank=True,null=True,verbose_name='Image2')
    image3 = models.ImageField(upload_to='Products',blank=True,null=True,verbose_name='Image3')
    price = models.IntegerField(default=0)
    maincategories = models.ManyToManyField(ProductMainCategories,blank=False,verbose_name='Main Category')
    subCategories1 = models.ManyToManyField(ProductSubCategories_1,blank=False,verbose_name='Sub Category 1')
    subCategories2 = models.ManyToManyField(ProductSubCategories_2,blank=False,verbose_name='Sub Category 2')
    volume = models.CharField(max_length=999,verbose_name='Volume')
    compounds = models.CharField(max_length=999,verbose_name='Compounds')
    licenseـissuer = models.CharField(max_length=999,verbose_name='License issuer')
    date = models.DateTimeField(auto_now_add=True)
    limit = models.IntegerField(default=0,blank=False,null=False,verbose_name='Limit')
    status = models.BooleanField(default=True)

    def jdate(self):
        return django_jalali(self.date)

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(Products, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class ProductsComments(models.Model):
    user = models.ForeignKey(Users,null=False, blank=False,on_delete=models.CASCADE,verbose_name='User')
    product = models.ForeignKey(Products,null=False, blank=False, on_delete=models.CASCADE,verbose_name='Prodcut Id')
    comment = models.TextField(null=False, blank=False,verbose_name='Comment')
    status = models.BooleanField(default=False, verbose_name='Status')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date')

    def user_fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return self.comment

class ProductsSliders(models.Model):
    image = models.ImageField(upload_to='ProductsSlides',verbose_name='Image')
    url = models.URLField(verbose_name='Url')

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(ProductsSliders, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.url}"





class ProductsCarts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Shoper')
    payment_date = models.DateTimeField(auto_now_add=True,blank=True,null=True, verbose_name='Payment Date')
    payment_status = models.BooleanField(default=False, verbose_name='Payment Status')

    def jdate(self):
        return django_jalali(self.payment_date)

    def __str__(self):
        return f'{self.user}'


class ProductsOrders(models.Model):
    cart = models.ForeignKey(ProductsCarts, on_delete=models.CASCADE,blank=True,null=True,verbose_name='Cart')
    shopper = models.ForeignKey(Users, on_delete=models.CASCADE,blank=True,null=True,verbose_name='shopper')
    title = models.CharField(blank=True,null=True,max_length=999, verbose_name='Title')
    description = models.TextField(blank=True,null=True,verbose_name='Description')
    price = models.IntegerField(blank=True, null=True, verbose_name='Price')
    product = models.ForeignKey(Products,on_delete=models.CASCADE,blank=False, null=False, verbose_name='Product ')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Payment Date')
    payment_status = models.BooleanField(default=False, verbose_name='Payment Status')

    def product_image(self):
        if self.product.image.url:
            return self.product.image.url
        else:
            return None

    def user_address(self):
        return self.shopper.address

    def jdate(self):
        return django_jalali(self.payment_date)

    def __str__(self):
        return f'{self.title}'



class Tiket(models.Model):
    title = models.CharField(max_length=999,verbose_name='Title')
    user = models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True,verbose_name='User',related_name='tiket_user')
    support = models.ForeignKey(Users,on_delete=models.CASCADE,null=False,blank=False,verbose_name='Support',related_name='tiket_support')
    status = models.BooleanField(default=False,verbose_name='Status')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date')

    def jdate(self):
        return django_jalali(self.date)

    def __str__(self):
        return self.title

class Messages(models.Model):
    tiket = models.ForeignKey(Tiket,on_delete=models.CASCADE,verbose_name='Tiket')
    user = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='User')
    support = models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True,verbose_name='Support',related_name='message')
    text = models.TextField(null=True,blank=True,verbose_name='Text')
    file = models.FileField(upload_to='TiketFile',blank=True,null=True,verbose_name='File')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date')
    is_suppot = models.BooleanField(default=False,verbose_name='Is Support')

    def jdate(self):
        return django_jalali(self.date)

    def status(self):
        if self.tiket.status:
            return self.tiket.status
        else:
            return None

    def __str__(self):
        return self.tiket.title



