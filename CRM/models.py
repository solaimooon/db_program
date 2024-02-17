from django.db import models


class marital_status (models.Model):
    status= models.CharField(max_length=15)


class level_of_life(models.Model):
    neme=models.CharField(max_length=15)


class Affordability(models.Model):
    job = models.CharField(max_length=45, blank=True, null=True,verbose_name='شغل')
    marital_status = models.ForeignKey(marital_status, blank=True, null=True,verbose_name='وضعیت مالی',on_delete=models.SET_NULL)  # Field renamed to remove unsuitable characters.
    level_of_life=models.ForeignKey(level_of_life,on_delete=models.SET_NULL,null=True)


class membership_type(models.Model):
    name=models.CharField(max_length=15)


class Users(models.Model):
    first_name = models.CharField(max_length=45,verbose_name='نام')
    last_name = models.CharField(max_length=45,verbose_name='خانوادگی')
    user_name = models.CharField( max_length=45, blank=True,null=True,verbose_name='کد عضویت')
    national_code = models.CharField( max_length=45, blank=True,null=True,verbose_name='کدملی')
    status = models.IntegerField(blank=True, null=True,verbose_name='ایا فعاله؟')
    financial_situation = models.IntegerField(blank=True,null=True)
    membership_type = models.ForeignKey(membership_type,on_delete=models.DO_NOTHING,verbose_name='نوع فعالیت')
    image = models.CharField(max_length=100)
    representative = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    join_at=models.DateField(auto_now_add=True)
    affordability=models.ForeignKey(Affordability,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Adress(models.Model):
    city = models.CharField(max_length=15, blank=True, null=True)
    number_of_region = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=15, blank=True, null=True)
    detail_adress = models.CharField(max_length=45, blank=True, null=True)
    idusers = models.ForeignKey('Users', models.DO_NOTHING, db_column='idusers')


class Phone(models.Model):
    number = models.CharField(max_length=45)
    identity = models.CharField(max_length=45, blank=True, null=True)
    pkuser = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)


class Point(models.Model):
    price = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    monasebat = models.CharField(max_length=45, blank=True, null=True)
    pointcol = models.CharField(max_length=45, blank=True, null=True)
    users_idusers = models.ForeignKey('Users', models.DO_NOTHING)

