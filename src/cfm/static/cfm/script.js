const reAddOperation = /operations\/add/;
const reEditOperation = /operations\/[0-9]*/;

if (
    reAddOperation.test(document.location.pathname)
    || reEditOperation.test(document.location.pathname)
) {
    // TODO: ADD EMPTY FIELD CHECK!
    const form = document.forms[0];
    const categoryUrl = form.attributes[2].value;
    const subcategoryUrl = form.attributes[3].value;

    let typeSelect = form.elements.id_type;
    let categorySelect = form.elements.id_category;
    let subcategorySelect = form.elements.id_subcategory;

    typeSelect.onchange = async function() {
        // Изменит список категорий для выбора.
        let typeId = typeSelect.value;
        let response = await fetch(`${categoryUrl}?type=${typeId}`);
        categorySelect.innerHTML = await response.text();
    }
    categorySelect.onchange = async function() {
        // Изменит список подкатегорий для выбора.
        let categoryId = categorySelect.value;
        let response = await fetch(`${subcategoryUrl}?category=${categoryId}`);
        subcategorySelect.innerHTML = await response.text();
    }
}
