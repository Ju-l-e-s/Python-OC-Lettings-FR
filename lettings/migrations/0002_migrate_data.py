from django.db import migrations


def migrate_data(apps, schema_editor):
    # Retrieve the old models
    old_address_model = apps.get_model('oc_lettings_site', 'Address')
    old_letting_model = apps.get_model('oc_lettings_site', 'Letting')

    # Retrieve the new models
    new_address_model = apps.get_model('lettings', 'Address')
    new_letting_model = apps.get_model('lettings', 'Letting')

    # Migrate addresses
    for old_address in old_address_model.objects.all():
        new_address = new_address_model.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code
        )

    # Migrate lettings
    for old_letting in old_letting_model.objects.all():
        # Find the corresponding address in the new data
        new_address = new_address_model.objects.get(
            number=old_letting.address.number,
            street=old_letting.address.street,
            city=old_letting.address.city
        )
        new_letting_model.objects.create(
            title=old_letting.title,
            address=new_address
        )


class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(migrate_data),
    ]
