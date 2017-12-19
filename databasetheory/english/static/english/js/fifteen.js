window.onload = function() {
	document.querySelector(".begin").addEventListener("click", mix);
	var timerId;
	var numbers = document.querySelectorAll(".com");
	var sixteen = 15;
	var minutes = document.querySelector(".minutes");
	var seconds = document.querySelector(".seconds");
	mix();
	function compareRandom(a, b) {
		return Math.random() - 0.5;
	}
	function mix() {
		var appnum = [];
		for (var i = 0; i < 16; i++) {
			appnum.push(i);
		}
		appnum.sort(compareRandom);
		for (var i = 0; i < 15; i++) {
			numbers[appnum[i]].style.backgroundColor = "green";
			numbers[appnum[i]].innerHTML = String(i+1);
		}
		numbers[appnum[15]].style.backgroundColor = "#0565ba";
		numbers[appnum[15]].innerHTML = "";
		var inv = [];
		for (var i = 0; i < 16; i++) {
			if (numbers[i].innerHTML != "")
				inv.push(Number(numbers[i].innerHTML))
		}
		console.log(inv);
		var inversions = 0;
		for (var i = 0; i < 15; i++) {
			for (var j = i; j < 15; j++) {
				if (inv[i] > inv[j])
					inversions++;
			}
		}
		var k = 0;
		if (appnum[15] < 4 || (appnum[15] > 7 && appnum[15] < 12))
			k = 1;
		if ((inversions + k) % 2 == 1)
			mix();
		else {
			sixteen = appnum[15];
			console.log(appnum[15]);
			minutes.innerHTML = "00";
			seconds.innerHTML = "00";
			clearInterval(timerId);
			timerId = setInterval(function() {
				seconds.innerHTML = String(Number(seconds.innerHTML) + 1);
				if ((seconds.innerHTML).length == 1) {
					seconds.innerHTML = "0" + seconds.innerHTML;
				} else if (Number(seconds.innerHTML) == 60) {
					minutes.innerHTML = String(Number(minutes.innerHTML) + 1);
					if (minutes.innerHTML.length == 1) {
						minutes.innerHTML = "0" + minutes.innerHTML;
					}
					seconds.innerHTML = "00";
				}

			}, 1000)
		}
	}

	function check() {
		var flag = true;
		for (var i = 0; i < 15; i++) {
			if (numbers[i].innerHTML != String(i+1)) {
				flag = false;
				break;
			}
		}
		if (flag) {
			var constr = "You did it! :) Your result is " + minutes.innerHTML + ":" + seconds.innerHTML + " Will you play again?";
			var again = confirm(constr);
			if (again) {
				mix();
			} else {
				clearInterval(timerId);
			}
		}
	}

	numbers[0].addEventListener("click", function() {
			numClick(0);
		});
	numbers[1].addEventListener("click", function() {
			numClick(1);
		});
	numbers[2].addEventListener("click", function() {
			numClick(2);
		});
	numbers[3].addEventListener("click", function() {
			numClick(3);
		});
	numbers[4].addEventListener("click", function() {
			numClick(4);
		});
	numbers[5].addEventListener("click", function() {
			numClick(5);
		});
	numbers[6].addEventListener("click", function() {
			numClick(6);
		});
	numbers[7].addEventListener("click", function() {
			numClick(7);
		});
	numbers[8].addEventListener("click", function() {
			numClick(8);
		});
	numbers[9].addEventListener("click", function() {
			numClick(9);
		});
	numbers[10].addEventListener("click", function() {
			numClick(10);
		});
	numbers[11].addEventListener("click", function() {
			numClick(11);
		});
	numbers[12].addEventListener("click", function() {
			numClick(12);
		});
	numbers[13].addEventListener("click", function() {
			numClick(13);
		});
	numbers[14].addEventListener("click", function() {
			numClick(14);
		});
	numbers[15].addEventListener("click", function() {
			numClick(15);
		});

	/*for (var i = 0; i < 16; i++) {
		console.log(i);
		numbers[i].addEventListener("click", function() {
			numClick(i);
		});
	}*/

	function numClick(i) {
		if (i+1 < 16 && i+1 != 4 && i+1 != 8 && i+1 != 12 && numbers[i+1].innerHTML == "") {
			numbers[i+1].innerHTML = numbers[i].innerHTML;
			numbers[i+1].style.backgroundColor = "green";
			numbers[i].innerHTML = "";
			numbers[i].style.backgroundColor = "#0565ba";
			sixteen = i;
		} else if (i-1 >= 0 && i-1 != 3 && i-1 != 7 && i-1 != 11 && numbers[i-1].innerHTML == "") {
			numbers[i-1].innerHTML = numbers[i].innerHTML;
			numbers[i-1].style.backgroundColor = "green";
			numbers[i].innerHTML = "";
			numbers[i].style.backgroundColor = "#0565ba";
			sixteen = i;
		} else if (i+4 < 16 && numbers[i+4].innerHTML == "") {
			numbers[i+4].innerHTML = numbers[i].innerHTML;
			numbers[i+4].style.backgroundColor = "green";
			numbers[i].innerHTML = "";
			numbers[i].style.backgroundColor = "#0565ba";
			sixteen = i;
		} else if (i-4 >= 0 && numbers[i-4].innerHTML == "") {
			numbers[i-4].innerHTML = numbers[i].innerHTML;
			numbers[i-4].style.backgroundColor = "green";
			numbers[i].innerHTML = "";
			numbers[i].style.backgroundColor = "#0565ba";
			sixteen = i;
		}
		check();
	}

	function move(e) {
		console.log(sixteen);
		switch(e.keyCode) {
			case 37:
				if (sixteen != 3 && sixteen != 7 && sixteen != 11 && sixteen != 15) {
					numbers[sixteen].style.backgroundColor = "green";
					numbers[sixteen].innerHTML = numbers[sixteen+1].innerHTML;
					numbers[sixteen+1].style.backgroundColor = "#0565ba";
					numbers[sixteen+1].innerHTML = "";
					sixteen++;
				}
				check();
				break;
			case 38:
				if (sixteen < 12) {
					numbers[sixteen].style.backgroundColor = "green";
					numbers[sixteen].innerHTML = numbers[sixteen+4].innerHTML;
					numbers[sixteen+4].style.backgroundColor = "#0565ba";
					numbers[sixteen+4].innerHTML = "";
					sixteen += 4;
				}
				check();
				break;
			case 39:
				if (sixteen != 0 && sixteen != 4 && sixteen != 8 && sixteen != 12) {
					numbers[sixteen].style.backgroundColor = "green";
					numbers[sixteen].innerHTML = numbers[sixteen-1].innerHTML;
					numbers[sixteen-1].style.backgroundColor = "#0565ba";
					numbers[sixteen-1].innerHTML = "";
					sixteen--;
				}
				check();
				break;
			case 40:
				if (sixteen > 3) {
					numbers[sixteen].style.backgroundColor = "green";
					numbers[sixteen].innerHTML = numbers[sixteen-4].innerHTML;
					numbers[sixteen-4].style.backgroundColor = "#0565ba";
					numbers[sixteen-4].innerHTML = "";
					sixteen -= 4;
				}
				check();
				break;
		}
		/*for (var i = 0; i < 16; i++) {
			console.log(numbers[i].innerHTML);
		}
		console.log("URAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");*/
	}

	window.addEventListener("keyup", move);
}
