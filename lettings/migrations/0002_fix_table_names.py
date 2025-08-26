from django.db import migrations


def rename_if_needed(apps, schema_editor):
    conn = schema_editor.connection
    existing = set(conn.introspection.table_names())

    Address = apps.get_model("lettings", "Address")
    Letting = apps.get_model("lettings", "Letting")

    # --- Address ---
    if "oc_lettings_site_address" in existing:
        # If the "new" table exists but is empty, delete it to free up the name.
        if "lettings_address" in existing and not Address.objects.exists():
            schema_editor.delete_model(Address)
            # Refresh the table list after deletion
            existing = set(conn.introspection.table_names())
        # Then rename the old -> new if needed.
        if "lettings_address" not in existing:
            schema_editor.alter_db_table(Address, "oc_lettings_site_address", "lettings_address")

    # --- Letting ---
    # Recompute existing tables before handling letting
    existing = set(conn.introspection.table_names())
    if "oc_lettings_site_letting" in existing:
        if "lettings_letting" in existing and not Letting.objects.exists():
            schema_editor.delete_model(Letting)
            # Refresh after deletion
            existing = set(conn.introspection.table_names())
        if "lettings_letting" not in existing:
            schema_editor.alter_db_table(Letting, "oc_lettings_site_letting", "lettings_letting")


class Migration(migrations.Migration):
    dependencies = [("lettings", "0001_initial")]
    operations = [
        migrations.RunPython(rename_if_needed, reverse_code=migrations.RunPython.noop),
        migrations.AlterModelTable(name="address", table=None),
        migrations.AlterModelTable(name="letting", table=None),
    ]
