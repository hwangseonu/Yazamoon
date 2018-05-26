$(document).ready(function(){
	$(".scroll").click(function(event) {
    event.preventDefault();
    $('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);//offset()함수로 위치를 찾음
  });
	$(".login").click(function(event) {
    event.preventDefault();
    $('.b-login').removeClass('hidden');
  });
	$(".signup").click(function(event) {
		event.preventDefault();
		$('.b-signup').removeClass('hidden');
	});
	$(".b-login .close").click(function(event) {
		event.preventDefault();
		$('.b-login').addClass('hidden');
	});
	$(".b-signup .close").click(function(event) {
		event.preventDefault();
		$('.b-signup').addClass('hidden');
	});
});
