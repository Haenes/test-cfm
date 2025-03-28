from django.contrib import admin

from .models import (
    Operation,
    OperationStatus,
    OperationType,
    OperationCategory,
    OperationSubCategory
)


admin.site.register([
    Operation,
    OperationStatus,
    OperationType,
    OperationCategory,
    OperationSubCategory
])
