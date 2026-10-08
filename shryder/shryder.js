(() => {
  const button = document.querySelector('[data-copy-mint]');
  const address = document.querySelector('#mint-address');
  const status = document.querySelector('#copy-status');
  if (!button || !address || !status) return;

  const originalStatus = status.textContent;
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(address.textContent.trim());
      button.textContent = 'Copied';
      status.textContent = 'Full mint address copied. Compare it with an independent explorer before taking any action.';
    } catch {
      button.textContent = 'Select';
      const range = document.createRange();
      range.selectNodeContents(address);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = 'Automatic copy was unavailable. The full mint address is selected for manual copying.';
    }

    window.setTimeout(() => {
      button.textContent = 'Copy';
      status.textContent = originalStatus;
    }, 5000);
  });
})();
