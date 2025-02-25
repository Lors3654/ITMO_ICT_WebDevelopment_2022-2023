# Generated by Django 4.1.3 on 2022-12-03 16:25

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField(auto_now=True)),
                ('check_out', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cleaners',
            fields=[
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('passport', models.CharField(max_length=10, unique=True)),
                ('cleaner_id', models.IntegerField(primary_key=True, serialize=False)),
                ('salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('passport', models.CharField(max_length=10, unique=True)),
                ('city', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='Check-in date')),
                ('number', models.IntegerField(verbose_name='Hotel number')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('single', 'single'), ('double', 'double'), ('triple', 'triple')], default='-', max_length=10, null=True, verbose_name='Type room')),
                ('number', models.IntegerField(unique=True)),
                ('phone', models.CharField(max_length=15, verbose_name='Phone number')),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('+', 'Available'), ('-', 'Occupied')], default='-', max_length=1, null=True, verbose_name='Status room')),
                ('cleaners', models.ManyToManyField(through='hotel_app.Cleaning', to='hotel_app.cleaners')),
                ('guest_in', models.ManyToManyField(through='hotel_app.Booking', to='hotel_app.guest', verbose_name='Guest')),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='room_book',
            field=models.ManyToManyField(related_name='guests', through='hotel_app.Booking', to='hotel_app.room'),
        ),
        migrations.AddField(
            model_name='cleaning',
            name='clean_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cleaning', to='hotel_app.room'),
        ),
        migrations.AddField(
            model_name='cleaning',
            name='cleaner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cleaning', to='hotel_app.cleaners'),
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_app.guest'),
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_app.room'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
