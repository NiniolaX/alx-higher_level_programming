$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    success: function (response) {
      for (const film of response.results) {
        $('#list_movies').append('<li>' + film.title + '</li>');
      }
    },
    error: function (error) {
      $('#list_movies').text('Error fetching data: ' + error.statusText);
    }
  });
});
