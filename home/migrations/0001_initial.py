# Generated by Django 4.0.3 on 2022-03-20 12:40

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('home_title', models.CharField(max_length=100, null=True)),
                ('content', wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='title', max_length=100, required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='the text content goes here', required=True))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=20, required=True))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
