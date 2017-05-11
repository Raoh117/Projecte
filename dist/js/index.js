$(document).ready(function(){
    $('#adalt').click(function(){
		$('body, html').animate({
			scrollTop: '0px'
		}, 300);
	});
	
	$('#YES').click(function(){
	var usuari=$(this).closest('.item').data('usuari');
	alert(usuari);
	});
	
	
	$('.titol').hide();
	$('.item').mouseover(function(){
		$(this).children('.titol').show();
	})
	$('.item').mouseout(function(){
		$(this).children('.titol').hide();
	})
})

