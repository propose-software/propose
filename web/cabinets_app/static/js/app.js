$('#addDrawerButton').click(function() {
    let drawerForm = $('#drawerForm');
    url = drawerForm.attr('data-url');
    formData = $('#drawerForm :input').serializeArray();
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

$(document).on('click', '.drawerDeleteButton', function() {
    const dataId = $(this).data('id');
    checkBox = $('#' + dataId);
    checkBox.prop('checked', !checkBox.prop("checked"));
    let drawerForm = $('#drawerForm');
    url = drawerForm.attr('data-url');
    formData = $('#drawerForm :input').serializeArray();
    console.log(formData);
    // if (formData.length > 1) {
    //     formData[1].value = parseInt(formData[1].value) - 1;
    // }
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
