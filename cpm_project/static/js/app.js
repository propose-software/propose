function addDrawer() {
    const count = $('.drawerRow').length
    const newEl = $('.drawerRow:last').clone(true);
    $(newEl).find('[]')
    $('.drawerRow:last').after(newEl);
}

function subtractDrawer() {

}

$(document).on('click', '#add', function() {
    addDrawer();
});
$(document).on('click', '#sub', function() {
    console.log('remove');
});