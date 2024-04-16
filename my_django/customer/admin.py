from django.contrib import admin
from django.http import HttpResponse
from .models import Cart, Category, Product,CartItem
import pandas as pd


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'name', 'price','supplier')  # Hiển thị các trường 'id' và 'name' trong danh sách
    search_fields = ('name','price','id')  # Cho phép tìm kiếm theo trường 'name'
    actions = ['export_to_excel']

    def export_to_excel(self, request, queryset):
        # Truy vấn dữ liệu từ cơ sở dữ liệu
        data = queryset.values()

        # Chuyển đổi dữ liệu thành DataFrame
        df = pd.DataFrame.from_records(data)

        # Tạo một phản hồi HTTP để xuất tệp Excel
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Book1.xlsx"'

        # Xuất dữ liệu DataFrame sang tệp Excel
        df.to_excel(response, index=False)

        return response
    
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')
     search_firlds = ('id', 'name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category,CategoryAdmin)