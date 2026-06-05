document.querySelectorAll("[data-tabs]").forEach((tabs) => {
  const buttons = Array.from(tabs.querySelectorAll("[data-tab-target]"));
  const panels = Array.from(tabs.querySelectorAll("[data-tab-panel]"));

  function activate(name) {
    buttons.forEach((button) => {
      const active = button.dataset.tabTarget === name;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-selected", String(active));
    });

    panels.forEach((panel) => {
      panel.hidden = panel.dataset.tabPanel !== name;
    });
  }

  buttons.forEach((button) => {
    button.addEventListener("click", () => activate(button.dataset.tabTarget));
  });

  const initial = buttons[0] ? buttons[0].dataset.tabTarget : "";
  if (initial) activate(initial);
});

document.querySelectorAll("[data-publication-list]").forEach((list) => {
  const controls = list.previousElementSibling;
  const buttons = controls
    ? Array.from(controls.querySelectorAll("[data-sort-publications]"))
    : [];

  function numericValue(item, key) {
    const value = Number.parseInt(item.dataset[key] || "0", 10);
    return Number.isFinite(value) ? value : 0;
  }

  function sortPublications(mode) {
    const items = Array.from(list.children);
    items.sort((a, b) => {
      const primary =
        mode === "date"
          ? numericValue(b, "year") - numericValue(a, "year")
          : numericValue(b, "citations") - numericValue(a, "citations");
      return primary || numericValue(a, "index") - numericValue(b, "index");
    });

    items.forEach((item) => list.appendChild(item));
    buttons.forEach((button) => {
      const active = button.dataset.sortPublications === mode;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", String(active));
    });
  }

  buttons.forEach((button) => {
    button.addEventListener("click", () => sortPublications(button.dataset.sortPublications));
  });

  sortPublications("citations");
});
