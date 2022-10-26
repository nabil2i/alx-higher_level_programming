document.addEventListener('DOMContentLoaded', function () {
    $('#add_item').click(function () {
      $('<li>Item</li>').appendTo('UL.my_list');
    });
    $('#remove_item').click(function () {
      $('.my_list li').last().remove();
    });
    $('#clear_list').click(function () {
        $('ul.my_list').empty();
    });
});
