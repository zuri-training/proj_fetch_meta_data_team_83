const menu_toggle = document.querySelector(".menu_toggle");
const navigation = document.querySelector(".navigation");
menu_toggle.onclick = function () {
	navigation.classList.toggle("open");
};

const nav_lists = document.querySelectorAll(".nav_list");
function activeLink() {
	nav_lists.forEach((item) => item.classList.remove("active"));
	this.classList.add("active");
}
list.forEach((item) => item.addEventListener("click", activeLink));
