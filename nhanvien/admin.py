from django.contrib import admin

# Register your models here.

from nhanvien.views import nhanvien
from nhanvien.models import ThemMoiNV

# Register your models here.

class NhanVienAdmin(admin.ModelAdmin):
    list_display = ('ten', 'chucvu', 'namsinh')
    list_display_links=('ten', 'chucvu', 'namsinh')
    list_filter=('ten', 'chucvu', 'namsinh')
    search_fields=('ten', 'chucvu', 'namsinh')
    list_per_page=20

admin.site.register(ThemMoiNV, NhanVienAdmin)