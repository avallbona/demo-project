from django.contrib import admin

from .models import Artist, Calification, Portfolio


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', )


class CalificationInline(admin.TabularInline):
    model = Calification


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [CalificationInline, ]
