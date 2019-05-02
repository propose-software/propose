$('#add-drawer-button').click(function() {
    let drawerForm = $('#drawer-form');
    url = drawerForm.attr('data-url');
    formData = $('#drawer-form :input').serializeArray();
    console.log(formData);
    if (formData.length > 1) {
        formData[1].value = parseInt(formData[1].value) + 1;
    }
    $.ajax({
        url: url,
        method: 'POST',
        data: formData,
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-TOKEN', formData['csrfmiddlewaretoken']);
        },
        success: function(data) {
            drawerForm.html(data);
        }
    });
});

$(document).on('click', '.drawer-delete-button', function() {
    const dataId = $(this).data('id');
    checkBox = $('#' + dataId);
    checkBox.prop('checked', !checkBox.prop("checked"));
    let drawerForm = $('#drawer-form');
    url = drawerForm.attr('data-url');
    formData = $('#drawer-form :input').serializeArray();
    console.log(formData);
    $.ajax({
        url: url,
        method: 'POST',
        data: formData,
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-TOKEN', formData['csrfmiddlewaretoken']);
        },
        success: function(data) {
            drawerForm.html(data);
        }
    });
});
