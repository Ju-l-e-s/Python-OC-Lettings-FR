# profiles/migrations/0002_fix_table_names.py
from django.db import migrations


def rename_if_needed(apps, schema_editor):
    conn = schema_editor.connection
    existing = set(conn.introspection.table_names())

    Profile = apps.get_model("profiles", "Profile")

    if "oc_lettings_site_profile" in existing:
        if "profiles_profile" in existing and not Profile.objects.exists():
            schema_editor.delete_model(Profile)
            # Refresh the table list after deletion
            existing = set(conn.introspection.table_names())
        if "profiles_profile" not in existing:
            schema_editor.alter_db_table(Profile, "oc_lettings_site_profile", "profiles_profile")


class Migration(migrations.Migration):
    dependencies = [("profiles", "0001_initial")]
    operations = [
        migrations.RunPython(rename_if_needed, reverse_code=migrations.RunPython.noop),
        migrations.AlterModelTable(name="profile", table=None),
    ]
