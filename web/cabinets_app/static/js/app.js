$('#addDrawerButton').click(function() {
    let drawerForm = $('#drawerForm');
    url = drawerForm.attr('data-url');
    formData = $('#drawerForm :input').serializeArray();
    if (formData.length > 1) {
        formData[1].value = parseInt(formData[1].value) + 1;
    }
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

// $(document).on('click', '#add_x', function() {
//     let drawerForm = $('#drawerForm');
//     url = drawerForm.attr('data-url');
//     formData = $('#drawerForm :input').serializeArray();
//     formData[1].value = parseInt(formData[1].value) + 1;
//     $.ajax({
//         url: url,
//         method: 'POST',
//         data: formData,
//         beforeSend: function(xhr) {
//             xhr.setRequestHeader('X-TOKEN', formData['csrfmiddlewaretoken']);
//         },
//         success: function(data) {
//             drawerForm.html(data);
//         }
//     });
// });

// $(document).on('click', '#sub', function() {
//     let drawerForm = $('#drawerForm');
//     url = drawerForm.attr('data-url');
//     formData = $('#drawerForm :input').serializeArray();
//     console.log(formData);
//     count = parseInt(formData[1].value);
//     formData[1].value = count - 1;
//     formData.push({name: 'form-' + toString(count - 1) + '-DELETE'});
//     $.ajax({
//         url: url,
//         method: 'POST',
//         data: formData,
//         beforeSend: function(xhr) {
//             xhr.setRequestHeader('X-TOKEN', formData['csrfmiddlewaretoken']);
//         },
//         success: function(data) {
//             drawerForm.html(data);
//         }
//     });
// });