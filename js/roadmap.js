/* =========================================================================
   MOJALEFA L. LETSOARA — living elements
   Loaded after js/main.js. Countdown to the next booked exam, a real
   last-updated stamp, and a live GitHub pulse in the nav. Everything here
   degrades quietly: if the GitHub API is unreachable, the static fallback
   already in the page markup just stays as it is.
   ========================================================================= */
(function () {
  'use strict';

  /* ---------- Countdown to the next booked exam ---------- */
  var countdownEls = document.querySelectorAll('[data-countdown-to]');
  countdownEls.forEach(function (el) {
    var target = new Date(el.getAttribute('data-countdown-to')).getTime();
    function tick() {
      var diff = target - Date.now();
      if (diff <= 0) { el.textContent = 'Today'; return; }
      var days = Math.floor(diff / 86400000);
      el.textContent = days + (days === 1 ? ' day' : ' days');
    }
    tick();
    setInterval(tick, 60000);
  });

  /* ---------- Real last-updated stamp ---------- */
  var updatedEls = document.querySelectorAll('[data-last-updated]');
  updatedEls.forEach(function (el) {
    var iso = el.getAttribute('data-last-updated');
    var d = new Date(iso + 'T00:00:00');
    if (isNaN(d.getTime())) return;
    el.textContent = d.toLocaleDateString('en-ZA', { day: 'numeric', month: 'long', year: 'numeric' });
  });

  /* ---------- Live GitHub pulse (public repos, unauthenticated, read-only) ---------- */
  var pulseEls = document.querySelectorAll('[data-github-pulse]');
  if (pulseEls.length) {
    fetch('https://api.github.com/users/Justjeff211')
      .then(function (res) { if (!res.ok) throw new Error('github fetch failed'); return res.json(); })
      .then(function (user) {
        pulseEls.forEach(function (el) {
          el.textContent = user.public_repos + ' public repos, updated live from GitHub';
        });
      })
      .catch(function () {
        /* Static copy already in the markup stays as-is. */
      });
  }

  /* ---------- 2027 flip cards: click/tap to flip, fully keyboard accessible ---------- */
  var flipCards = document.querySelectorAll('.flip-card');
  flipCards.forEach(function (card) {
    var front = card.querySelector('.flip-card-front');
    var back = card.querySelector('.flip-card-back');
    var frontBtn = front ? front.querySelector('.flip-trigger') : null;
    var backBtn = back ? back.querySelector('.flip-trigger') : null;

    function setFlipped(flipped) {
      card.classList.toggle('is-flipped', flipped);
      if (front) front.setAttribute('aria-hidden', flipped ? 'true' : 'false');
      if (back) back.setAttribute('aria-hidden', flipped ? 'false' : 'true');
      if (frontBtn) { frontBtn.setAttribute('tabindex', flipped ? '-1' : '0'); frontBtn.setAttribute('aria-expanded', String(flipped)); }
      if (backBtn) { backBtn.setAttribute('tabindex', flipped ? '0' : '-1'); backBtn.setAttribute('aria-expanded', String(flipped)); }
    }

    setFlipped(false);

    if (frontBtn) frontBtn.addEventListener('click', function () { setFlipped(true); if (backBtn) backBtn.focus(); });
    if (backBtn) backBtn.addEventListener('click', function () { setFlipped(false); if (frontBtn) frontBtn.focus(); });
  });
})();
