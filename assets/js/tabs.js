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

// The resume on the page is the same markup the PDF is printed from, laid out
// at letter width. Scale it to whatever width it has, so it keeps the printed
// proportions on a phone as well as a laptop. The text stays real and
// selectable; only the box it sits in changes size.
(function () {
  var wraps = Array.prototype.slice.call(document.querySelectorAll('.sheet-wrap'));
  if (!wraps.length) return;

  function fit() {
    wraps.forEach(function (wrap) {
      var sheet = wrap.querySelector('.sheet');
      sheet.style.transform = 'none';
      wrap.style.height = 'auto';
      // A sheet on a tab that is not showing has no width to measure.
      if (!wrap.clientWidth) return;
      var scale = Math.min(1, wrap.clientWidth / sheet.offsetWidth);
      sheet.style.transform = 'scale(' + scale + ')';
      wrap.style.height = sheet.offsetHeight * scale + 'px';
    });
  }

  fit();
  window.addEventListener('resize', fit);
  // A hidden tab has no width to measure, so refit when one is opened.
  document.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('.tab')) setTimeout(fit, 0);
  });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
})();
