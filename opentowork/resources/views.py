
from django.shortcuts import render, redirect, get_object_or_404
from .models import Section, Category, Subcategory, Resource
from .forms import ResourceForm, CategoryForm, SubcategoryForm, SectionForm
from django.contrib import messages
from django.core.paginator import Paginator #Importando paginator para manejar la paginacion de resources


#Manejo de Recursos

def resource_list(request):
    # Obteniendo todos los Recursos
    resources = Resource.objects.all()

    # Filtros opcionales
    section_id = request.GET.get('section')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Aplicar filtros si están presentes
    if section_id:
        resources = resources.filter(section_id=section_id)
    if category_id:
        resources = resources.filter(category_id=category_id)
    if subcategory_id:
        resources = resources.filter(subcategories__id=subcategory_id)
    if min_price:
        resources = resources.filter(price__gte=min_price)
    if max_price:
        resources = resources.filter(price__lte=max_price)

    # Paginación
    paginator = Paginator(resources, 5)  # Muestra 5 recursos por página
    page_number = request.GET.get('page')  # Obtén el número de página de la solicitud
    page_obj = paginator.get_page(page_number)  # Obtén los objetos de la página

    # Obtener las secciones, categorías y subcategorías para los filtros
    sections = Section.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    # Pasar los filtros seleccionados al contexto para mantener el estado en el formulario
    context = {
        'page_obj': page_obj,
        'sections': sections,
        'categories': categories,
        'subcategories': subcategories,
        'selected_section': section_id,
        'selected_category': category_id,
        'selected_subcategory': subcategory_id,
        'min_price': min_price,
        'max_price': max_price,
    }

    return render(request, 'resources/resource_list.html', context)
    

def resource_detail(request, resource_id):
    resource = get_object_or_404(resource, id=resource_id)
    return render(request, 'resources/resource_detail.html', {'resource': resource})


def resource_create(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'resources/resource_form.html', {'form': form})

def resource_edit(request,pk):
    resource = get_object_or_404(resource, pk=pk)
    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm(instance=resource)
    return render(request, 'resources/resource_form.html', {'form': form})

def resource_delete(request, pk):
    resource = get_object_or_404(resource, pk=pk)

    if request.method == 'POST':
        resource.delete()
        messages.success(request, 'El recurso ha sido eliminado con éxito.')
        return redirect('resource_list')

    return render(request, 'resources/resource_confirm_delete.html', {'resource': resource})


#Manejo de categorias

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'resources/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'resources/category_form.html', {'form': form})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'resources/category_form.html', {'form': form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('category_list')


#Manejo de Subcategorias
def subcategory_list(request):
    subcategories = Subcategory.objects.all()
    return render(request, 'resources/subcategory_list.html', {'subcategories': subcategories})
def subcategory_create(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm()
    return render(request, 'resources/subcategory_form.html', {'form': form})

def subcategory_edit(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect('subcategory_list')
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, 'resources/subcategory_form.html', {'form': form})

def subcategory_delete(request, pk):
    subcategory = get_object_or_404(Subcategory, pk=pk)
    subcategory.delete()
    return redirect('subcategory_list')



#Manejo de Secciones

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'resources/section_list.html', {'sections': sections})

def section_create(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'resources/section_form.html', {'form': form})

def section_edit(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm(instance=section)
    return render(request, 'resources/section_form.html', {'form': form})

def section_delete(request, pk):
    section = get_object_or_404(Section, pk=pk)
    section.delete()
    return redirect('section_list')


