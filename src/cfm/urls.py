from django.urls import path

from .views import (
    ListOperation,
    CreateOperation,
    EditOperation,
    delete_operation,

    Handbook,

    ListStatus,
    CreateStatus,
    EditStatus,
    delete_status,

    ListType,
    CreateType,
    EditType,
    delete_type,

    ListCategory,
    CreateCategory,
    EditCategory,
    delete_category,

    ListSubCategory,
    CreateSubCategory,
    EditSubCategory,
    delete_subcategory,

    load_categories,
    load_subcategories
)


app_name = 'cfm'
urlpatterns = [
    path('operations/', ListOperation.as_view(), name='operations'),
    path('operations/add/', CreateOperation.as_view(), name='add_operation'),
    path('operations/<int:pk>/', EditOperation.as_view(), name='edit_operation'),
    path('operations/<int:pk>/delete/', delete_operation, name='delete_operation'),

    path('handbook/', Handbook.as_view(), name='handbook'),

    path('handbook/types/', ListType.as_view(), name='types'),
    path('handbook/types/add/', CreateType.as_view(), name='add_type'),
    path('handbook/types/<int:pk>/', EditType.as_view(), name='edit_type'),
    path('handbook/types/<int:pk>/delete/', delete_type, name='delete_type'),

    path('handbook/statuses/', ListStatus.as_view(), name='statuses'),
    path('handbook/status/add/', CreateStatus.as_view(), name='add_status'),
    path('handbook/status/<int:pk>/', EditStatus.as_view(), name='edit_status'),
    path('handbook/status/<int:pk>/delete/', delete_status, name='delete_status'),

    path('handbook/categories/', ListCategory.as_view(), name='categories'),
    path('handbook/category/add/', CreateCategory.as_view(), name='add_category'),
    path('handbook/category/<int:pk>/', EditCategory.as_view(), name='edit_category'),
    path('handbook/category/<int:pk>/delete/', delete_category, name='delete_category'),

    path('handbook/subcategories/', ListSubCategory.as_view(), name='subcategories'),
    path(
        route='handbook/subcategory/add/',
        view=CreateSubCategory.as_view(),
        name='add_subcategory'
    ),
    path(
        route='handbook/subcategory/<int:pk>/',
        view=EditSubCategory.as_view(),
        name='edit_subcategory'
    ),
    path(
        route='handbook/subcategory/<int:pk>/delete/',
        view=delete_subcategory,
        name='delete_subcategory'
    ),

    path('fetch-categories/', load_categories, name='fetch_categories'),
    path('fetch-subcategories/', load_subcategories, name='fetch_subcategories')
]
