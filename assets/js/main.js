const dropdowns = document.querySelectorAll(".dropdown");

dropdowns.forEach(dropdown => {
  const button = dropdown.querySelector(".dropdown__button");

  button.addEventListener("click", (e) => {
    e.stopPropagation();
    // Ferme tous les autres dropdowns
    dropdowns.forEach(d => {
      if (d !== dropdown) d.classList.remove("show-dropdown");
    });
    dropdown.classList.toggle("show-dropdown");
  });
});

// Fermer quand on clique ailleurs
document.addEventListener("click", () => {
  dropdowns.forEach(dropdown => dropdown.classList.remove("show-dropdown"));
});

