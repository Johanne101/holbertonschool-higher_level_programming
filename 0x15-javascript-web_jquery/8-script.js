$.ajax({
	url: 'https://swapi-api.hbtn.io/api/films/?format=json',
	success: function (result) {
		$.each(result.results, function(key, value) {
			$('UL#list_movies').prepend('<li>' + value.title + '</li>');
		});
	}
});
