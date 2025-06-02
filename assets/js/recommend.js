document.getElementById("recommendButton").addEventListener("click", async function () {
  const ingredients = document.getElementById("inputText").value.trim();

  const getSelectedValue = (dropdownId) => {
    const dropdown = document.getElementById(dropdownId);
    const selected = dropdown.querySelector(".dropdown__item.selected");
    return selected ? selected.textContent : "";
  };

  const country = getSelectedValue("countryDropdown");
  const nutriscore = getSelectedValue("nutriscoreDropdown");
  const nova_group = getSelectedValue("novaGroupDropdown");

  // 🔽 Simulation locale (remplace fetch temporairement)
  const simulatedResponse = [
    { product_name: "Pâtes Bio Carrefour", score: 0.92 },
    { product_name: "Tomates en boîte Mutti", score: 0.89 },
    { product_name: "Huile d'olive extra vierge Puget", score: 0.87 }
  ];

  const data = simulatedResponse;

  // 🔽 Affichage
  const outputDiv = document.getElementById("recommendation-output");
  if (data.length === 0) {
    outputDiv.innerHTML = "<p style='color:white;'>Aucun produit trouvé.</p>";
  } else {
    outputDiv.innerHTML = "<h3 style='color:white;'>Produits recommandés :</h3><ul style='color:white;'>";
    data.forEach((item) => {
      outputDiv.innerHTML += `<li>${item.product_name} (score: ${item.score})</li>`;
    });
    outputDiv.innerHTML += "</ul>";
  }
});





document.querySelectorAll(".dropdown").forEach(dropdown => {
  const items = dropdown.querySelectorAll(".dropdown__item");
  const buttonText = dropdown.querySelector(".dropdown__name");

  items.forEach(item => {
    item.addEventListener("click", () => {
      // Retirer la classe "selected" de tous les items
      items.forEach(i => i.classList.remove("selected"));
      // Ajouter la classe à l’élément cliqué
      item.classList.add("selected");
      // Mettre à jour le bouton
      buttonText.textContent = item.textContent;
    });
  });
});
