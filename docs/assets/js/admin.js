document.addEventListener('DOMContentLoaded', function() {
  // This file is a helper for the admin page.
  // Admin.html has its own complete inline script
  // We just ensure theme consistency
  var t = localStorage.getItem('sTheme') || 'light';
  document.documentElement.setAttribute('data-theme', t);
});
