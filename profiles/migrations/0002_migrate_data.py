from django.db import migrations


def migrate_data(apps, schema_editor):
    # Retrieve the old models
    old_profile_model = apps.get_model('oc_lettings_site', 'Profile')

    # Retrieve the new models
    new_profile_model = apps.get_model('profiles', 'Profile')

    # Migrate profiles
    for old_profile in old_profile_model.objects.all():
        new_profile_model.objects.create(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city
        )


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(migrate_data),
    ]
