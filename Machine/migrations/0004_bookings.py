# Generated by Django 3.2.6 on 2021-10-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Machine', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Artist', models.CharField(max_length=100)),
                ('Event', models.CharField(blank=True, choices=[('Festival', 'Festival'), ('Mini Tour', 'Mini Tour'), ('Corporate Event', 'Corporate Event'), ('Club Performance', 'Club Performance'), ('Paid Appearence', 'Paid Appearence')], max_length=100, null=True)),
                ('Name_of_Event', models.CharField(max_length=100)),
                ('Date', models.DateField(max_length=100)),
                ('Time_Slot', models.TimeField()),
                ('Set_Time', models.IntegerField()),
                ('Country', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Venue', models.CharField(max_length=100)),
                ('Promoter', models.CharField(max_length=100)),
                ('Promoter_Email', models.EmailField(max_length=100)),
            ],
        ),
    ]
