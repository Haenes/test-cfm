import datetime
from django.forms import ModelForm, DateInput

from .models import (
    Operation,
    OperationStatus,
    OperationType,
    OperationCategory,
    OperationSubCategory
)


class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = [
            'created_at',
            'status',
            'type',
            'category',
            'subcategory',
            'total',
            'comment'
        ]

        widgets = {
            'created_at': DateInput(attrs={
                'type': 'date',
                'value': datetime.date.today()
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # if not self.instance.pk:
        #     self.fields['category'].queryset = OperationCategory.objects.none()
        #     self.fields['subcategory'].queryset = OperationSubCategory.objects.none()

        # Возникает проблема с валидацией из-за того,
        # что опций выбора категорий и подкатегорий
        # нет при рендере формы.
        # При чём, при изменении уже существующей операции - проблем нет...
        # Но код ниже помогает эту проблему обойти.

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = OperationCategory.objects.filter(
                    type_id=type_id
                )
            except (ValueError, TypeError):
                pass  # ignore invalid input and fallback to empty queryset


class StatusForm(ModelForm):
    class Meta:
        model = OperationStatus
        fields = ['status_name']


class TypeForm(ModelForm):
    class Meta:
        model = OperationType
        fields = ['type_name']


class CategoryForm(ModelForm):
    class Meta:
        model = OperationCategory
        fields = ['type', 'category_name']


class SubCategoryForm(ModelForm):
    class Meta:
        model = OperationSubCategory
        fields = ['category', 'subcategory_name']
