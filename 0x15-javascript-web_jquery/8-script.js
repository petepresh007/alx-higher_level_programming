$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        dataType: 'json',
        success: function(data) {
            data.results.map(data => {
                const li = $(`<li>${data.title}</li>`);
                $('ul#list_movies').append(li);
            });
        }
    });
});