const faqQuest = document.querySelectorAll(".faq_quest");

faqQuest.forEach((faqQuest) => {
  faqQuest.addEventListener("click", (event) => {
    faqQuest.classList.toggle("active");
    const faqBody = faqQuest.nextElementSibling;
    console.log(faqBody);
    if (faqQuest.classList.contains("active")) {
      faqBody.style.maxHeight = faqBody.scrollHeight + "px";
      console.log(faqBody.scrollHeight);
    } else {
      faqBody.style.maxHeight = 0;
    }
  });
});
