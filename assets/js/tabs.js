// Tabs that survive a refresh and can be shared as a link.
// Every panel is real content in the page; this only chooses which one shows.
(function () {
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
  var panels = Array.prototype.slice.call(document.querySelectorAll('.panel'));
  if (!tabs.length) return;

  function show(id, push) {
    var found = false;
    panels.forEach(function (p) {
      var on = p.id === id;
      if (on) found = true;
      p.classList.toggle('panel-on', on);
    });
    if (!found) return false;
    tabs.forEach(function (t) {
      var on = t.getAttribute('data-tab') === id;
      t.classList.toggle('tab-on', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    if (push && history.replaceState) history.replaceState(null, '', '#' + id);
    return true;
  }

  tabs.forEach(function (t) {
    t.addEventListener('click', function (e) {
      e.preventDefault();
      show(t.getAttribute('data-tab'), true);
      window.scrollTo(0, 0);
    });
  });

  window.addEventListener('hashchange', function () {
    show(location.hash.slice(1), false);
  });

  if (location.hash) show(location.hash.slice(1), false);
})();
