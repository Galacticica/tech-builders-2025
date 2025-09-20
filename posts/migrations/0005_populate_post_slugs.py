from django.db import migrations
from django.utils.text import slugify


def gen_unique_slug(title, existing_slugs):
    base_slug = slugify(title) or "post"
    slug = base_slug
    counter = 1
    while slug in existing_slugs:
        slug = f"{base_slug}-{counter}"
        counter += 1
    existing_slugs.add(slug)
    return slug


def populate_slugs(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')
    existing_slugs = set(Post.objects.exclude(slug='').values_list('slug', flat=True))
    for post in Post.objects.filter(slug=''):
        post.slug = gen_unique_slug(post.title, existing_slugs)
        post.save(update_fields=['slug'])


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0004_post_post_type_post_slug_alter_media_url'),
    ]

    operations = [
        migrations.RunPython(populate_slugs, reverse_code=migrations.RunPython.noop),
    ]
