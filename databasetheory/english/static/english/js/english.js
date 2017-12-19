jQuery('document').ready(function() {
	var all_buttons = jQuery('button');
	var word_amount = 0;
	var all_words = []
	function sendd(yes, word) {
		jQuery.get({type:"GET", url:"/testt", dataType: 'json', data: {'word':word, 'learned': yes}, 
														success:onAjaxSuccesss});
	}
	sendd(true, '')
	var result = 0;
	var ind_this;
	var end;
	jQuery('button').on('click', function() {
		end = 1;
		for (var i = 0; i < all_buttons.length; i++) {
			if (all_buttons[i] == this)
				ind_this = i;
		}
		for (var i = 0; i < all_buttons.length; i++) {
			if (jQuery(all_buttons[i]).attr("disabled") && jQuery(all_buttons[i]).attr('n') == jQuery(this).attr('n')) {
				jQuery(this).css('visibility', 'hidden');
				jQuery(all_buttons[i]).css('visibility', 'hidden');
			}
			else if (jQuery(all_buttons[i]).attr("disabled") && ((i <= 4 && ind_this >= 5) || (i >= 5 && ind_this <= 4)))
				if (jQuery(all_buttons[i]).css('visibility') == 'visible')
					result++;
			jQuery(all_buttons[i]).removeAttr("disabled");
			jQuery(all_buttons[i]).css("background-color", "#032042");
		}
		jQuery(this).attr("disabled", "");
		jQuery(this).css("background-color", "red");
		for (var i = 0; i < all_buttons.length; i++)
			if (jQuery(all_buttons[i]).css('visibility') == 'visible') {
				end = 0;
				break;
			}
		if (end == 1) {
			alert("Amount of wrong answers: " + result.toString());
			var answer = confirm('Do you want to play again?');
			if (answer) {
				all_words = []
				word_amount = 0
				sendd()
			}
		}
	});
	
	function start(all_words) {
		result = 0;
		var numbers = []
		for (var i = 0; i < 10; i++) {
			jQuery(all_buttons[i]).css('visibility', 'visible');
			jQuery(all_buttons[i]).css('background-color', "#032042");
			jQuery(all_buttons[i]).removeAttr("disabled");
		}
		for (var i = 0; i < 5; i++) {
			which = Math.floor(Math.random()*5);
			while (is_there(numbers, which))
				which = Math.floor(Math.random()*5);
			numbers.push(which);
			jQuery(all_buttons[i]).attr("n", all_words[which]["Word"]["id"]);
			jQuery(all_buttons[i]).text(all_words[which]["Word"]["into_russian"]);
		}
		numbers = [];
		for (var i = 5; i < 10; i++) {
			which = Math.floor(Math.random()*5);
			while (is_there(numbers, which))
				which = Math.floor(Math.random()*5);
			numbers.push(which);
			jQuery(all_buttons[i]).attr("n", all_words[which]["Word"]["id"]);
			jQuery(all_buttons[i]).text(all_words[which]["Word"]["into_english"]);
		}
	}
	function onAjaxSuccesss(data) {
		var answer = confirm('Do you know word: ' + data['Word']['into_english']);
		if (!answer) {
			all_words.push(data)
			word_amount += 1
		}
		if (word_amount < 5) {
			sendd(answer, data['Word']['into_english'])
		} else if (word_amount == 5) {
			start(all_words)
			
		}
	}
	function is_there(numbers, a) {
		for (var i = 0; i < numbers.length; i++)
			if (numbers[i] == a)
				return true;
		return false;
	}
});