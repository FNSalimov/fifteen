$(function() {
	var flag = 1;
	$(".blue").click(function() {
		if (flag) {
			$(".icons").fadeIn(1000);
			flag = 0;
		} else {
			$(".icons").fadeOut(1000);
			flag = 1;
		}
	});
});