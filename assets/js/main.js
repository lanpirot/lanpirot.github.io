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

// PGP key popover: toggle the menu and copy a chosen public key to the clipboard.
(function () {
  function onReady() {
    var wrap = document.querySelector("[data-pgp]");
    if (!wrap) return;
    var btn = wrap.querySelector(".pgp-btn");
    var menu = wrap.querySelector(".pgp-menu");
    var status = wrap.querySelector(".pgp-status");
    var items = Array.prototype.slice.call(wrap.querySelectorAll(".pgp-item"));
    var cache = {};
    var copiedTimer;
    function clearCopied() { clearTimeout(copiedTimer); items.forEach(function (it) { it.classList.remove("copied"); }); }

    function fetchKey(src) {
      if (src in cache) return Promise.resolve(cache[src]);
      return fetch(src).then(function (r) {
        if (!r.ok) throw new Error("fetch failed");
        return r.text();
      }).then(function (t) { cache[src] = t; return t; });
    }
    function prime() { items.forEach(function (it) { fetchKey(it.getAttribute("data-src")).catch(function () {}); }); }

    function open() {
      menu.hidden = false;
      btn.setAttribute("aria-expanded", "true");
      document.addEventListener("click", onDoc, true);
      document.addEventListener("keydown", onKey);
    }
    function close() {
      menu.hidden = true;
      btn.setAttribute("aria-expanded", "false");
      if (status) status.textContent = "";
      clearCopied();
      document.removeEventListener("click", onDoc, true);
      document.removeEventListener("keydown", onKey);
    }
    function onDoc(e) { if (!wrap.contains(e.target)) close(); }
    function onKey(e) { if (e.key === "Escape") { close(); btn.focus(); } }

    btn.addEventListener("mouseenter", prime);
    btn.addEventListener("focus", prime);
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      if (menu.hidden) { prime(); open(); } else { close(); }
    });

    items.forEach(function (item) {
      item.addEventListener("click", function () {
        var src = item.getAttribute("data-src");
        var email = item.querySelector(".pgp-email").textContent;
        var ok = function () {
          if (status) status.textContent = "Copied " + email;
          clearCopied();
          item.classList.add("copied");
          copiedTimer = setTimeout(function () { item.classList.remove("copied"); }, 1600);
        };
        var fail = function () { window.open(src, "_blank", "noopener"); close(); };
        fetchKey(src).then(function (text) {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(text).then(ok, fail);
          } else { fail(); }
        }).catch(fail);
      });
    });
  }
  if (document.readyState !== "loading") onReady();
  else document.addEventListener("DOMContentLoaded", onReady);
})();
