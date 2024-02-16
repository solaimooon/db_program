
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Affordability(models.Model):
    id_affordability = models.IntegerField(db_column='id affordability',
                                           primary_key=True)  # Field renamed to remove unsuitable characters.
    job = models.CharField(max_length=45, blank=True, null=True)
    marital_status = models.CharField(db_column='marital status', max_length=1, blank=True,
                                      null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'affordability'


class Users(models.Model):
    idusers = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    user_name = models.CharField(db_column='user name', max_length=45, blank=True,
                                 null=True)  # Field renamed to remove unsuitable characters.
    national_code = models.CharField(db_column='national Code', max_length=45, blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    status = models.IntegerField(blank=True, null=True)
    financial_situation = models.IntegerField(db_column='financial situation', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters.
    membership_type = models.CharField(max_length=7)
    image = models.CharField(max_length=100)
    representative = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    affordability_id_affordability = models.ForeignKey(Affordability, db_column='affordability_id affordability',
                                                       on_delete=models.DO_NOTHING)  # Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'users'


class Adress(models.Model):
    id_adress = models.AutoField(primary_key=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    number_fo_region = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=15, blank=True, null=True)
    detail_adress = models.CharField(max_length=45, blank=True, null=True)
    idusers = models.ForeignKey('Users', models.DO_NOTHING, db_column='idusers')

    class Meta:
        db_table = 'adress'


class Affordability(models.Model):
    id_affordability = models.IntegerField(db_column='id affordability',
                                           primary_key=True)  # Field renamed to remove unsuitable characters.
    job = models.CharField(max_length=45, blank=True, null=True)
    marital_status = models.CharField(db_column='marital status', max_length=1, blank=True,
                                      null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'affordability'


class Phone(models.Model):
    id_phone = models.AutoField(primary_key=True)
    number = models.CharField(max_length=45)
    identity = models.CharField(max_length=45, blank=True, null=True)
    pkuser = models.ForeignKey('Users', models.DO_NOTHING, db_column='pkuser', blank=True, null=True)

    class Meta:
        db_table = 'phone'


class Point(models.Model):
    id_point = models.AutoField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    monasebat = models.CharField(max_length=45, blank=True, null=True)
    pointcol = models.CharField(max_length=45, blank=True, null=True)
    users_idusers = models.ForeignKey('Users', models.DO_NOTHING, db_column='users_idusers')

    class Meta:
        db_table = 'point'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'django_session'








