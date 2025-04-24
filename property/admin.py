from django.contrib import admin

from .models import Flat, Report, Owner


class FlatInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields = ('owner', 'flat')


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [
        FlatInline,
    ]
    exclude = ['owned_by']
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'construction_year', 'new_building', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ('liked_by',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ('reporter', 'reported_flat')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owners_flats',)