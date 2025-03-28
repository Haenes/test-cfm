from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


LENGTH_VALIDATOR = MinLengthValidator(2, 'Минимальная длина - 2 символа.')
USER_TABLE = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Operation(models.Model):
    user = USER_TABLE
    status = models.ForeignKey('OperationStatus', on_delete=models.CASCADE)
    type = models.ForeignKey('OperationType', on_delete=models.CASCADE)
    category = models.ForeignKey('OperationCategory', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('OperationSubCategory', on_delete=models.CASCADE)
    total = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateField()

    class Meta:
        ordering = ['-created_at', 'total']
        constraints = [
            models.CheckConstraint(
                condition=models.Q(total__gt=0),
                name='total_gt_0'
            ),
        ]

    def get_absolute_url(self):
        return reverse('cfm:edit_operation', kwargs={"pk": self.pk})

    def __str__(self):
        return (
            f'{self.created_at} {self.status} {self.type} {self.category} '
            f'{self.subcategory} {self.total} '
        )


class OperationStatus(models.Model):
    user = USER_TABLE
    status_name = models.CharField(
        max_length=50,
        unique=True,
        validators=[LENGTH_VALIDATOR]
    )

    class Meta:
        db_table = 'cfm_operation_status'
        verbose_name_plural = 'operation statuses'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'status_name'],
                name='unique_status_name_per_user',
                violation_error_message='Такой статус уже существует!'
            ),
            # Добавить проверку, чтобы юзер не мог создать
            # те же статусы, что изначально уже есть?
            # models.CheckConstraint(
            #     condition=models.Q(type_name__not_in=['Бизнес', 'Личное', 'Налог']),
            #     name='status_name_not_the_initial'
            # )
        ]

    def get_absolute_url(self):
        return reverse('cfm:edit_status', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.status_name}'


class OperationType(models.Model):
    user = USER_TABLE
    type_name = models.CharField(max_length=50, validators=[LENGTH_VALIDATOR])

    class Meta:
        db_table = 'cfm_operation_type'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'type_name'],
                name='unique_type_name_per_user',
                violation_error_message='Такой тип уже существует!'
            ),
            # Добавить проверку, чтобы юзер не мог создать
            # те же типы, что изначально уже есть?
            # models.CheckConstraint(
            #     condition=models.Q(type_name__not_in=['Пополнение', 'Списание']),
            #     name='type_name_not_the_initial'
            # )
        ]

    def get_absolute_url(self):
        return reverse('cfm:edit_type', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.type_name}'


class OperationCategory(models.Model):
    user = USER_TABLE
    type = models.ForeignKey(OperationType, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=50, validators=[LENGTH_VALIDATOR])

    class Meta:
        db_table = 'cfm_operation_category'
        verbose_name_plural = 'operation categories'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'type', 'category_name'],
                name='unique_type_and_category_per_user',
                violation_error_message='Такая связка уже существует!'
            ),
        ]

    def get_absolute_url(self):
        return reverse('cfm:edit_category', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.category_name}'


class OperationSubCategory(models.Model):
    user = USER_TABLE
    category = models.ForeignKey(OperationCategory, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=50, validators=[LENGTH_VALIDATOR])

    class Meta:
        db_table = 'cfm_operation_subcategory'
        verbose_name_plural = 'operation subcategories'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'category', 'subcategory_name'],
                name='unique_category_and_subcategory_per_user',
                violation_error_message='Такая связка уже существует!'
            ),
        ]

    def get_absolute_url(self):
        return reverse('cfm:edit_subcategory', kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.subcategory_name}'
