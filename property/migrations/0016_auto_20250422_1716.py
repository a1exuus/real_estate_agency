from django.db import migrations
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()

    for flat in flats:
        try:
            parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
            if phonenumbers.is_valid_number(parsed_number):
                flat.owner_pure_number = parsed_number
                flat.save()
        except phonenumbers.NumberParseException:
            continue


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('property', '0015_flat_owner_pure_number_alter_flat_owners_phonenumber'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers)
    ]
