document.addEventListener('DOMContentLoaded', function () {
    $('#btn_translate').click(function () {
      const language = $('#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + language, function (data, textStatus) {
        if (textStatus === 'success') {
            $('#hello').text(data.hello);
        }
      });
    });
});
