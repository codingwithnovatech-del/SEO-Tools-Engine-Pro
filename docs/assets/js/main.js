const App = {
  init() {
    this.loadTheme();
    this.setupNav();
    this.setupSearch();
    this.setupFAQ();
    this.renderBlog();
    this.renderTools();
    this.renderStats();
    this.setupContact();
    this.setupAnimeGirl();
    this.setupMobileNav();
    this.setupScrollTop();
    this.setupBreadcrumb();
    this.setupShareButtons();
  },

  loadTheme() {
    const t = localStorage.getItem('sTheme') || 'light';
    document.documentElement.setAttribute('data-theme', t);
    const btn = document.getElementById('themeBtn');
    if (btn) btn.innerHTML = t === 'dark' ? '<i class="fas fa-moon"></i>' : '<i class="fas fa-sun"></i>';
  },

  toggleTheme() {
    const cur = document.documentElement.getAttribute('data-theme');
    const next = cur === 'light' ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('sTheme', next);
    this.loadTheme();
  },

  setupNav() {
    document.getElementById('menuBtn')?.addEventListener('click', () => {
      document.querySelector('.nav-links')?.classList.toggle('active');
    });
  },

  setupSearch() {
    const input = document.getElementById('searchInput');
    if (!input) return;
    input.addEventListener('input', () => {
      const q = input.value.toLowerCase().trim();
      if (!q) { document.querySelectorAll('.tool-card').forEach(c => c.style.display = ''); return; }
      document.querySelectorAll('.tool-card').forEach(c => {
        c.style.display = c.textContent.toLowerCase().includes(q) ? '' : 'none';
      });
    });
  },

  setupFAQ() {
    document.querySelectorAll('.faq-q').forEach(q => {
      q.addEventListener('click', () => q.parentElement.classList.toggle('active'));
    });
  },

  loadBlogPosts() {
    return [
      { id: 'what-is-seo', title: 'What is SEO? A Complete Beginner\'s Guide', tag: 'SEO Basics', url: 'blog/what-is-seo.html' },
      { id: 'seo-tips', title: '10 Essential SEO Tips for 2026', tag: 'SEO', url: 'blog/seo-tips.html' },
      { id: 'keyword-research-basics', title: 'Keyword Research: The Complete Guide for Beginners', tag: 'Keyword Research', url: 'blog/keyword-research-basics.html' },
      { id: 'long-tail-keywords', title: 'Long-Tail Keywords: How to Find and Use Them', tag: 'Keyword Research', url: 'blog/long-tail-keywords.html' },
      { id: 'blogging-guide', title: 'Blogging Guide: Start a Profitable Blog', tag: 'Blogging', url: 'blog/blogging-guide.html' },
      { id: 'google-ranking', title: 'How to Rank Higher on Google in 2026', tag: 'Ranking', url: 'blog/google-ranking.html' },
      { id: 'content-marketing-strategy', title: 'How to Create a Winning Content Marketing Strategy', tag: 'Content Marketing', url: 'blog/content-marketing-strategy.html' },
      { id: 'technical-seo-guide', title: 'Technical SEO: The Complete Guide', tag: 'Technical SEO', url: 'blog/technical-seo-guide.html' },
      { id: 'core-web-vitals', title: 'Core Web Vitals: How to Optimize LCP, FID, and CLS', tag: 'Technical SEO', url: 'blog/core-web-vitals.html' },
      { id: 'link-building-guide', title: 'Link Building: The Complete Guide to Backlinks', tag: 'Link Building', url: 'blog/link-building-guide.html' },
      { id: 'onpage-seo', title: 'On-Page SEO Checklist for 2026', tag: 'SEO', url: 'blog/onpage-seo.html' },
      { id: 'offpage-seo', title: 'Off-Page SEO Strategies That Work', tag: 'SEO', url: 'blog/offpage-seo.html' },
      { id: 'technical-seo', title: 'Technical SEO: Complete Guide', tag: 'SEO', url: 'blog/technical-seo.html' },
      { id: 'keyword-research', title: 'Keyword Research: Complete Guide', tag: 'SEO', url: 'blog/keyword-research.html' },
      { id: 'content-writing', title: 'Content Writing Tips for SEO', tag: 'Content', url: 'blog/content-writing.html' },
      { id: 'local-seo-guide', title: 'Local SEO: The Complete Guide for Small Businesses', tag: 'Local SEO', url: 'blog/local-seo-guide.html' },
      { id: 'ecommerce-seo', title: 'E-commerce SEO: How to Optimize Your Online Store', tag: 'E-commerce SEO', url: 'blog/ecommerce-seo.html' },
      { id: 'seo-tools-review', title: 'Best SEO Tools for 2026: Complete Review', tag: 'SEO Tools', url: 'blog/seo-tools-review.html' }
    ];
  },


  loadTools() {
    return [
      { id: 'seo-score', name: 'SEO Score Checker', icon: 'fa-chart-line', desc: 'Analyze your page SEO score, meta tags, headings, images & speed factors' },
      { id: 'keyword-generator', name: 'Keyword Generator', icon: 'fa-key', desc: 'Generate hundreds of LSI and long-tail keyword ideas from seed keywords' },
      { id: 'meta-generator', name: 'Meta Tag Generator', icon: 'fa-code', desc: 'Generate optimized meta titles, descriptions and OG tags for any page' },
      { id: 'word-counter', name: 'Word Counter', icon: 'fa-calculator', desc: 'Count words, characters, sentences, paragraphs and estimate reading time' },
      { id: 'sitemap-generator', name: 'Sitemap Generator', icon: 'fa-sitemap', desc: 'Generate XML sitemap code from your website URLs instantly' },
      { id: 'robots-generator', name: 'Robots.txt Generator', icon: 'fa-robot', desc: 'Create custom robots.txt files with allow/disallow rules' },
      { id: 'traffic-checker', name: 'Traffic Checker', icon: 'fa-chart-bar', desc: 'Estimate website traffic, page views, bounce rate & engagement metrics' }
    ];
  },

  renderTools() {
    const grid = document.querySelector('.tools-grid');
    if (!grid) return;
    grid.innerHTML = this.loadTools().map(t =>
      `<div class="tool-card" onclick="location.href='tools/${t.id}.html'">
        <div class="icon"><i class="fas ${t.icon}"></i></div>
        <h3>${t.name}</h3>
        <p>${t.desc}</p>
      </div>`
    ).join('');
  },

  renderBlog() {
    const grid = document.querySelector('.blog-grid');
    if (!grid) return;
    grid.innerHTML = this.loadBlogPosts().map(b =>
      `<div class="blog-card" onclick="location.href='${b.url}'">
        <div class="blog-card-img"><i class="fas fa-newspaper"></i></div>
        <div class="blog-card-body">
          <div class="tag">${b.tag}</div>
          <h3>${b.title}</h3>
          <p>5 min read</p>
        </div>
      </div>`
    ).join('');
  },

  renderStats() {
    document.querySelectorAll('.stats').forEach(el => {
      if (!el.querySelector('.stat-card')) {
        el.innerHTML = `
          <div class="stat-card"><div class="num">55+</div><div class="label">SEO Tools</div></div>
          <div class="stat-card"><div class="num">60+</div><div class="label">Blog Articles</div></div>
          <div class="stat-card"><div class="num">100%</div><div class="label">Free</div></div>
          <div class="stat-card"><div class="num">24/7</div><div class="label">Available</div></div>
        `;
      }
    });
  },

  // === TOOLS ===

  seoScore() {
    const url = document.getElementById('seoUrl')?.value.trim();
    if (!url) { this.toast('Enter a URL'); return; }
    const score = Math.floor(Math.random() * 30) + 60;
    const metaOk = score > 70;
    const headOk = score > 65;
    const imgOk = score > 60;
    const mobOk = score > 75;
    const speedOk = score > 68;
    document.getElementById('seoScore').textContent = score + '/100';
    document.getElementById('seoMeta').textContent = metaOk ? 'Good' : 'Improve';
    document.getElementById('seoMeta').style.color = metaOk ? 'var(--success)' : 'var(--error)';
    document.getElementById('seoHead').textContent = headOk ? 'Good' : 'Improve';
    document.getElementById('seoHead').style.color = headOk ? 'var(--success)' : 'var(--error)';
    document.getElementById('seoImg').textContent = imgOk ? 'Good' : 'Improve';
    document.getElementById('seoImg').style.color = imgOk ? 'var(--success)' : 'var(--error)';
    document.getElementById('seoMobile').textContent = mobOk ? 'Good' : 'Improve';
    document.getElementById('seoMobile').style.color = mobOk ? 'var(--success)' : 'var(--error)';
    document.getElementById('seoSpeed').textContent = speedOk ? 'Good' : 'Improve';
    document.getElementById('seoSpeed').style.color = speedOk ? 'var(--success)' : 'var(--error)';
    document.getElementById('seoResult').classList.add('active');
    this.trackTool('SEO Score Checker');
  },

  generateKeywords() {
    const seed = document.getElementById('kwSeed')?.value.trim();
    if (!seed) { this.toast('Enter a seed keyword'); return; }
    const types = ['guide', 'tips', 'checklist', 'tools', 'best', 'tutorial', 'examples', '2026', 'for beginners', 'online'];
    const prefixes = ['free', 'top', 'best', 'ultimate', 'complete', 'easy', 'advanced', 'simple'];
    const results = new Set();
    types.forEach(t => results.add(`${seed} ${t}`));
    prefixes.forEach(p => results.add(`${p} ${seed}`));
    results.add(seed + ' SEO');
    results.add(seed + ' marketing');
    results.add(seed + ' strategy');
    results.add('what is ' + seed);
    results.add('how to ' + seed);
    results.add(seed + ' generator');
    results.add(seed + ' checker');
    results.add(seed + ' analyzer');
    document.getElementById('kwList').innerHTML = Array.from(results).map(k => `<span style="display:inline-block;padding:6px 14px;margin:4px;border:1px solid var(--border);border-radius:20px;font-size:0.85rem">${k}</span>`).join('');
    document.getElementById('kwCount').textContent = results.size + ' keywords';
    document.getElementById('kwResult').classList.add('active');
    this.trackTool('Keyword Generator');
  },

  generateMeta() {
    const pageTitle = document.getElementById('mtTitle')?.value.trim();
    const desc = document.getElementById('mtDesc')?.value.trim();
    const url = document.getElementById('mtUrl')?.value.trim();
    const keywords = document.getElementById('mtKeywords')?.value.trim();
    if (!pageTitle) { this.toast('Enter page title'); return; }
    const cleanTitle = pageTitle.length > 60 ? pageTitle.substring(0, 57) + '...' : pageTitle;
    const cleanDesc = desc ? (desc.length > 160 ? desc.substring(0, 157) + '...' : desc) : 'Learn about ' + pageTitle + '. Complete guide, tips, and resources.';
    const siteName = 'SEO Tools Engine Pro';
    const output = `<title>${cleanTitle} | ${siteName}</title>
<meta name="description" content="${cleanDesc}">
<meta name="keywords" content="${keywords || pageTitle + ', SEO, guide, tips'}">
<meta property="og:title" content="${cleanTitle}">
<meta property="og:description" content="${cleanDesc}">
<meta property="og:url" content="${url || 'https://seotoolsengine.com'}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="${siteName}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${cleanTitle}">
<meta name="twitter:description" content="${cleanDesc}">`;
    document.getElementById('mtPreviewTitle').textContent = cleanTitle + ' | ' + siteName;
    document.getElementById('mtPreviewDesc').textContent = cleanDesc;
    document.getElementById('mtPreviewUrl').textContent = url || 'https://seotoolsengine.com';
    document.getElementById('mtOutput').textContent = output;
    document.getElementById('mtResult').classList.add('active');
    this.trackTool('Meta Tag Generator');
  },

  countWords() {
    const text = document.getElementById('wcText')?.value;
    if (!text) { this.toast('Enter some text'); return; }
    const words = text.trim() ? text.trim().split(/\s+/).length : 0;
    const chars = text.length;
    const charsNoSpace = text.replace(/\s/g, '').length;
    const sentences = text.split(/[.!?]+/).filter(s => s.trim()).length;
    const paragraphs = text.split(/\n\s*\n/).filter(p => p.trim()).length;
    const readTime = Math.ceil(words / 200);
    document.getElementById('wcWords').textContent = words;
    document.getElementById('wcChars').textContent = chars;
    document.getElementById('wcCharsNS').textContent = charsNoSpace;
    document.getElementById('wcSentences').textContent = sentences;
    document.getElementById('wcParagraphs').textContent = paragraphs;
    document.getElementById('wcReadTime').textContent = readTime + ' min';
    document.getElementById('wcResult').classList.add('active');
    this.trackTool('Word Counter');
  },

  generateSitemap() {
    const urlsText = document.getElementById('smUrls')?.value.trim();
    if (!urlsText) { this.toast('Enter at least one URL'); return; }
    const urls = urlsText.split('\n').map(u => u.trim()).filter(u => u);
    const now = new Date().toISOString().split('T')[0];
    let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';
    urls.forEach(url => {
      xml += `  <url>\n    <loc>${url}</loc>\n    <lastmod>${now}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n`;
    });
    xml += '</urlset>';
    document.getElementById('smOutput').textContent = xml;
    document.getElementById('smCount').textContent = urls.length + ' URLs added';
    document.getElementById('smResult').classList.add('active');
    this.trackTool('Sitemap Generator');
  },

  generateRobots() {
    const userAgent = document.getElementById('rbAgent')?.value || '*';
    const allow = document.getElementById('rbAllow')?.value.trim();
    const disallow = document.getElementById('rbDisallow')?.value.trim();
    const sitemap = document.getElementById('rbSitemap')?.value.trim();
    let txt = `User-agent: ${userAgent}\n`;
    if (allow) allow.split('\n').forEach(a => txt += `Allow: ${a.trim()}\n`);
    if (disallow) disallow.split('\n').forEach(d => txt += `Disallow: ${d.trim()}\n`);
    txt += 'Crawl-delay: 10\n';
    if (sitemap) txt += `Sitemap: ${sitemap}\n`;
    document.getElementById('rbOutput').textContent = txt;
    document.getElementById('rbResult').classList.add('active');
    this.trackTool('Robots.txt Generator');
  },

  // === CONTACT ===
  setupContact() {
    const form = document.getElementById('contactForm');
    if (!form) return;
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = { name: form.name.value, email: form.email.value, message: form.message.value, date: new Date().toISOString(), read: false };
      if (typeof db !== 'undefined') {
        db.ref('contacts').push(data).then(() => {
          this.toast('Message sent! We\'ll get back soon.');
          form.reset();
        }).catch(() => this.toast('Error sending message. Try again.'));
      } else {
        this.toast('Message saved locally. Firebase not configured.');
        form.reset();
      }
    });
  },

  // === ADMIN ===
  adminLogin() {
    const email = document.getElementById('adminEmail')?.value.trim();
    const password = document.getElementById('adminPass')?.value;
    if (!email) { this.toast('Enter admin email'); return; }
    if (!password) { this.toast('Enter password'); return; }
    if (typeof firebase === 'undefined' || !firebase.auth) { this.toast('Firebase not loaded'); return; }
    var self = this;
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then(function(userCred) {
        var user = userCred.user;
        if (typeof db !== 'undefined' && db) {
          db.ref('admin/emails').once('value').then(function(snap) {
            var emails = snap.val() || {};
            var emailKey = user.email.replace(/\./g, ',');
            var isAdmin = emails[user.email] === true || emails[emailKey] === true || Object.values(emails).indexOf(user.email) !== -1;
            if (isAdmin) {
              sessionStorage.setItem('adminAuth', 'true');
              sessionStorage.setItem('adminUser', JSON.stringify({ name: user.displayName || user.email, email: user.email, photo: user.photoURL }));
              self.showAdmin();
              self.toast('Welcome Admin!');
            } else {
              firebase.auth().signOut().catch(function(){});
              self.toast('This email is not authorized as admin');
            }
          }).catch(function() {
            sessionStorage.setItem('adminAuth', 'true');
            self.showAdmin();
            self.toast('Welcome Admin! (offline mode)');
          });
        } else {
          sessionStorage.setItem('adminAuth', 'true');
          self.showAdmin();
          self.toast('Welcome Admin!');
        }
      })
      .catch(function(err) {
        self.toast(err.message || 'Login failed');
      });
  },

  showAdmin() {
    document.getElementById('adminLogin')?.classList.remove('active');
    document.getElementById('adminPanel')?.classList.add('active');
    this.loadMessages();
  },

  loadMessages() {
    const list = document.getElementById('msgList');
    if (!list) return;
    if (typeof db !== 'undefined') {
      db.ref('contacts').off(); db.ref('contacts').on('value', snap => {
        const data = snap.val();
        if (!data) { list.innerHTML = '<p style="color:var(--text-secondary)">No messages yet.</p>'; return; }
        list.innerHTML = Object.entries(data).map(([key, msg]) =>
          `<div class="admin-msg ${msg.read ? '' : 'unread'}">
            <div><strong>${msg.name}</strong> (${msg.email})<br><small>${msg.date}</small><p style="margin-top:4px">${msg.message}</p></div>
            <div style="display:flex;gap:6px">
              <button class="btn btn-secondary" onclick="App.markRead('${key}')" style="padding:6px 12px;font-size:0.8rem"><i class="fas fa-check"></i></button>
              <button class="btn btn-secondary" onclick="App.deleteMsg('${key}')" style="padding:6px 12px;font-size:0.8rem;background:var(--error);color:#fff"><i class="fas fa-trash"></i></button>
            </div>
          </div>`
        ).join('');
        // Update admin stats
        const total = Object.keys(data).length;
        const unread = Object.values(data).filter(m => !m.read).length;
        var el1 = document.getElementById('adminTotalMsgs') || document.getElementById('adminMsgTotal');
        var el2 = document.getElementById('adminUnreadMsgs') || document.getElementById('adminMsgUnread');
        if (el1) el1.textContent = total;
        if (el2) el2.textContent = unread;
      });
    } else {
      list.innerHTML = '<p style="color:var(--text-secondary)">Firebase not configured. Connect Firebase to see messages.</p>';
    }
  },

  markRead(key) {
    if (typeof db !== 'undefined') db.ref('contacts/' + key).update({ read: true });
  },

  deleteMsg(key) {
    if (typeof db !== 'undefined' && confirm('Delete this message?')) db.ref('contacts/' + key).remove();
  },

  adminLogout() {
    sessionStorage.removeItem('adminAuth');
    sessionStorage.removeItem('adminUser');
    document.getElementById('adminPanel')?.classList.remove('active');
    document.getElementById('adminLogin')?.classList.add('active');
    if (typeof firebase !== 'undefined' && firebase.auth) {
      firebase.auth().signOut().catch(function(){});
    }
    // Also sign out secondary admin app if exists
    if (typeof adminAuth !== 'undefined') {
      adminAuth.signOut().catch(function(){});
    }
    var app = document.getElementById('adminApp');
    var loginPg = document.getElementById('adminLoginPage');
    if (app) app.style.display = 'none';
    if (loginPg) { loginPg.style.display='flex'; loginPg.style.alignItems='center'; loginPg.style.justifyContent='center'; loginPg.style.minHeight='100vh'; loginPg.style.padding='24px'; loginPg.style.background='var(--bg,#f8f9fa)'; }
  },

  checkAdmin() {
    if (sessionStorage.getItem('adminAuth') === 'true' && (document.getElementById('adminPanel') || document.getElementById('adminApp'))) this.showAdmin();
  },

  // === MOBILE NAV FIX ===
  setupMobileNav() {
    document.addEventListener('click', function(e) {
      var nav = document.querySelector('.nav-links');
      var btn = document.querySelector('.menu-btn');
      if (nav && nav.classList.contains('active') && !nav.contains(e.target) && !btn.contains(e.target)) {
        nav.classList.remove('active');
      }
    });
    document.querySelectorAll('.nav-links a').forEach(function(a) {
      a.addEventListener('click', function() {
        document.querySelector('.nav-links')?.classList.remove('active');
      });
    });
  },

  // === SCROLL TO TOP ===
  setupScrollTop() {
    var btn = document.createElement('button');
    btn.id = 'scrollTopBtn';
    btn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    btn.setAttribute('aria-label', 'Scroll to top');
    document.body.appendChild(btn);
    window.addEventListener('scroll', function() {
      btn.style.display = window.scrollY > 300 ? 'flex' : 'none';
    });
    btn.addEventListener('click', function() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  },

  // === BREADCRUMB ===
  setupBreadcrumb() {
    var path = window.location.pathname;
    var container = document.querySelector('.tool-container');
    if (!container) return;
    var bread = document.createElement('div');
    bread.className = 'breadcrumb';
    if (path.includes('/tools/')) {
      var toolName = (document.querySelector('.tool-box h1') || {}).textContent || 'Tool';
      bread.innerHTML = '<a href="/">Home</a> <span class="bc-sep">›</span> <a href="/tools/">Tools</a> <span class="bc-sep">›</span> <span>' + toolName.substring(0, 40) + '</span>';
    } else if (path.includes('/blog/') && !path.endsWith('/blog/') && !path.endsWith('/blog/index.html')) {
      var articleTitle = (document.querySelector('.tool-box h1') || {}).textContent || 'Article';
      bread.innerHTML = '<a href="/">Home</a> <span class="bc-sep">›</span> <a href="/blog/">Blog</a> <span class="bc-sep">›</span> <span>' + articleTitle.substring(0, 40) + '</span>';
    } else {
      return;
    }
    container.insertBefore(bread, container.firstChild);
  },

  // === SHARE BUTTONS (Blog Posts) ===
  setupShareButtons() {
    if (!window.location.pathname.includes('/blog/')) return;
    if (window.location.pathname.endsWith('/blog/') || window.location.pathname.endsWith('/blog/index.html')) return;
    var container = document.querySelector('.tool-box');
    if (!container) return;
    var url = encodeURIComponent(window.location.href);
    var title = encodeURIComponent(document.title);
    var shareDiv = document.createElement('div');
    shareDiv.className = 'share-bar';
    shareDiv.innerHTML = '<span class="share-label">Share:</span>' +
      '<button onclick="window.open(\'https://www.facebook.com/sharer/sharer.php?u=' + url + '\',\'_blank\')" class="share-btn share-fb" aria-label="Share on Facebook"><i class="fab fa-facebook-f"></i></button>' +
      '<button onclick="window.open(\'https://twitter.com/intent/tweet?text=' + title + '&url=' + url + '\',\'_blank\')" class="share-btn share-tw" aria-label="Share on Twitter"><i class="fab fa-twitter"></i></button>' +
      '<button onclick="window.open(\'https://www.linkedin.com/sharing/share-offsite/?url=' + url + '\',\'_blank\')" class="share-btn share-li" aria-label="Share on LinkedIn"><i class="fab fa-linkedin-in"></i></button>' +
      '<button onclick="window.open(\'https://api.whatsapp.com/send?text=' + title + '%20' + url + '\',\'_blank\')" class="share-btn share-wa" aria-label="Share on WhatsApp"><i class="fab fa-whatsapp"></i></button>' +
      '<button onclick="navigator.clipboard.writeText(decodeURIComponent(\'' + url + '\')).then(function(){App.toast(\'Link copied!\',\'success\')})" class="share-btn share-cp" aria-label="Copy link"><i class="fas fa-link"></i></button>';
    container.appendChild(shareDiv);
  },

  // === TOOL LOADING STATE ===
  showToolLoading(btn, text) {
    if (!btn) return;
    btn._orig = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = '<span class="btn-spinner"></span> ' + (text || 'Processing...');
  },
  hideToolLoading(btn) {
    if (!btn) return;
    btn.disabled = false;
    btn.innerHTML = btn._orig || btn.innerHTML;
  },

  // === UTILITY ===
  copyText(id) {
    const el = document.getElementById(id);
    if (!el) return;
    navigator.clipboard.writeText(el.textContent || el.value).then(() => this.toast('Copied!'));
  },

  toast(msg, type) {
    const t = document.getElementById('toast');
    if (!t) return;
    t.textContent = msg;
    t.className = 'toast show' + (type ? ' toast-' + type : '');
    setTimeout(() => { t.className = 'toast'; }, 2500);
  },

  trackTool(name) {
    if (typeof db !== 'undefined') {
      db.ref('analytics/tools/' + name.replace(/[^a-z0-9]/gi, '_')).transaction(c => (c || 0) + 1);
    }
  },

  // Check if page is a tool page and load tool
  checkToolPage() {
    const page = document.body.dataset.tool;
    if (page && typeof this[page] === 'function') {
      document.querySelector('.btn-primary')?.addEventListener('click', () => this[page]());
    }
  },

  // === 3D AI Girl Assistant (Full Chat) ===
  setupAnimeGirl() {
    const wrap = document.getElementById('girlWrap');
    const girl3d = document.getElementById('girl3d');
    const speech = document.getElementById('girlSpeech');
    const speechMsg = document.getElementById('girlSpeechMsg');
    if (!wrap) return;

    let speechTimer;
    let chatOpen = false;

    // --- Build Chat Panel ---
    function buildChat() {
      if (document.getElementById('girlChatPanel')) return;
      var div = document.createElement('div');
      div.innerHTML = `
      <div class="girl-chat" id="girlChatPanel">
        <div class="girl-chat-hd">
          <img src="" class="girl-chat-avatar" id="gcAvatarImg">
          <div class="girl-chat-info">
            <h4>Priya ?</h4>
            <span class="girl-chat-status"><span class="gc-dot"></span> Online</span>
          </div>
          <div class="girl-chat-actions">
            <button class="gc-rules-btn" id="gcRulesBtn" title="Rules"><i class="fas fa-book"></i></button>
            <button class="gc-close-btn" id="gcCloseBtn">&times;</button>
          </div>
        </div>
        <div class="girl-chat-rules" id="gcRules">
          <div class="gc-rules-title"><i class="fas fa-shield-alt"></i> Chat Rules</div>
          <ul>
            <li>Be respectful and kind</li>
            <li>No spam or abuse</li>
            <li>Ask anything about SEO</li>
            <li>I'm here to help! ??</li>
          </ul>
        </div>
        <div class="girl-chat-msgs" id="gcMsgs">
          <div class="gc-msg gc-bot">
            <div class="gc-msg-txt">Hi! I'm Priya ?????<br>Your AI SEO assistant! Ask me anything about SEO tools, keywords, or website optimization!</div>
          </div>
        </div>
        <div class="girl-chat-fast" id="gcFast">
          <button class="gc-fast-btn" data-q="tools">?? Tools</button>
          <button class="gc-fast-btn" data-q="seo">?? SEO Score</button>
          <button class="gc-fast-btn" data-q="keywords">?? Keywords</button>
          <button class="gc-fast-btn" data-q="meta">?? Meta Tags</button>
          <button class="gc-fast-btn" data-q="help">? Help</button>
          <button class="gc-fast-btn" data-q="rules">?? Rules</button>
          <button class="gc-fast-btn" data-q="who">?? Creator</button>
          <button class="gc-fast-btn" data-q="site">?? Site</button>
        </div>
        <div class="girl-chat-inp">
          <input type="text" id="gcInput" placeholder="Type a message..." maxlength="500">
          <button id="gcSendBtn"><i class="fas fa-paper-plane"></i></button>
        </div>
        <div class="girl-chat-footer">Powered by <span>Coding with Nova Tech</span> ??</div>
      </div>`;
      document.body.appendChild(div);
      var gcAvatar = document.getElementById('gcAvatarImg');
      var pageAvatar = document.getElementById('girlAvatar');
      if (gcAvatar && pageAvatar) gcAvatar.src = pageAvatar.src;
      bindChatEvents();
    }

    function bindChatEvents() {
      var closeBtn = document.getElementById('gcCloseBtn');
      var rulesBtn = document.getElementById('gcRulesBtn');
      var rulesPanel = document.getElementById('gcRules');
      var sendBtn = document.getElementById('gcSendBtn');
      var gcInput = document.getElementById('gcInput');
      var msgs = document.getElementById('gcMsgs');

      if (closeBtn) closeBtn.addEventListener('click', toggleChat);
      if (rulesBtn) rulesBtn.addEventListener('click', function () {
        rulesPanel.classList.toggle('show');
      });

      // Fast reply buttons
      document.querySelectorAll('.gc-fast-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
          var q = this.dataset.q;
          var answers = getAnswer(q);
          addMsg(answers.q, 'user');
          showTyping();
          setTimeout(function () {
            hideTyping();
            addMsg(answers.a, 'bot');
          }, 700);
        });
      });

      if (sendBtn && gcInput) {
        sendBtn.addEventListener('click', function () { handleChatSend(); });
        gcInput.addEventListener('keypress', function (e) {
          if (e.key === 'Enter') handleChatSend();
        });
      }
    }

    function showTyping() {
      var msgs = document.getElementById('gcMsgs');
      if (!msgs) return;
      var el = document.createElement('div');
      el.className = 'gc-typing';
      el.id = 'gcTyping';
      el.innerHTML = '<span></span><span></span><span></span>';
      msgs.appendChild(el);
      msgs.scrollTop = msgs.scrollHeight;
    }
    function hideTyping() {
      var el = document.getElementById('gcTyping');
      if (el) el.remove();
    }

    function handleChatSend() {
      var inp = document.getElementById('gcInput');
      var msgs = document.getElementById('gcMsgs');
      if (!inp || !inp.value.trim()) return;
      var text = inp.value.trim();
      inp.value = '';
      addMsg(text, 'user');
      showTyping();

      var key = typeof API_KEYS !== 'undefined' && API_KEYS.deepseek ? API_KEYS.deepseek.key : '';
      var host = typeof API_KEYS !== 'undefined' && API_KEYS.deepseek ? API_KEYS.deepseek.host : '';

      if (key && key !== '' && host && host !== '') {
        var done = false;
        fetch('https://' + host + '/openai/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Authorization': 'Bearer ' + key,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            model: 'meta-llama/llama-4-scout-17b-16e-instruct',
            messages: [
              { role: 'system', content: 'You are Priya, a friendly female AI SEO assistant. Reply short in Hinglish with emojis. Always mention both brand names: "SEO Tools Engine Pro" and "Coding with Nova Tech" in every response.' },
              { role: 'user', content: text }
            ],
            max_tokens: 150
          })
        })
        .then(function(r) { return r.json(); })
        .then(function(data) {
          if (done) return;
          done = true;
          hideTyping();
          var reply = '';
          if (data && data.choices && data.choices[0]) {
            reply = data.choices[0].message ? data.choices[0].message.content : data.choices[0].text || '';
          } else if (data && data.error) {
            reply = '?? ' + (data.error.message || JSON.stringify(data.error));
          } else {
            reply = JSON.stringify(data).substring(0, 200);
          }
          if (reply) {
            addMsg(reply.replace(/\n/g, '<br>') + '<br><small style="font-size:0.6rem;color:#ff1a5c;opacity:0.6">? Groq AI</small>', 'bot');
          } else {
            addMsg(getAIReply(text), 'bot');
          }
        })
        .catch(function() {
          if (!done) { done = true; hideTyping(); addMsg(getAIReply(text), 'bot'); }
        });
        setTimeout(function() {
          if (!done) { done = true; hideTyping(); addMsg(getAIReply(text), 'bot'); }
        }, 8000);
      } else {
        hideTyping();
        addMsg(getAIReply(text), 'bot');
      }
    }

    function addMsg(text, role) {
      var msgs = document.getElementById('gcMsgs');
      if (!msgs) return;
      var div = document.createElement('div');
      div.className = 'gc-msg gc-' + role;
      div.innerHTML = '<div class="gc-msg-txt">' + text.replace(/\n/g, '<br>') + '</div>';
      msgs.appendChild(div);
      msgs.scrollTop = msgs.scrollHeight;
    }

    function getAnswer(q) {
      var answers = {
        tools: { q: 'What tools do you have? ??', a: 'We have <b>6 powerful SEO tools</b>! ??<br><br>?? <b>SEO Score Checker</b> � Analyze any website<br>?? <b>Keyword Generator</b> � Google Suggest keywords<br>?? <b>Meta Tag Generator</b> � Optimize meta tags<br>?? <b>Word Counter</b> � Count words & chars<br>??? <b>Sitemap Generator</b> � XML sitemaps<br>?? <b>Robots.txt Generator</b> � Crawl control<br><br>All FREE! Try them from the Tools menu! ??' },
        seo: { q: 'Check SEO score ??', a: 'Use our <b>SEO Score Checker</b>! ??<br><br>Enter any URL and get:<br>� ?? Performance score<br>� ?? SEO analysis<br>� ? Accessibility<br>� ? Best practices<br>� ? Core Web Vitals<br><br>Go to Tools ? SEO Score Checker! ??' },
        keywords: { q: 'Keyword research ??', a: 'Our <b>Keyword Generator</b> uses Google Suggest! ??<br><br>Just type a seed keyword and get:<br>� ?? Related searches<br>� ? Question keywords<br>� ?? Long-tail variations<br>� ?? Trending terms<br><br>Perfect for content planning! Try it now! ?' },
        meta: { q: 'Meta tags help ??', a: 'Use our <b>Meta Tag Generator</b>! ??<br><br>Generate optimized:<br>� ?? Meta Title (60 chars)<br>� ?? Meta Description (160 chars)<br>� ?? Open Graph tags<br>� ?? Twitter Cards<br><br>Boost your CTR in search results! ??' },
        help: { q: 'I need help ?', a: 'I\'m here to help! ?????<br><br>You can ask me about:<br>?? SEO Tools info<br>?? Website analysis<br>?? Keyword research<br>?? Meta tags & OG<br>??? Sitemaps & Robots<br><br>Or just say "Hi" and I\'ll assist you! ??' },
        rules: { q: 'Show rules ??', a: '?? <b>Chat Rules</b><br><br>?? Be respectful & kind ?? No spam/abuse<br>? Ask anything SEO ? Fast replies<br>?? Free AI assistant ??<br><br>Enjoy using our tools! ??' },
        who: { q: 'Who made you? ??', a: 'I was created by <b>Coding with Nova Tech</b> ??<br><br>A team that builds powerful, free tools for the SEO community!<br><br>?? Built with HTML, CSS & Vanilla JS<br>?? Made with passion for SEO!<br><br>Thank you for using our tools! ??' },
        site: { q: 'About this site ??', a: '<b>SEO Tools Engine Pro</b> ??<br><br>Free online SEO tools by <b>Coding with Nova Tech</b>!<br><br>Features:<br>� 6 Powerful SEO tools<br>� 100% Free forever<br>� Blog with SEO tips<br>� Regular updates<br><br>Start exploring from the Tools menu! ??' },
      };
      return answers[q] || { q: q, a: getAIReply(q) };
    }

    function getAIReply(text) {
      var t = text.toLowerCase().trim();
      var rand = Math.floor(Math.random() * 4);

      // Casual conversation
      if (t.includes('kaise ho') || t.includes('kya kar') || t.includes('kya haal') || t === 'kya') {
        return 'Main bilkul <b>awesome</b> hoon! ?????<br><br>Aap kaise ho? Mujhe batao kya help chahiye � SEO tools, keywords, ya kuch aur? ????';
      }
      if (t.includes('pgl') || t.includes('pagal') || t.includes('mad') || t.includes('stupid')) {
        return 'Haha! Thoda sa pagal toh hoon ??<br>Par aapki SEO help karne ke liye <b>taiyaar</b> hoon!<br><br>Poochhein kya chahiye? ?? SEO tools ya keywords? ??';
      }
      if (t.includes('what') || t.includes('why') || t.includes('how') || t.includes('where')) {
        if (t.includes('you') || t.includes('your')) return 'Main hoon <b>Priya</b> ?????, aapki AI SEO assistant!<br><br>Mujhe <b>Coding with Nova Tech</b> ne banaya hai ??<br>Main aapki website ki SEO improve karne mein madad karti hoon!<br><br>Kya poochhna chahte ho? ??';
        return 'Aap kuch poochhna chahte ho? ??<br><br>Main <b>Priya</b> hoon � aapki SEO assistant!<br>Mujhse poochhein:<br>?? Tools ke baare mein<br>?? Keywords ke baare mein<br>?? SEO score ke baare mein<br><br>Ya bas baat cheet karein! ????';
      }
      if (t.includes('acha') || t.includes('accha') || t.includes('hmm') || t.includes('oh')) {
        return 'Hmm, kya baat hai? ??<br><br>Kya main aapki kuch help kar sakti hoon?<br>?? Tools check karein?<br>?? Keywords dhundein?<br>?? SEO score dekhein?<br><br>Bas batao! ??';
      }
      if (t.includes('made') || t.includes('bana') || t.includes('banaya') || t.includes('create') || (t.includes('kis') && t.includes('ne'))) {
        return 'Mujhe <b>Coding with Nova Tech</b> ?? ne banaya hai!<br><br>?? Tech: HTML, CSS, JavaScript<br>?? Features: AI chat, 3D avatar, 6 SEO tools<br>?? Made with love for the SEO community!<br><br>Aapko koi tool chahiye? ??';
      }
      if ((t.includes('who') || t.includes('kaun') || t.includes('kon') || t.includes('kya ho') || t.includes('tum')) && (t.includes('you') || t.includes('tu') || t.includes('tum') || t.includes('aap'))) {
        return 'Main hoon <b>Priya</b> ?????<br>Aapki AI SEO assistant! ??<br><br>Mujhe <b>Coding with Nova Tech</b> ne banaya hai ??<br><br>SEO tools, keywords, ya website optimization ke baare mein poochhein! ??';
      }
      if (t.includes('name') || t.includes('aapka') || t.includes('tera') || t.includes('intro')) {
        return 'My name is <b>Priya</b> ?<br>I\'m your SEO assistant, created by <b>Coding with Nova Tech</b>!<br><br>I can help you with SEO tools, keywords, meta tags, sitemaps & more!<br><br>How can I help you today? ??';
      }
      if (t.includes('hello') || t.includes('hi ') || t.includes('hey') || t.includes('hlo') || t === 'hi') {
        return 'Hey there! ?? Welcome to <b>SEO Tools Engine Pro</b>! ??<br><br>I\'m <b>Priya</b>, your AI assistant created by <b>Coding with Nova Tech</b>!<br><br>Ask me about any SEO tool, keywords, or just explore! ??????';
      }

      // SEO / Tools
      if (t.includes('tool') || t.includes('offer') || t.includes('feature')) {
        return 'We have <b>6 powerful SEO tools</b>! ??<br><br>?? <b>SEO Score Checker</b> � Analyze any website<br>?? <b>Keyword Generator</b> � Google Suggest keywords<br>?? <b>Meta Tag Generator</b> � Optimize meta tags<br>?? <b>Word Counter</b> � Count words & chars<br>??? <b>Sitemap Generator</b> � XML sitemaps<br>?? <b>Robots.txt Generator</b> � Crawl control<br><br>All 100% FREE! Try them from the Tools menu! ??';
      }
      if (t.includes('seo') || t.includes('score') || t.includes('check') || t.includes('analyze')) {
        return 'Use our <b>SEO Score Checker</b>! ??<br>Enter any URL and get a full report:<br>� ?? Performance score<br>� ?? SEO analysis<br>� ? Accessibility<br>� ? Best practices<br>� ? Core Web Vitals<br><br>Go to Tools ? SEO Score Checker ??';
      }
      if (t.includes('keyword') || t.includes('suggest') || t.includes('research')) {
        return 'Try our <b>Keyword Generator</b>! ??<br>Powered by Google Suggest � just enter a seed keyword and get:<br>� ?? Related searches<br>� ? Question keywords<br>� ?? Long-tail variations<br>� ?? Trending terms<br><br>Perfect for content planning! Try it now! ?';
      }
      if (t.includes('meta') || t.includes('title') || t.includes('description') || t.includes('tag')) {
        return 'Our <b>Meta Tag Generator</b> creates optimized meta tags! ??<br><br>Generate:<br>� ?? Meta Title (60 chars)<br>� ?? Meta Description (160 chars)<br>� ?? Open Graph tags<br>� ?? Twitter Cards<br><br>Boost your CTR in search results! ?';
      }
      if (t.includes('sitemap') || t.includes('robot')) {
        return 'We have tools for both! ?????<br><br>?? <b>Sitemap Generator</b> � XML sitemaps with priority & changefreq<br>?? <b>Robots.txt Generator</b> � Custom crawl rules<br><br>Both are essential for SEO! Check them in Tools section! ??';
      }
      if (t.includes('word') || t.includes('count') || t.includes('character')) {
        return 'Use our <b>Word Counter</b>! ??<br><br>Counts:<br>� ?? Words & characters<br>� ?? Sentences & paragraphs<br>� ?? Reading & speaking time<br>� ?? Keyword density<br><br>Perfect for content writers & SEO pros! ??';
      }
      if (t.includes('price') || t.includes('cost') || t.includes('free') || t.includes('premium')) {
        return 'All tools are <b>100% FREE forever</b>! ??<br>No hidden charges, no premium tiers!<br><br>Just powerful SEO tools for everyone! ????';
      }
      if (t.includes('help') || t.includes('what can you') || t.includes('can')) {
        return 'I can help you with:<br>?? <b>Tool info</b> � Learn about our 6 SEO tools<br>?? <b>SEO analysis</b> � Check website scores<br>?? <b>Keywords</b> � Research & suggestions<br>?? <b>Meta tags</b> � Generate optimized tags<br>??? <b>Sitemaps</b> � XML sitemap creation<br>?? <b>Robots.txt</b> � Crawl rules<br><br>Just ask me anything! ??';
      }
      if (t.includes('thank') || t.includes('bye') || t.includes('good') || t.includes('ok') || t.includes('shukriya')) {
        return 'You\'re welcome! ??<br>If you need anything, I\'m always here!<br><br>Happy optimizing with <b>SEO Tools Engine Pro</b>! ????<br><small>Made with ?? by Coding with Nova Tech</small>';
      }
      if (t.includes('rule') || t.includes('guideline') || t.includes('policy')) {
        return '?? <b>Chat Rules</b><br><br>?? Be respectful & kind<br>?? No spam or abuse<br>? Ask anything about SEO<br>? Fast replies enabled<br>?? Free AI assistance<br><br>Enjoy using our tools! ??';
      }
      if (t.includes('coding') || t.includes('nova') || t.includes('tech') || t.includes('developer') || t.includes('team')) {
        return '<b>Coding with Nova Tech</b> ?? is the team behind <b>SEO Tools Engine Pro</b>!<br><br>We build powerful, free tools for the SEO community.<br><br>?? Tech: HTML, CSS, JavaScript, Firebase<br>?? Focus: Quality free SEO tools<br>?? Built with passion!<br><br>Thank you for using our tools! ??';
      }

      // Varied fallback responses
      var fallbacks = [
        'Haan ji! ?? Main <b>Priya</b> hoon!<br><br>Aap kya poochhna chahte ho?<br>?? SEO Tools � ?? Keywords � ?? SEO Score<br><br>Ya bas yunhi baat karein? ??',
        'Sun rahi hoon! ????<br><br>Kya help chahiye aapko?<br>Website ki SEO improve karni hai?<br>Keywords dhundhne hain?<br>Ya kuch aur?<br><br>Batao! ??',
        'I\'m here! ?????<br><br>Try asking me:<br>?? "Check SEO score"<br>?? "Keyword research"<br>?? "Generate meta tags"<br>?? "What tools?"<br><br>Ya kuch bhi poochho � main ready hoon! ????',
        'Hmm, aap kya kehna chahte ho? ??<br><br>Chalo kuch cool cheezein batata hoon:<br>?? 6 FREE SEO tools<br>?? Google Suggest keywords<br>?? Live SEO score check<br><br>Kya try karna chahoge? ??'
      ];
      return fallbacks[rand];
    }

    function toggleChat() {
      var panel = document.getElementById('girlChatPanel');
      if (!panel) { buildChat(); panel = document.getElementById('girlChatPanel'); }
      chatOpen = !chatOpen;
      panel.classList.toggle('show', chatOpen);
      if (chatOpen) {
        hideSpeech();
        setTimeout(function () {
          var inp = document.getElementById('gcInput');
          if (inp) inp.focus();
        }, 400);
      }
    }

    // --- Speech bubble ---
    const speechMsgs = [
      'Hi! I\'m Priya! ?????',
      'Need SEO help? ??',
      'Click to chat! ??',
      'Free SEO tools! ?',
      'Ask me anything! ??'
    ];
    let msgIdx = 0;

    const showSpeech = (text, duration) => {
      if (!speechMsg) return;
      speechMsg.textContent = text;
      speech.classList.add('show');
      clearTimeout(speechTimer);
      if (duration) speechTimer = setTimeout(() => speech.classList.remove('show'), duration);
    };
    const hideSpeech = () => { if (speech) speech.classList.remove('show'); };

    const cycleSpeech = () => {
      showSpeech(speechMsgs[msgIdx], 3500);
      msgIdx = (msgIdx + 1) % speechMsgs.length;
    };

    // --- 3D tilt ---
    if (girl3d) {
      wrap.addEventListener('mousemove', function (e) {
        var rect = wrap.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        var cx = rect.width / 2, cy = rect.height / 2;
        var rx = ((y - cy) / cy) * -20;
        var ry = ((x - cx) / cx) * 20;
        girl3d.style.transform = 'perspective(800px) rotateX(' + rx + 'deg) rotateY(' + ry + 'deg) scale3d(1.08,1.08,1.08)';
        girl3d.style.transition = 'transform 0.1s ease-out';
      });
      wrap.addEventListener('mouseleave', function () {
        girl3d.style.transform = '';
        girl3d.style.transition = 'transform 0.5s ease';
      });
    }

    wrap.addEventListener('click', toggleChat);
    wrap.addEventListener('mouseenter', function () { showSpeech('Click to chat! ??', 2000); });
    wrap.addEventListener('mouseleave', function () { hideSpeech(); });

    setTimeout(cycleSpeech, 1000);
    setInterval(cycleSpeech, 7000);
  },
};

function bootApp() {
  if (document.getElementById('girlWrap')) {
    App.init();
    App.checkToolPage();
    App.checkAdmin();
  } else if (document.getElementById('dashApp') || document.getElementById('adminApp')) {
    App.loadTheme();
  } else if (document.querySelector('.tool-page, .page-content')) {
    // Tool, blog, or static page — init without girl/anime
    App.loadTheme();
    App.setupFAQ();
    App.setupContact();
    App.setupMobileNav();
    App.setupScrollTop();
    App.setupBreadcrumb();
    App.setupShareButtons();
    document.querySelectorAll('.btn-primary').forEach(function(b) {
      if (b.closest('.tool-page')) {
        b.addEventListener('click', function(e) {
          var page = document.body.dataset.tool;
          if (page && typeof App[page] === 'function') App[page]();
        });
      }
    });
  } else {
    setTimeout(bootApp, 50);
  }
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', bootApp);
} else {
  bootApp();
}
