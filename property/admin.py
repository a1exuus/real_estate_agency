from django.contrib import admin

from .models import Flat, Report, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'construction_year', 'new_building', 'town', 'owners_phonenumber', 'owner_pure_number']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('liked_by',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ('reporter', 'reported_flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owners_flats',)