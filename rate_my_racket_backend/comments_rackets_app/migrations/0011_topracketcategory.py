# Generated by Django 4.0.4 on 2022-04-23 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0002_remove_userprofile_id_alter_userprofile_user'),
        ('comments_rackets_app', '0010_ratingcommentvote'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopRacketCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bronze_racket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bronze_racket_set', to='comments_rackets_app.racket')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comments_rackets_app.categoryrating')),
                ('gold_racket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gold_racket_set', to='comments_rackets_app.racket')),
                ('silver_racket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='silver_racket_set', to='comments_rackets_app.racket')),
                ('userprofile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_app.userprofile')),
            ],
        ),
    ]