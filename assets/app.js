(function () {
  const track = (eventName, detail) => {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: eventName, ...detail });
    window.dispatchEvent(new CustomEvent(eventName, { detail }));
  };

  document.querySelectorAll('[data-outbound]').forEach((link) => {
    link.addEventListener('click', () => {
      track('shryder_outbound_click', {
        destination: link.dataset.outbound,
        href: link.href,
        page: location.pathname
      });
    });
  });
})();
