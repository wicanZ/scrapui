from django.contrib import admin

from scrapui.models import ScrapItem ,MultiScrapImage
# Register your models here.

class MultiSImage( admin.StackedInline ) : # TabularInline
    model = MultiScrapImage
    extra = 1
    show_change_link = True

@admin.register( ScrapItem  )
class ScrapAdmin( admin.ModelAdmin ) :
    inlines = [MultiSImage]
    class Meta :
        model = ScrapItem
