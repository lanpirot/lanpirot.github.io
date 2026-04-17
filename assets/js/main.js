(function () {
  var root = document.documentElement;
  var mq = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;

  function currentTheme() {
    return root.getAttribute("data-theme") === "dark" ? "dark" : "light";
  }
  function storedTheme() {
    try {
      var s = localStorage.getItem("theme");
      return (s === "light" || s === "dark") ? s : null;
    } catch (e) { return null; }
  }
  function syncAria(btn) {
    if (btn) btn.setAttribute("aria-pressed", currentTheme() === "dark" ? "true" : "false");
  }

  if (mq) {
    var onSystemChange = function (e) {
      if (storedTheme()) return;
      root.setAttribute("data-theme", e.matches ? "dark" : "light");
      syncAria(document.querySelector(".theme-toggle"));
    };
    if (mq.addEventListener) mq.addEventListener("change", onSystemChange);
    else if (mq.addListener) mq.addListener(onSystemChange);
  }

  function onReady() {
    var btn = document.querySelector(".theme-toggle");
    if (!btn) return;
    syncAria(btn);
    btn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("theme", next); } catch (e) {}
      syncAria(btn);
    });
  }
  if (document.readyState !== "loading") onReady();
  else document.addEventListener("DOMContentLoaded", onReady);
})();
