from django.contrib import admin


class WebAppAdmin(admin.ModelAdmin):

   @staticmethod
   def released_year(obj):
      return obj.released.year

   @staticmethod
   def cleanup_description(modeladmin, request, queryset):
      queryset.update(description=None)

   ordering = ['id']
   list_display = ['id', 'username', 'ranking']
   list_display_links = ['id', 'username']
   list_per_page = 20
   list_filter = ['username']
   search_fields = ['username']
   fieldsets = [
      (None, {'fields': ['username', 'created']}),
   ]
   readonly_fields = ['created']