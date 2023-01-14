# Generated by Django 4.1 on 2022-10-10 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_group"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orgs", "0009_auto_20220903_1256"),
    ]

    operations = [
        migrations.CreateModel(
            name="AppInstallationLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "item",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="link",
                        to="apps.appinstallation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AppLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "item",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="link",
                        to="apps.app",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BatchOperationLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "item",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="link",
                        to="data.batchoperation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DataTemplateLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "item",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="link",
                        to="data.datatemplate",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="organization",
            name="apps",
            field=models.ManyToManyField(
                related_name="org", through="orgs.AppLink", to="apps.app"
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="batch_operations",
            field=models.ManyToManyField(
                related_name="org",
                through="orgs.BatchOperationLink",
                to="data.batchoperation",
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="data_templates",
            field=models.ManyToManyField(
                related_name="org",
                through="orgs.DataTemplateLink",
                to="data.datatemplate",
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="installations",
            field=models.ManyToManyField(
                related_name="org",
                through="orgs.AppInstallationLink",
                to="apps.appinstallation",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="users",
            field=models.ManyToManyField(
                related_name="%(app_label)s_%(class)s",
                through="orgs.OrganizationUser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="organizationinvitation",
            name="invited_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_sent_invitations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="organizationinvitation",
            name="invitee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_invitations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="organizationuser",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="datatemplatelink",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="data_template_links",
                to="orgs.organization",
            ),
        ),
        migrations.AddField(
            model_name="batchoperationlink",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="batch_operation_links",
                to="orgs.organization",
            ),
        ),
        migrations.AddField(
            model_name="applink",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="app_links",
                to="orgs.organization",
            ),
        ),
        migrations.AddField(
            model_name="appinstallationlink",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="app_installation_links",
                to="orgs.organization",
            ),
        ),
    ]
