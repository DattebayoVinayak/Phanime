document.addEventListener("DOMContentLoaded", function() {
  const slidesContainer = document.querySelector(".slides");
  const slides = Array.from(slidesContainer.children);
  const indicatorsContainer = document.querySelector(".indicators");

  // Remove existing indicators
  while (indicatorsContainer.firstChild) {
    indicatorsContainer.removeChild(indicatorsContainer.firstChild);
  }

  // Create indicators based on the number of slides
  slides.forEach((slide, index) => {
    const indicator = document.createElement("div");
    if(index===0){
      indicator.classList.add('active')
    }
    indicator.classList.add("indicator");
    indicator.addEventListener("click", () => goToSlide(index));
    indicatorsContainer.appendChild(indicator);
  });

  let currentSlide = 0;

  // Function to go to a specific slide
  function goToSlide(slideIndex) {
    currentSlide = slideIndex;
    const slideWidth = slides[0].offsetWidth;
    slidesContainer.style.transform = `translateX(-${slideWidth * slideIndex}px)`;

    // Update active class for indicators
    const indicators = Array.from(indicatorsContainer.children);
    indicators.forEach((indicator, index) => {
      indicator.classList.toggle("active", index === currentSlide);
    });
  }

  // Automatically advance the carousel
  setInterval(() => {
    currentSlide = (currentSlide + 1) % slides.length;
    goToSlide(currentSlide);
  }, 3000);
});
