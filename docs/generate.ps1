$base = "C:\Users\ayush\OneDrive\ads\SEO-Tools-Engine-Pro"

$head = @'
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="index, follow">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <link rel="stylesheet" href="../assets/css/style.css">
  <title>__TITLE__</title>
</head>
<body>
  <nav class="nav">
    <div class="nav-inner">
      <a href="/" class="nav-brand"><i class="fas fa-rocket"></i> SEO Tools Pro</a>
      <div class="nav-links">
        <a href="/">Home</a>
        <a href="/#tools">Tools</a>
        <a href="/#blog">Blog</a>
        <a href="../about.html">About</a>
        <a href="../contact.html">Contact</a>
      </div>
      <div class="nav-actions">
        <button class="theme-btn" id="themeBtn" onclick="App.toggleTheme()" aria-label="Theme"><i class="fas fa-sun"></i></button>
        <button class="menu-btn" onclick="document.querySelector('.nav-links')?.classList.toggle('active')" aria-label="Menu"><i class="fas fa-bars"></i></button>
      </div>
    </div>
  </nav>
  __CONTENT__
  <footer class="footer">
    <div class="footer-grid">
      <div class="footer-col"><h4>SEO Tools Engine Pro</h4><p style="opacity:0.7;font-size:0.85rem">Free professional SEO tools.</p></div>
      <div class="footer-col"><h4>Tools</h4><ul><li><a href="../tools/seo-score.html">SEO Score</a></li><li><a href="../tools/keyword-generator.html">Keyword Generator</a></li><li><a href="../tools/meta-generator.html">Meta Generator</a></li></ul></div>
      <div class="footer-col"><h4>Company</h4><ul><li><a href="../about.html">About</a></li><li><a href="../contact.html">Contact</a></li><li><a href="../privacy.html">Privacy</a></li></ul></div>
    </div>
    <div class="footer-bottom">&copy; 2026 SEO Tools Engine Pro</div>
  </footer>
  <div class="toast" id="toast"></div>
  <script src="../assets/js/main.js"></script>
</body>
</html>
'@

$tools = @(
  @{file="tools\seo-score.html";title="SEO Score Checker - Free Online SEO Analysis Tool";desc="Free SEO Score Checker to analyze your webpage. Check meta tags, headings, images, mobile friendliness and speed optimization.";h1="SEO Score Checker";seo="Analyze your webpage's SEO health instantly. Our SEO Score Checker evaluates meta tags, heading structure, image optimization, mobile readiness, and speed factors to give you a comprehensive SEO score out of 100.";form='<div class="form-group"><label>Enter Your URL</label><input type="url" id="seoUrl" placeholder="https://example.com" value="https://example.com"></div><button class="btn btn-primary" onclick="App.seoScore()"><i class="fas fa-search"></i> Analyze SEO</button><div class="result-box" id="seoResult"><div class="result-label">SEO Score</div><div class="result-value" id="seoScore">0/100</div><div class="result-detail"><strong>Meta Tags:</strong> <span id="seoMeta">-</span></div><div class="result-detail"><strong>Headings:</strong> <span id="seoHead">-</span></div><div class="result-detail"><strong>Images:</strong> <span id="seoImg">-</span></div><div class="result-detail"><strong>Mobile Ready:</strong> <span id="seoMobile">-</span></div><div class="result-detail"><strong>Speed:</strong> <span id="seoSpeed">-</span></div></div>';faq='<div class="faq-item"><button class="faq-q">How is SEO score calculated? <i class="fas fa-chevron-down"></i></button><div class="faq-a">We analyze meta tags, headings, image optimization, mobile readiness, and speed factors to generate a score out of 100.</div></div><div class="faq-item"><button class="faq-q">Is this tool accurate? <i class="fas fa-chevron-down"></i></button><div class="faq-a">It provides a solid estimate. For complete analysis, combine with Google Search Console.</div></div>'},
  @{file="tools\keyword-generator.html";title="Keyword Generator - Free SEO Keyword Ideas Tool";desc="Free Keyword Generator tool to find hundreds of LSI and long-tail keywords. Perfect for SEO content planning and blog research.";h1="Keyword Generator";seo="Generate hundreds of keyword ideas from a single seed keyword. Our Keyword Generator creates LSI keywords, long-tail variations, and related search terms to help you plan your SEO content strategy.";form='<div class="form-group"><label>Enter Seed Keyword</label><input type="text" id="kwSeed" placeholder="e.g., seo tips" value="seo tips"></div><button class="btn btn-primary" onclick="App.generateKeywords()"><i class="fas fa-key"></i> Generate Keywords</button><div class="result-box" id="kwResult"><div class="result-detail"><strong>Total:</strong> <span id="kwCount">0 keywords</span></div><div id="kwList" style="margin-top:12px"></div></div>';faq='<div class="faq-item"><button class="faq-q">How many keywords can I generate? <i class="fas fa-chevron-down"></i></button><div class="faq-a">You can generate 20+ keyword ideas per seed keyword. Use different seed keywords for more variations.</div></div>'},
  @{file="tools\meta-generator.html";title="Meta Tag Generator - Free SEO Meta Tags Generator";desc="Free Meta Tag Generator to create optimized title tags, meta descriptions, Open Graph and Twitter Cards for better SEO.";h1="Meta Tag Generator";seo="Create perfectly optimized meta tags for your web pages. Our Meta Tag Generator helps you craft SEO-friendly title tags, meta descriptions, Open Graph tags, and Twitter Card markup.";form='<div class="form-group"><label>Page Title</label><input type="text" id="mtTitle" placeholder="Enter page title" value="Your Page Title"></div><div class="form-group"><label>Meta Description</label><textarea id="mtDesc" placeholder="Enter description (max 160 chars)">Learn about this topic. Complete guide, tips, and best practices for beginners and experts.</textarea></div><div class="form-group"><label>Page URL</label><input type="url" id="mtUrl" placeholder="https://example.com/page" value="https://example.com/page"></div><div class="form-group"><label>Keywords (comma separated)</label><input type="text" id="mtKeywords" placeholder="keyword1, keyword2" value="SEO, guide, tips"></div><button class="btn btn-primary" onclick="App.generateMeta()"><i class="fas fa-code"></i> Generate Meta Tags</button><div class="result-box" id="mtResult"><h4 style="margin-bottom:8px">Preview</h4><div style="border:1px solid var(--border);padding:12px;border-radius:8px;margin-bottom:12px"><div style="color:var(--success);font-size:0.82rem" id="mtPreviewUrl">-</div><div style="font-size:1rem;font-weight:600;color:var(--text)" id="mtPreviewTitle">-</div><div style="font-size:0.85rem;color:var(--text-secondary)" id="mtPreviewDesc">-</div></div><div class="result-label">Generated Code</div><div class="result-raw" id="mtOutput"></div></div>';faq='<div class="faq-item"><button class="faq-q">What are meta tags? <i class="fas fa-chevron-down"></i></button><div class="faq-a">Meta tags are HTML elements that provide information about your webpage to search engines and social platforms.</div></div>'},
  @{file="tools\word-counter.html";title="Word Counter - Free Online Word Count Tool";desc="Free Word Counter tool to count words, characters, sentences, paragraphs and estimate reading time.";h1="Word Counter";seo="Count words, characters, sentences, and paragraphs instantly. Our Word Counter also estimates reading time and provides detailed text statistics.";form='<div class="form-group"><label>Enter Your Text</label><textarea id="wcText" placeholder="Paste your text here..." style="min-height:200px">This is a sample text. Count its words and characters using this tool. It will show you detailed statistics including reading time.</textarea></div><button class="btn btn-primary" onclick="App.countWords()"><i class="fas fa-calculator"></i> Count Words</button><div class="result-box" id="wcResult"><div class="result-detail"><strong>Words:</strong> <span id="wcWords">0</span></div><div class="result-detail"><strong>Characters (with spaces):</strong> <span id="wcChars">0</span></div><div class="result-detail"><strong>Characters (no spaces):</strong> <span id="wcCharsNS">0</span></div><div class="result-detail"><strong>Sentences:</strong> <span id="wcSentences">0</span></div><div class="result-detail"><strong>Paragraphs:</strong> <span id="wcParagraphs">0</span></div><div class="result-detail"><strong>Reading Time:</strong> <span id="wcReadTime">0 min</span></div></div>';faq='<div class="faq-item"><button class="faq-q">How is reading time calculated? <i class="fas fa-chevron-down"></i></button><div class="faq-a">Reading time is calculated at 200 words per minute, the average adult reading speed.</div></div>'},
  @{file="tools\sitemap-generator.html";title="Sitemap Generator - Free XML Sitemap Generator Tool";desc="Free XML Sitemap Generator to create sitemaps for your website. Improve Google indexing with proper sitemaps.";h1="Sitemap Generator";seo="Generate XML sitemaps for your website instantly. Our Sitemap Generator creates properly formatted XML sitemaps with correct namespace, lastmod dates, and priority settings.";form='<div class="form-group"><label>Enter URLs (one per line)</label><textarea id="smUrls" placeholder="https://example.com/&#10;https://example.com/about&#10;https://example.com/contact" style="min-height:150px">https://example.com/&#10;https://example.com/about&#10;https://example.com/blog</textarea></div><button class="btn btn-primary" onclick="App.generateSitemap()"><i class="fas fa-sitemap"></i> Generate Sitemap</button><div class="result-box" id="smResult"><div class="result-detail" id="smCount">-</div><div class="result-raw" id="smOutput"></div></div>';faq='<div class="faq-item"><button class="faq-q">What is a sitemap? <i class="fas fa-chevron-down"></i></button><div class="faq-a">A sitemap is an XML file that lists all pages on your website to help search engines discover and index your content.</div></div>'},
  @{file="tools\robots-generator.html";title="Robots.txt Generator - Free Robots.txt File Generator";desc="Free Robots.txt Generator to create custom robots.txt files with allow/disallow rules for search engine crawlers.";h1="Robots.txt Generator";seo="Create custom robots.txt files for your website. Our generator helps you control how search engine crawlers access your site with proper allow/disallow rules.";form='<div class="form-group"><label>User-agent</label><input type="text" id="rbAgent" value="*" placeholder="*"></div><div class="form-group"><label>Allow Paths (one per line)</label><textarea id="rbAllow" placeholder="/public/&#10;/blog/" style="min-height:60px">/</textarea></div><div class="form-group"><label>Disallow Paths (one per line)</label><textarea id="rbDisallow" placeholder="/admin/&#10;/private/" style="min-height:60px">/admin/</textarea></div><div class="form-group"><label>Sitemap URL (optional)</label><input type="url" id="rbSitemap" placeholder="https://example.com/sitemap.xml" value="https://example.com/sitemap.xml"></div><button class="btn btn-primary" onclick="App.generateRobots()"><i class="fas fa-robot"></i> Generate Robots.txt</button><div class="result-box" id="rbResult"><div class="result-raw" id="rbOutput"></div></div>';faq='<div class="faq-item"><button class="faq-q">What is robots.txt? <i class="fas fa-chevron-down"></i></button><div class="faq-a">Robots.txt tells search engine crawlers which pages they can or cannot access on your website.</div></div>'}
)

$blogPosts = @(
  @{id="seo-tips";title="10 Essential SEO Tips for 2026";content="<p>SEO in 2026 requires a focus on user experience, Core Web Vitals, and AI-powered search. Here are 10 essential tips:</p><h2>1. Focus on Core Web Vitals</h2><p>Google's Core Web Vitals (LCP, FID, CLS) remain crucial ranking factors. Optimize loading speed, interactivity, and visual stability.</p><h2>2. Create Topic Clusters</h2><p>Instead of individual keywords, create comprehensive topic clusters with pillar pages and supporting articles to establish authority.</p><h2>3. Optimize for Voice Search</h2><p>With growing voice assistant usage, optimize for conversational queries and featured snippets.</p><h2>4. Prioritize Mobile Experience</h2><p>Google uses mobile-first indexing. Ensure your site is fully responsive and fast on mobile devices.</p><h2>5. Build Quality Backlinks</h2><p>Focus on earning backlinks from authoritative sites through guest posting, digital PR, and creating linkable assets.</p><h2>6. Improve User Engagement</h2><p>Low bounce rates, high time-on-page, and good click-through rates signal quality to Google.</p><h2>7. Use Structured Data</h2><p>Implement schema markup to help Google understand your content and enable rich snippets.</p><h2>8. Optimize Images</h2><p>Use next-gen formats (WebP), proper alt text, and lazy loading for better performance.</p><h2>9. Write for Humans First</h2><p>Create content that answers user questions comprehensively. AI can help research but human touch matters.</p><h2>10. Monitor and Adapt</h2><p>Use Google Search Console and Analytics to track performance and adapt your strategy continuously.</p>";tag="SEO"},
  @{id="blogging-guide";title="Blogging Guide: Start a Profitable Blog in 2026";content="<p>Starting a blog in 2026 is easier than ever, but building a profitable one requires strategy. Here's your complete guide.</p><h2>Choose Your Niche</h2><p>Pick a niche you're passionate about with good monetization potential. Popular niches include personal finance, health, tech, and lifestyle.</p><h2>Set Up Your Blog</h2><p>Choose a domain name, reliable hosting, and a CMS like WordPress or Blogger. Focus on speed and mobile optimization from day one.</p><h2>Create Quality Content</h2><p>Publish comprehensive, well-researched content that solves problems. Aim for at least 1500 words per post with proper formatting.</p><h2>Monetization Strategies</h2><p>Diversify income through display ads, affiliate marketing, digital products, sponsored posts, and membership programs.</p><h2>Promote Your Blog</h2><p>Use SEO, social media, email marketing, and guest posting to drive traffic. Build an email list from the start.</p><h2>Track and Improve</h2><p>Monitor analytics, identify top-performing content, and double down on what works.</p>";tag="Blogging"},
  @{id="keyword-research";title="Keyword Research: Complete Guide for SEO";content="<p>Keyword research is the foundation of SEO. Here's how to find the right keywords for your content strategy.</p><h2>What is Keyword Research?</h2><p>Keyword research is the process of finding terms your target audience uses in search engines to discover content like yours.</p><h2>Types of Keywords</h2><p>Short-tail (1-2 words) have high volume but high competition. Long-tail (3-5 words) have lower volume but higher conversion rates.</p><h2>How to Research Keywords</h2><p>Use tools like Google Keyword Planner, Ahrefs, Semrush, or our free Keyword Generator to find keyword ideas.</p><h2>Analyze Keyword Difficulty</h2><p>Check competition level before targeting a keyword. Start with low-competition keywords if your site is new.</p><h2>Map Keywords to Content</h2><p>Create a content plan mapping primary and secondary keywords to specific blog posts and pages.</p><h2>Track Rankings</h2><p>Monitor your keyword rankings using Google Search Console and adjust your strategy based on performance data.</p>";tag="SEO"},
  @{id="google-ranking";title="How to Rank Higher on Google in 2026";content="<p>Ranking higher on Google requires a combination of technical SEO, quality content, and user experience optimization.</p><h2>Technical SEO Foundation</h2><p>Ensure your site is crawlable, indexable, and loads quickly. Use XML sitemaps and proper URL structure.</p><h2>Content Quality Matters</h2><p>Google's algorithms prioritize helpful, original content that demonstrates E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness).</p><h2>On-Page Optimization</h2><p>Optimize title tags, meta descriptions, headings, and image alt text. Include target keywords naturally.</p><h2>Build Authority</h2><p>Earn backlinks from reputable sites, get mentioned in industry publications, and build your brand presence.</p><h2>User Experience Signals</h2><p>Google considers page speed, mobile-friendliness, and Core Web Vitals as ranking factors.</p><h2>Regular Updates</h2><p>Keep your content fresh and updated. Google prefers recently updated content for current topics.</p>";tag="Ranking"},
  @{id="onpage-seo";title="On-Page SEO Checklist for 2026";content="<p>On-page SEO is everything you can do on your website to rank higher. Follow this comprehensive checklist.</p><h2>Title Tags</h2><p>Include primary keyword near the beginning. Keep under 60 characters. Make it compelling for clicks.</p><h2>Meta Descriptions</h2><p>Write unique meta descriptions under 160 characters with keywords and a call-to-action.</p><h2>Heading Structure</h2><p>Use one H1 per page, H2s for main sections, and H3s for subsections. Include keywords naturally.</p><h2>URL Structure</h2><p>Use short, descriptive URLs with hyphens. Avoid numbers and special characters.</p><h2>Image Optimization</h2><p>Use descriptive file names, alt text, compress images, and use responsive images with srcset.</p><h2>Internal Linking</h2><p>Link to related content within your site. Use descriptive anchor text.</p><h2>Content Quality</h2><p>Write comprehensive content that satisfies search intent. Include tables, lists, and media.</p><h2>Schema Markup</h2><p>Implement relevant schema types (Article, FAQ, HowTo) for rich snippets.</p>";tag="SEO"},
  @{id="offpage-seo";title="Off-Page SEO Strategies That Work";content="<p>Off-page SEO refers to actions taken outside your website to improve rankings. Here are proven strategies.</p><h2>Link Building</h2><p>Earn high-quality backlinks through guest posting, broken link building, and creating shareable content.</p><h2>Social Signals</h2><p>While not direct ranking factors, social shares increase visibility and drive traffic that leads to links.</p><h2>Brand Mentions</h2><p>Unlinked brand mentions can be converted into backlinks. Monitor mentions using tools like Google Alerts.</p><h2>Guest Posting</h2><p>Write for authoritative sites in your niche. Include relevant links back to your content.</p><h2>Local SEO</h2><p>Optimize Google Business Profile, get reviews, and build local citations for location-based businesses.</p><h2>Influencer Outreach</h2><p>Collaborate with influencers in your niche for mentions, shares, and backlinks.</p>";tag="SEO"},
  @{id="technical-seo";title="Technical SEO: Complete Guide for Beginners";content="<p>Technical SEO ensures search engines can crawl, index, and render your website properly.</p><h2>Website Crawling</h2><p>Use robots.txt and XML sitemaps to guide search engine crawlers to your important pages.</p><h2>Indexing</h2><p>Ensure all important pages are indexable. Use noindex for thin content, admin pages, and duplicate content.</p><h2>Page Speed</h2><p>Optimize loading time through image compression, caching, minification, and CDN usage.</p><h2>Mobile Optimization</h2><p>Use responsive design, proper viewport settings, and touch-friendly navigation for mobile users.</p><h2>Core Web Vitals</h2><p>Optimize LCP (under 2.5s), FID (under 100ms), and CLS (under 0.1) for better rankings.</p><h2>Structured Data</h2><p>Implement JSON-LD schema markup for better visibility in search results.</p><h2>HTTPS Security</h2><p>Use SSL certificates to secure your site. Google prefers HTTPS sites.</p>";tag="SEO"},
  @{id="content-writing";title="Content Writing Tips for SEO";content="<p>SEO content writing combines reader-friendly prose with search engine optimization. Here's how to master it.</p><h2>Understand Search Intent</h2><p>Before writing, understand what users want: informational, navigational, commercial, or transactional content.</p><h2>Keyword Placement</h2><p>Include primary keywords in title, first paragraph, headings, and naturally throughout the content.</p><h2>Content Structure</h2><p>Use short paragraphs, bullet points, subheadings, and white space for readability.</p><h2>Write Compelling Headlines</h2><p>Use power words, numbers, and emotional triggers. Test different headline variations.</p><h2>Add Value</h2><p>Go beyond surface-level information. Include original insights, data, examples, and actionable tips.</p><h2>Optimize Readability</h2><p>Write at a 7th-8th grade reading level. Use transition words and vary sentence length.</p><h2>Include Multimedia</h2><p>Add images, videos, infographics, and tables to enhance user engagement and time on page.</p><h2>Call-to-Action</h2><p>End each piece with a clear next step for the reader, like reading related content or subscribing.</p>";tag="Content"}
)

# Generate tool pages
foreach ($t in $tools) {
  $html = $head
  $html = $html.Replace('__TITLE__', $t.title)
  
  $toolContent = @"
  <div class="tool-page">
    <div class="tool-container">
      <div class="tool-box">
        <h1>$($t.h1)</h1>
        <p class="desc">$($t.seo)</p>
        $($t.form)
        <div class="btn-group">
          <button class="btn btn-secondary" onclick="App.toast('Share link copied!')"><i class="fas fa-share-alt"></i> Share</button>
        </div>
      </div>
      <div class="tool-box">
        <h3>$($t.h1) - FAQ</h3>
        <div class="faq">$($t.faq)</div>
      </div>
      <div class="tool-box">
        <h3>Related Tools</h3>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px">
"@
  
  foreach ($other in $tools) {
    if ($other.file -ne $t.file) {
      $name = ($other.h1)
      $relPath = $other.file.Replace("tools\","")
      $toolContent += "          <a href='$relPath' style='padding:10px;border:1px solid var(--border);border-radius:8px;text-align:center;font-size:0.85rem'>$name</a>`n"
    }
  }
  
  $toolContent += @'
        </div>
      </div>
    </div>
  </div>
'@
  
  $html = $html.Replace('__CONTENT__', $toolContent)
  $html | Out-File -FilePath "$base\$($t.file)" -Encoding utf8
  Write-Host "Created $($t.file)"
}

# Generate blog pages
foreach ($b in $blogPosts) {
  $html = $head
  $html = $html.Replace('__TITLE__', "$($b.title) - SEO Tools Engine Pro")
  
  $relatedArticles = $blogPosts | Where-Object { $_.id -ne $b.id } | Select-Object -First 4
  
  $blogContent = @"
  <article class="blog-page">
    <div class="blog-content">
      <div class="meta"><span>$($b.tag)</span><span>5 min read</span><span>June 2026</span></div>
      <h1>$($b.title)</h1>
      <div class="body">$($b.content)</div>
      
      <div style="margin-top:32px;padding:20px;background:var(--accent-light);border-radius:12px">
        <strong style="color:var(--accent)">Use our free tools:</strong><br>
        <a href="../tools/keyword-generator.html" style="font-size:0.9rem">Keyword Generator</a> &bull;
        <a href="../tools/meta-generator.html" style="font-size:0.9rem">Meta Tag Generator</a> &bull;
        <a href="../tools/seo-score.html" style="font-size:0.9rem">SEO Score Checker</a>
      </div>

      <h3 style="margin-top:32px">Related Articles</h3>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px">
"@
  
  foreach ($ra in $relatedArticles) {
    $blogContent += "        <a href='$($ra.id).html' style='padding:12px;border:1px solid var(--border);border-radius:8px;font-size:0.85rem'>$($ra.title)</a>`n"
  }
  
  $blogContent += @'
      </div>
      <div style="margin-top:32px;text-align:center">
        <a href="/#blog" style="color:var(--accent)">← Back to Blog</a>
      </div>
    </div>
  </article>
'@
  
  $html = $html.Replace('__CONTENT__', $blogContent)
  $html | Out-File -FilePath "$base\blog\$($b.id).html" -Encoding utf8
  Write-Host "Created blog/$($b.id).html"
}

# Generate static pages
$pages = @(
  @{file="about.html";title="About Us - SEO Tools Engine Pro";h1="About SEO Tools Engine Pro";content="<p>Welcome to SEO Tools Engine Pro, your complete resource for free professional SEO tools and guides.</p><h2>Our Mission</h2><p>We believe SEO tools should be accessible to everyone. Our mission is to provide high-quality, free SEO tools that help website owners, bloggers, and marketers improve their search engine rankings without expensive subscriptions.</p><h2>What We Offer</h2><p>6 powerful SEO tools including SEO Score Checker, Keyword Generator, Meta Tag Generator, Word Counter, Sitemap Generator, and Robots.txt Generator. Plus 8+ comprehensive SEO guides and tutorials.</p><h2>Why Choose Us</h2><p>All tools are 100% free with no hidden charges. No signup required. Results are instant. Tools work on any device. Created by SEO professionals with years of experience.</p>"},
  @{file="contact.html";title="Contact Us - SEO Tools Engine Pro";h1="Contact Us";content="<p>Have a question, suggestion, or feedback? We'd love to hear from you. Fill out the form below and we'll get back to you within 24-48 hours.</p><form id='contactForm'><div class='form-group'><label>Your Name</label><input type='text' name='name' required placeholder='Enter your name'></div><div class='form-group'><label>Email Address</label><input type='email' name='email' required placeholder='Enter your email'></div><div class='form-group'><label>Message</label><textarea name='message' required placeholder='Write your message here...' min-height='150'></textarea></div><button type='submit' class='btn btn-primary'><i class='fas fa-paper-plane'></i> Send Message</button></form>"},
  @{file="privacy.html";title="Privacy Policy - SEO Tools Engine Pro";h1="Privacy Policy";content="<p><strong>Last Updated:</strong> June 2026</p><h2>Information We Collect</h2><p>We do not collect, store, or share any personal information. All tools process data locally in your browser.</p><h2>Cookies</h2><p>We use minimal local storage for theme preference only. We do not use tracking cookies.</p><h2>Third-Party Services</h2><p>We display ads from Adsterra and PropellerAds. These networks may use cookies for ad personalization. You can opt out at your ad settings.</p><h2>Data Security</h2><p>Since we don't collect user data, there is no risk of data breach from our side.</p><h2>Changes to Policy</h2><p>We may update this policy occasionally. Changes will be posted here.</p><h2>Contact</h2><p>For questions about this policy, contact us through our contact page.</p>"},
  @{file="disclaimer.html";title="Disclaimer - SEO Tools Engine Pro";h1="Disclaimer";content="<p><strong>Last Updated:</strong> June 2026</p><h2>General Information</h2><p>The tools and information on SEO Tools Engine Pro are for general informational purposes only. They should not be considered as professional SEO advice.</p><h2>Accuracy</h2><p>While we strive for accuracy, results from our tools are estimates and should be verified with other sources.</p><h2>No Guarantee</h2><p>We do not guarantee specific search engine rankings or traffic results from using our tools or following our guides.</p><h2>External Links</h2><p>Our website may contain links to external sites. We are not responsible for their content or practices.</p><h2>Limitation</h2><p>We shall not be liable for any damages arising from the use of our tools or information.</p>"}
)

foreach ($p in $pages) {
  $html = $head
  $html = $html.Replace('__TITLE__', $p.title)
  
  $pageContent = @"
  <div class="page-content">
    <div class="content">
      <h1>$($p.h1)</h1>
      $($p.content)
    </div>
  </div>
"@
  
  $html = $html.Replace('__CONTENT__', $pageContent)
  
  # Fix paths for blog links in static pages
  $html = $html.Replace('../tools/', 'tools/').Replace('../about.html', 'about.html').Replace('../contact.html', 'contact.html').Replace('../privacy.html', 'privacy.html').Replace('../disclaimer.html', 'disclaimer.html').Replace('../assets/', 'assets/')
  
  $html | Out-File -FilePath "$base\$($p.file)" -Encoding utf8
  Write-Host "Created $($p.file)"
}

Write-Host ""
Write-Host "========================================"
Write-Host "All pages generated successfully!"
Write-Host "Total: $($tools.Count) tools + $($blogPosts.Count) blog posts + $($pages.Count) static pages"
Write-Host "========================================"
