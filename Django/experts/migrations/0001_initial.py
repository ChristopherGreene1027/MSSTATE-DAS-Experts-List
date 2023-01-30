# Generated by Django 4.1.1 on 2022-09-20 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expert_Name', models.TextField()),
                ('expert_Picture', models.ImageField(upload_to='')),
                ('expert_Field', models.TextField()),
                ('expert_College', models.CharField(choices=[('ARTSSCIENCE', 'Arts and Sciences'), ('AGRICULTURELIFESCIENCE', 'Agriculture and Life Sciences'), ('ARCHITECHTUREARTDESIGN', 'Architechture, Art and Design'), ('BUSINESS', 'Business'), ('EDUCATION', 'Education'), ('FORESTRESOURCES', 'Forest Resources'), ('VETERINARYMEDICINE', 'Veterninary Medicine'), ('ENGINEERING', 'James Worth Bagley College of Engineering'), ('HONORS', 'Shackouls Honors College')], max_length=22)),
                ('expert_Phone', models.IntegerField()),
                ('expert_Email', models.EmailField(max_length=254)),
                ('expert_Topics', models.TextField()),
                ('expert_Achievements', models.TextField()),
            ],
        ),
    ]