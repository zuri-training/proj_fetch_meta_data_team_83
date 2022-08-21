var faq = document.getElementsByClassName("faq_quest");
var i;

for (i = 0; i < faq.length; i++) {
	faq[i].addEventListener("click",  () => {
		this.classList.toggle("active");

		/* Toggle between hiding and showing the active panel */
		var body = this.nextElementSibling;
		if (body.style.display === "block") {
			body.style.display = "none";
		} else {
			body.style.display = "block";
		}
	});
}
