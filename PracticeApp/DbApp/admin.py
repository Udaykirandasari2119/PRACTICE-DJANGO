from django.contrib import admin
from.models import Employee,Department,DupEmployee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empno','empname','salary','grade']
    list_filter=['salary','empname']
    list_editable=['empname']
    list_per_page=2
    #ordering=['empno']

    def grade(self,obj):
        if obj.salary>4000:
            return 'high'
        elif obj.salary>3000:
            return 'average'
        else:
            return 'low'

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department)
admin.site.register(DupEmployee,EmployeeAdmin) 