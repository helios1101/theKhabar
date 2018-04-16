$(document).ready(function(){

	$('#random').on('click',function(){

		var username = $('#username').val();
		var title = $('#title').val()
		var comment = $('#comment').val()

		req = $.ajax({
			url : '/update',
			type: 'POST',
			data :{ username :user,title:title,comment:comment}

		});


	});

});