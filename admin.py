from django.contrib import admin
from django_site_googleanalytics.models import GoogleAnalytics
from django.contrib.sites.admin import Site

class DjangoSiteGoogleAnalyticsInline(admin.TabularInline):
    model = GoogleAnalytics

class SiteAdmin(admin.ModelAdmin):
    inlines = [DjangoSiteGoogleAnalyticsInline]

admin.site.unregister(Site)
admin.site.register(Site, SiteAdmin)