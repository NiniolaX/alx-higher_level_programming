$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (response) {
    $('#hello').text(response.hello);
  }).fail(function (error) {
    console.log('Error fetching data: ' + error.statusText);
  });
});
