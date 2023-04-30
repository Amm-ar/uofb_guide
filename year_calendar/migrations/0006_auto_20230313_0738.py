# Generated by Django 3.2.14 on 2023-03-13 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('year_calendar', '0005_auto_20230312_2116'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventCancellations',
        ),
        migrations.AlterField(
            model_name='event',
            name='year_tag',
            field=models.CharField(choices=[('2016/2017', '2016/2017'), ('2017/2018', '2017/2018'), ('2018/2019', '2018/2019'), ('2019/2020', '2019/2020'), ('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023'), ('2023/2024', '2023/2024')], max_length=50, verbose_name='Year Tag'),
        ),
    ]
