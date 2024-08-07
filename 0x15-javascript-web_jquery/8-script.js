$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      for (const i in data.results) {
        $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
      }
    }
  });
});
