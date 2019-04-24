$(document).on('click', '#add', function() {
    let drawerForm = $('#drawerForm');
    url = drawerForm.attr('data-url');
    form_data = $('#drawerForm :input').serializeArray();
    drawerForm.load(url, form_data);
});


// function addDrawer() {
//     const count = $('.drawerRow').length
//     const newEl = $('.drawerRow:last').clone(true);
//     $(newEl).find('[]')
//     $('.drawerRow:last').after(newEl);
// }

// function subtractDrawer() {

// }

// $(document).on('click', '#add', function() {
//     addDrawer();
// });
// $(document).on('click', '#sub', function() {
//     console.log('remove');
// });