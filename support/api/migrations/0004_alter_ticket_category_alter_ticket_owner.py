# Generated by Django 4.0.4 on 2022-05-15 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_alter_ticket_category_alter_ticket_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='api.categories'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]