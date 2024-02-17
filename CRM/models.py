from django.db import models
from django.utils.html import mark_safe
from django_jalali.db import models as jmodels

class marital_status (models.Model):
    status= models.CharField(max_length=15)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name="وضعیت تاهل"
        verbose_name_plural="وضعیت تاهل"



class level_of_life(models.Model):
    neme=models.CharField(max_length=15,verbose_name='درجه مالی')

    def __str__(self):
        return self.neme
    class Meta:
        verbose_name="توان مالی"
        verbose_name_plural="توان مالی"



class membership_type(models.Model):
    name=models.CharField(max_length=20,verbose_name="نوع عضویت")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="نوع عضویت"
        verbose_name_plural="نوع عضویت"

class Users(models.Model):
    first_name = models.CharField(max_length=45,verbose_name='نام')
    last_name = models.CharField(max_length=45,verbose_name='خانوادگی')
    user_name = models.CharField( max_length=45, blank=True,null=True,verbose_name='کد عضویت')
    national_code = models.CharField( max_length=45, blank=True,null=True,verbose_name='کدملی')
    membership_type = models.ForeignKey(membership_type,on_delete=models.DO_NOTHING,verbose_name='نوع عضویت')
    image = models.ImageField(upload_to='picture/',verbose_name="عکس",blank=True)
    representative = models.ForeignKey('Users',blank=True, null=True,on_delete=models.CASCADE,verbose_name="معرف")
    age = models.IntegerField(blank=True, null=True,verbose_name="سن")
    join_at=jmodels.jDateField(auto_now_add=True,verbose_name="تاریخ عضویت")
    job = models.CharField(max_length=45, blank=True, null=True, verbose_name='شغل')
    marital_status = models.ForeignKey(marital_status, blank=True, null=True, verbose_name='وضعیت تاهل',
                                       on_delete=models.SET_NULL)
    level_of_life = models.ForeignKey(level_of_life, on_delete=models.SET_NULL, null=True, verbose_name='توان مالی',blank=True)
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def نام(self):
        return "{} {}".format(self.first_name,self.last_name)

    class Meta:
        verbose_name="جدول اعضا"
        verbose_name_plural="جدول اعضا"



class Adress(models.Model):
    city = models.CharField(max_length=15, blank=True, null=True,verbose_name="شهر")
    number_of_region = models.IntegerField(blank=True, null=True,verbose_name="منطقه")
    street = models.CharField(max_length=15, blank=True, null=True,verbose_name="خیابان")
    detail_adress = models.CharField(max_length=45, blank=True, null=True,verbose_name="ادرس کامل")
    idusers = models.ForeignKey('Users', models.DO_NOTHING, db_column='idusers',verbose_name="عضو")

    class Meta:
        verbose_name="ادرس"
        verbose_name_plural="ادرس ها "



class Phone(models.Model):
    number = models.CharField(max_length=45,verbose_name="تلفن")
    identity = models.CharField(max_length=45, blank=True, null=True,verbose_name="مالکیت")
    pkuser = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True,verbose_name="عضو")

    class Meta:
        verbose_name="تلفن"
        verbose_name_plural="تلفن ها"


class Point(models.Model):
    price = models.IntegerField(blank=True, null=True,verbose_name="امتیاز")
    date = models.DateField(blank=True, null=True,verbose_name="تاریخ")
    monasebat = models.CharField(max_length=45, blank=True, null=True,verbose_name="مناسبت")
    users_idusers = models.ForeignKey('Users', on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name="امتیاز"
        verbose_name_plural="امتیاز ها"

