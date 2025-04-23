from django.db import migrations


def add_users(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(
            owners_name=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_number=flat.owner_pure_number,
        )
        owner.owners_flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_owner'),
    ]

    operations = [
        migrations.RunPython(add_users)
    ]
