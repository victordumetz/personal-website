const toggleButton = document.getElementById("toggle-navigation-bar")
const navigationItems = document.querySelector(".navigation-items")

const toggleDropdown = function () {
  navigationItems.classList.toggle("dropdown");
};

toggleButton.addEventListener("click", function(e) {
  e.stopPropagation();
  toggleDropdown();
})

document.documentElement.addEventListener("click", function () {
  if (navigationItems.classList.contains("dropdown")) {
    toggleDropdown();
  }
});
