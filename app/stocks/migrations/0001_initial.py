from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='BuyingStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(choices=[('USER1', 'user1'), ('USER2', 'user2')], max_length=100, verbose_name='user')),
                ('stock', models.CharField(choices=[('STOCK1', 'stock1'), ('STOCK2', 'stock2'), ('STOCK3', 'stock3')], max_length=100, verbose_name='stock')),
                ('status', models.CharField(choices=[('DENY', 'Deny'), ('ACCEPTED', 'Accepted')], max_length=8, verbose_name='status')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity')),
            ],
        )
    ]
