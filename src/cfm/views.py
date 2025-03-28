from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import (
    Operation,
    OperationStatus,
    OperationType,
    OperationCategory,
    OperationSubCategory
)
from .forms import OperationForm, StatusForm, TypeForm, CategoryForm, SubCategoryForm


class ListOperation(LoginRequiredMixin, ListView):
    model = Operation
    template_name = 'operation/operations.html'
    context_object_name = 'operations'


# class CreateOperation(View):
#     def get(self, request):
#         # statuses = OperationStatus.objects.filter(user=1)
#         # types = OperationType.objects.filter(user=1)
#         # categories = OperationCategory.objects.filter(user=1)
#         # subcategories = OperationSubCategory.objects.filter(user=1)

#         # context = {
#         #     'statuses': statuses,
#         #     'types': types,
#         #     'categories': categories,
#         #     'subcategories': subcategories
#         # }
#         # return render(request, 'new_operation.html', context)

#         form = OperationForm()
#         form.fields['category'].queryset = OperationCategory.objects.none()
#         form.fields['subcategory'].queryset = OperationSubCategory.objects.none()

#         return render(request, 'new_operation.html', {'form': form})

#     def post(self, request):
#         form = OperationForm(request.POST)

#         if form.is_valid():
#             print(form.cleaned_data)
#             pass

class CreateOperation(LoginRequiredMixin, CreateView):
    model = Operation
    form_class = OperationForm
    template_name = 'operation/add_operation.html'

    def form_invalid(self, form):
        print(form.data)
        return super().form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditOperation(LoginRequiredMixin, UpdateView):
    model = Operation
    form_class = OperationForm
    template_name = 'operation/edit_operation.html'
    context_object_name = 'operation'


def delete_operation(request, pk):
    operation = get_object_or_404(Operation, pk=pk)
    operation.delete()
    return redirect('cfm:operations')


class Handbook(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'handbook/handbook.html')


class ListStatus(LoginRequiredMixin, ListView):
    template_name = 'handbook/status/statuses.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return OperationStatus.objects.filter(user_id__in=[1, self.request.user.id])


class CreateStatus(LoginRequiredMixin, CreateView):
    model = OperationStatus
    form_class = StatusForm
    template_name = 'handbook/status/add_status.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditStatus(LoginRequiredMixin, UpdateView):
    model = OperationStatus
    form_class = StatusForm
    template_name = 'handbook/status/edit_status.html'
    context_object_name = 'status'


def delete_status(request, pk):
    operation_status = get_object_or_404(OperationStatus, pk=pk)
    operation_status.delete()
    return redirect('cfm:statuses')


class ListType(LoginRequiredMixin, ListView):
    template_name = 'handbook/type/types.html'
    context_object_name = 'types'

    def get_queryset(self):
        return OperationType.objects.filter(user_id__in=[1, self.request.user.id])


class CreateType(LoginRequiredMixin, CreateView):
    model = OperationType
    form_class = TypeForm
    template_name = 'handbook/type/add_type.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditType(LoginRequiredMixin, UpdateView):
    model = OperationType
    form_class = TypeForm
    template_name = 'handbook/type/edit_type.html'
    context_object_name = 'type'


def delete_type(request, pk):
    operation_type = get_object_or_404(OperationType, pk=pk)
    operation_type.delete()
    return redirect('cfm:types')


class ListCategory(LoginRequiredMixin, ListView):
    template_name = 'handbook/category/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return OperationCategory.objects.filter(user_id__in=[1, self.request.user.id])


class CreateCategory(LoginRequiredMixin, CreateView):
    model = OperationCategory
    form_class = CategoryForm
    template_name = 'handbook/category/add_category.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditCategory(LoginRequiredMixin, UpdateView):
    model = OperationCategory
    form_class = CategoryForm
    template_name = 'handbook/category/edit_category.html'
    context_object_name = 'category'


def delete_category(request, pk):
    operation_category = get_object_or_404(OperationCategory, pk=pk)
    operation_category.delete()
    return redirect('cfm:categories')


class ListSubCategory(LoginRequiredMixin, ListView):
    template_name = 'handbook/subcategory/subcategories.html'
    context_object_name = 'subcategories'

    def get_queryset(self):
        return OperationSubCategory.objects.filter(
            user_id__in=[1, self.request.user.id]
        )


class CreateSubCategory(LoginRequiredMixin, CreateView):
    model = OperationSubCategory
    form_class = SubCategoryForm
    template_name = 'handbook/subcategory/add_subcategory.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditSubCategory(LoginRequiredMixin, UpdateView):
    model = OperationSubCategory
    form_class = SubCategoryForm
    template_name = 'handbook/subcategory/edit_subcategory.html'
    context_object_name = 'subcategory'


def delete_subcategory(request, pk):
    operation_subcategory = get_object_or_404(OperationSubCategory, pk=pk)
    operation_subcategory.delete()
    return redirect('cfm:subcategories')


def load_categories(request):
    type_id = request.GET.get('type')
    categories = OperationCategory.objects.filter(type_id=type_id)
    return render(
        request=request,
        template_name='dropdowns/categories-dropdown.html',
        context={'categories': categories}
    )


def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = OperationSubCategory.objects.filter(category_id=category_id)

    return render(
        request=request,
        template_name='dropdowns/subcategories-dropdown.html',
        context={'subcategories': subcategories}
    )
