$(document).ready(function(){
	$.ajax({
		url: 'https://fourtonfish.com/hellosalut/?lang=fr',
		success: function (result) {
			$('DIV#hello').text(result.hello);
		}
	});
});
