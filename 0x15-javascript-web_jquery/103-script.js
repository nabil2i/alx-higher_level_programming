document.addEventListener('DOMContentLoaded', function () {
    $('#language_code').keypress(function (event) {
      const keyCode = event.which;
      if (keyCode === 13) {
        const language = $('#language_code').val();
        $.get('https://fourtonfish.com/hellosalut/?lang=' + language, function (data) {
          $('#hello').text(data.hello);
        });
      }
    });
    $('#btn_translate').click(function () {
      const language = $('#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + language, function (data) {
        $('#hello').text(data.hello);
      });
    });
});
