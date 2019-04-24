$(document).on('click', '#add', function() {
    let drawerForm = $('#drawerForm');
    url = drawerForm.attr('data-url');
    form_data = $('#drawerForm :input').serializeArray();
    form_data[1].value = parseInt(form_data[1].value) + 1;
    $.ajax({
        url: url,
        method: 'POST',
        data: form_data,
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-TOKEN', form_data['csrfmiddlewaretoken']);
        },
        success: function(data) {
            drawerForm.html(data);
        }
    });
});

$(document).on('click', '#sub', function() {
    let drawerForm = $('#drawerForm');
    url = drawerForm.attr('data-url');
    form_data = $('#drawerForm :input').serializeArray();
    console.log(form_data);
    count = parseInt(form_data[1].value);
    form_data[1].value = count - 1;
    form_data.push({name: 'form-' + toString(count - 1) + '-DELETE'});
    $.ajax({
        url: url,
        method: 'POST',
        data: form_data,
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-TOKEN', form_data['csrfmiddlewaretoken']);
        },
        success: function(data) {
            drawerForm.html(data);
        }
    });
});