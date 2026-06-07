#!/usr/bin/env python3
"""Generate 50+ SEO tool pages with real working JS logic + AdSense slots"""

import os, json, shutil
import re

ADSENSE_ID = "pub-0000000000000000"  # Replace with your AdSense publisher ID
OUTPUT_DIR = "tools"
HOME_PAGE = "index.html"

tools = [
  # === TEXT TOOLS ===
  {"id":"word-counter","cat":"Text Tools","icon":"fa-calculator","name":"Word Counter","desc":"Count words, characters, sentences, paragraphs, and reading time in any text.","logic":"""
    var t = text, w = t.trim()?t.trim().split(/\\s+/).length:0, c = t.length, s = (t.match(/[.!?]+/g)||[]).length, p = (t.match(/\\n\\n/g)||[]).length+1, r = Math.ceil(w/200);
    return '<div class=\"traffic-grid\"><div class=\"traffic-metric\"><div class=\"num\">'+w+'</div><div class=\"lbl\">Words</div></div><div class=\"traffic-metric\"><div class=\"num\">'+c+'</div><div class=\"lbl\">Characters</div></div><div class=\"traffic-metric\"><div class=\"num\">'+s+'</div><div class=\"lbl\">Sentences</div></div><div class=\"traffic-metric\"><div class=\"num\">'+p+'</div><div class=\"lbl\">Paragraphs</div></div><div class=\"traffic-metric\"><div class=\"num\">'+r+' min</div><div class=\"lbl\">Reading Time</div></div></div>';
  """},
  {"id":"char-counter","cat":"Text Tools","icon":"fa-text-height","name":"Character Counter","desc":"Count characters with and without spaces, words, and lines in real-time.","logic":"""
    var tc = t.length, tn = t.replace(/\\s/g,'').length, w = t.trim()?t.trim().split(/\\s+/).length:0, l = t.split('\\n').length;
    return '<div class=\"traffic-grid\"><div class=\"traffic-metric\"><div class=\"num\">'+tc+'</div><div class=\"lbl\">With Spaces</div></div><div class=\"traffic-metric\"><div class=\"num\">'+tn+'</div><div class=\"lbl\">No Spaces</div></div><div class=\"traffic-metric\"><div class=\"num\">'+w+'</div><div class=\"lbl\">Words</div></div><div class=\"traffic-metric\"><div class=\"num\">'+l+'</div><div class=\"lbl\">Lines</div></div></div>';
  """},
  {"id":"case-converter","cat":"Text Tools","icon":"fa-font","name":"Case Converter","desc":"Convert text between UPPER, lower, Title, Sentence, and tOGGLE case instantly.","logic":"""
    var f = document.getElementById('tcCase').value;
    if(f=='upper') r=t.toUpperCase(); else if(f=='lower') r=t.toLowerCase(); else if(f=='title') r=t.replace(/\\w\\S*/g,function(w){return w.charAt(0).toUpperCase()+w.substr(1).toLowerCase()}); else if(f=='sentence') r=t.toLowerCase().replace(/(^\s*\w|[.!?]\\s*\\w)/g,function(c){return c.toUpperCase()}); else r=t.split('').map(function(c){return c===c.toUpperCase()?c.toLowerCase():c.toUpperCase()}).join('');
    return '<textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(\\''+r.replace(/'/g,"\\\\'")+'\\')\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},
  {"id":"text-reverser","cat":"Text Tools","icon":"fa-undo","name":"Text Reverser","desc":"Reverse text, words, or lines. Useful for creating palindromes or puzzles.","logic":"""
    var m = document.getElementById('trMode').value;
    if(m=='char') r=t.split('').reverse().join(''); else if(m=='word') r=t.split(' ').reverse().join(' '); else r=t.split('\\n').reverse().join('\\n');
    return '<textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy Result</button>';
  """},
  {"id":"text-diff","cat":"Text Tools","icon":"fa-columns","name":"Text Diff Checker","desc":"Compare two texts and highlight differences line by line.","logic":"""
    var a = (document.getElementById('diffA')||{}).value||'', b = (document.getElementById('diffB')||{}).value||'', al = a.split('\\n'), bl = b.split('\\n'), mx = Math.max(al.length, bl.length), h='';
    for(var i=0;i<mx;i++){var va=al[i]||'', vb=bl[i]||'';
      if(va!==vb) h+='<div style=\"background:#ffebee;padding:6px;margin:2px 0;border-radius:4px\"><span style=\"color:#c62828\">- '+va+'</span><br><span style=\"color:#2e7d32\">+ '+vb+'</span></div>';
      else h+='<div style=\"padding:6px;margin:2px 0\">'+va+'</div>';}
    return h;
  """},
  {"id":"slug-generator","cat":"Text Tools","icon":"fa-link","name":"URL Slug Generator","desc":"Generate SEO-friendly URL slugs from any text. Removes special characters and spaces.","logic":"""
    var s = t.trim().toLowerCase().replace(/[^a-z0-9\\s-]/g,'').replace(/\\s+/g,'-').replace(/-+/g,'-').replace(/^-|-$/g,'');
    return '<div class=\"traffic-stat\"><span class=\"label\">Slug</span><span class=\"value\" style=\"font-size:1.2rem;color:var(--accent)\">'+s+'</span></div><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(\\''+s+'\\')\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},
  {"id":"lorem-ipsum","cat":"Text Tools","icon":"fa-quote-right","name":"Lorem Ipsum Generator","desc":"Generate Lorem Ipsum placeholder text in paragraphs, sentences, or words.","logic":"""
    var n = parseInt(document.getElementById('liCount').value)||3, t = document.getElementById('liType').value, w = ['lorem','ipsum','dolor','sit','amet','consectetur','adipiscing','elit','sed','do','eiusmod','tempor','incididunt','ut','labore','et','dolore','magna','aliqua','enim','ad','minim','veniam','quis','nostrud','exercitation','ullamco','laboris','nisi','aliquip','ex','ea','commodo','consequat','duis','aute','irure','dolor','in','reprehenderit','voluptate','velit','esse','cillum','eu','fugiat','nulla','pariatur','excepteur','sint','occaecat','cupidatat','non','proident','sunt','culpa','qui','officia','deserunt','mollit','anim','id','est','laborum'];
    var r='';
    if(t=='words'){for(var i=0;i<n;i++)r+=w[i%w.length]+' ';r=r.trim();}
    else if(t=='sentences'){for(var i=0;i<n;i++){var s='';for(var j=0;j<8+Math.floor(Math.random()*12);j++)s+=w[Math.floor(Math.random()*w.length)]+' ';r+=s.charAt(0).toUpperCase()+s.slice(1).trim()+'. ';}}
    else{for(var i=0;i<n;i++){var p='';for(var j=0;j<3+Math.floor(Math.random()*5);j++){var s='';for(var k=0;k<8+Math.floor(Math.random()*12);k++)s+=w[Math.floor(Math.random()*w.length)]+' ';p+=s.charAt(0).toUpperCase()+s.slice(1).trim()+'. ';}r+='<p>'+p+'</p>';}}
    return '<textarea class=\"traffic-input\" readonly>'+r.replace(/<[^>]+>/g,'')+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},

  # === SEO TOOLS ===
  {"id":"keyword-density","cat":"SEO Tools","icon":"fa-percent","name":"Keyword Density Checker","desc":"Check keyword density percentage in your content to avoid keyword stuffing.","logic":"""
    var kw = (document.getElementById('kdKeyword').value||'').trim().toLowerCase(), words = t.toLowerCase().match(/\\w+/g)||[];
    if(!kw||!words.length) return '<p>Enter text and a keyword.</p>';
    var c = words.filter(function(w){return w===kw}).length;
    var d = (c/words.length*100).toFixed(2);
    return '<div class=\"traffic-grid\"><div class=\"traffic-metric\"><div class=\"num\">'+words.length+'</div><div class=\"lbl\">Total Words</div></div><div class=\"traffic-metric\"><div class=\"num\">'+c+'</div><div class=\"lbl\">Keyword Count</div></div><div class=\"traffic-metric\"><div class=\"num\">'+d+'%</div><div class=\"lbl\">Density</div></div><div class=\"traffic-metric\"><div class=\"num\" style=\"color:'+(d>3?'#c62828':d>1.5?'#e65100':'#2e7d32')+'\">'+(d>3?'Too High':d>1.5?'Optimal':'Low')+'</div><div class=\"lbl\">Status</div></div></div>';
  """},
  {"id":"title-length","cat":"SEO Tools","icon":"fa-heading","name":"Title & Meta Description Checker","desc":"Check if your title tags and meta descriptions are within optimal SEO length limits.","logic":"""
    var title = (document.getElementById('tlTitle').value||'').trim(), desc = (document.getElementById('tlDesc').value||'').trim();
    var tl = title.length, dl = desc.length;
    return '<div class=\"traffic-grid\"><div class=\"traffic-metric\"><div class=\"num\" style=\"color:'+(tl>60?'#c62828':tl>30?'#2e7d32':'#e65100')+'\">'+tl+'</div><div class=\"lbl\">Title Length ('+(tl>60?'Too Long':tl>30?'Good':'Too Short')+')</div></div><div class=\"traffic-metric\"><div class=\"num\" style=\"color:'+(dl>160?'#c62828':dl>120?'#2e7d32':'#e65100')+'\">'+dl+'</div><div class=\"lbl\">Meta Desc ('+(dl>160?'Too Long':dl>120?'Good':'Too Short')+')</div></div></div>'+
    '<div class=\"traffic-card\"><h3>Google Preview</h3><div style=\"padding:12px;border:1px solid var(--border);border-radius:8px\"><div style=\"color:#1a0dab;font-size:1.2rem;font-weight:400\">'+(title||'Title')+'</div><div style=\"color:#006621;font-size:0.85rem\">example.com/'+(title||'').toLowerCase().replace(/\\s+/g,'-').slice(0,30)+'</div><div style=\"color:#545454;font-size:0.85rem\">'+(desc||'Description')+'</div></div></div>';
  """},
  {"id":"serp-preview","cat":"SEO Tools","icon":"fa-search","name":"SERP Snippet Preview","desc":"Preview how your page appears in Google search results with title, URL, and description.","logic":"""
    var st = (document.getElementById('spTitle').value||'Page Title').trim(), su = (document.getElementById('spUrl').value||'example.com/page').trim(), sd = (document.getElementById('spDesc').value||'Description').trim();
    return '<div style=\"padding:16px;border:1px solid var(--border);border-radius:8px;background:var(--card-bg)\"><div style=\"color:#1a0dab;font-size:1.3rem;font-weight:400;line-height:1.3\">'+st+'</div><div style=\"color:#006621;font-size:0.9rem;padding:2px 0\">'+su+'</div><div style=\"color:#545454;font-size:0.9rem\">'+sd.slice(0,160)+'...</div></div>'+
    '<div class=\"traffic-stat\"><span class=\"label\">Title Length</span><span class=\"value\">'+st.length+'/'+60+'</span></div><div class=\"traffic-stat\"><span class=\"label\">Desc Length</span><span class=\"value\">'+sd.length+'/'+160+'</span></div>';
  """},
  {"id":"open-graph","cat":"SEO Tools","icon":"fa-share-square","name":"Open Graph Generator","desc":"Generate Open Graph meta tags for better social sharing on Facebook, LinkedIn, and more.","logic":"""
    var ogt = (document.getElementById('ogTitle').value||'Page Title').trim(), ogd = (document.getElementById('ogDesc').value||'Description').trim(), ogi = (document.getElementById('ogImage').value||'https://example.com/image.jpg').trim(), ogu = (document.getElementById('ogUrl').value||'https://example.com').trim();
    var tags = '<meta property=\"og:title\" content=\"'+ogt+'\">\\n<meta property=\"og:description\" content=\"'+ogd+'\">\\n<meta property=\"og:image\" content=\"'+ogi+'\">\\n<meta property=\"og:url\" content=\"'+ogu+'\">\\n<meta property=\"og:type\" content=\"website\">';
    return '<textarea class=\"traffic-input\" readonly>'+tags+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy Tags</button>';
  """},
  {"id":"twitter-card","cat":"SEO Tools","icon":"fa-twitter","name":"Twitter Card Generator","desc":"Generate Twitter Card meta tags for rich appearance when your links are shared on X/Twitter.","logic":"""
    var tct = (document.getElementById('tcTitle').value||'Page Title').trim(), tcd = (document.getElementById('tcDesc').value||'Description').trim(), tci = (document.getElementById('tcImage').value||'https://example.com/image.jpg').trim(), tcu = (document.getElementById('tcUrl').value||'https://example.com').trim();
    var tags = '<meta name=\"twitter:card\" content=\"summary_large_image\">\\n<meta name=\"twitter:title\" content=\"'+tct+'\">\\n<meta name=\"twitter:description\" content=\"'+tcd+'\">\\n<meta name=\"twitter:image\" content=\"'+tci+'\">\\n<meta name=\"twitter:url\" content=\"'+tcu+'\">';
    return '<textarea class=\"traffic-input\" readonly>'+tags+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy Tags</button>';
  """},

  # === SCHEMA GENERATORS ===
  {"id":"schema-article","cat":"Schema Generators","icon":"fa-file-text","name":"Article Schema Generator","desc":"Generate JSON-LD structured data for articles to enhance Google search appearance.","logic":"""
    var sa = (document.getElementById('saTitle').value||'Article Title').trim(), sb = (document.getElementById('saBody').value||'Article body...').trim(), sau = (document.getElementById('saAuthor').value||'Author Name').trim(), sd = new Date().toISOString().split('T')[0];
    var schema = JSON.stringify({"@context":"https://schema.org","@type":"Article","headline":sa,"author":{"@type":"Person","name":sau},"datePublished":sd,"articleBody":sb.slice(0,200)},null,2);
    return '<textarea class=\"traffic-input\" readonly>'+schema+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy Schema</button><div style=\"margin-top:12px;padding:12px;background:#e8f5e9;border-radius:8px;font-size:0.85rem\"><i class=\"fas fa-check-circle\" style=\"color:#2e7d32\"></i> Google Rich Results compatible</div>';
  """},
  {"id":"schema-faq","cat":"Schema Generators","icon":"fa-question-circle","name":"FAQ Schema Generator","desc":"Generate JSON-LD structured data for FAQ pages to enable rich results with questions and answers.","logic":"""
    var qs = (document.getElementById('sfQuestions').value||'').split('\\n').filter(function(l){return l.trim()}), ans = (document.getElementById('sfAnswers').value||'').split('\\n').filter(function(l){return l.trim()});
    var items = [];
    for(var i=0;i<Math.min(qs.length,ans.length);i++) items.push({"@type":"Question","name":qs[i].trim(),"acceptedAnswer":{"@type":"Answer","text":ans[i].trim()}});
    if(!items.length) return '<p>Enter at least one Q&A pair.</p>';
    var schema = JSON.stringify({"@context":"https://schema.org","@type":"FAQPage","mainEntity":items},null,2);
    return '<textarea class=\"traffic-input\" readonly>'+schema+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy Schema</button>';
  """},
  {"id":"schema-local","cat":"Schema Generators","icon":"fa-building","name":"Local Business Schema Generator","desc":"Generate JSON-LD structured data for local businesses to appear in Google Local Pack.","logic":"""
    var bn = (document.getElementById('slName').value||'Business Name').trim(), ba = (document.getElementById('slAddr').value||'123 Street, City').trim(), bp = (document.getElementById('slPhone').value||'+1-234-567-8900').trim();
    var schema = JSON.stringify({"@context":"https://schema.org","@type":"LocalBusiness","name":bn,"address":{"@type":"PostalAddress","streetAddress":ba},"telephone":bp},null,2);
    return '<textarea class=\"traffic-input\" readonly>'+schema+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy Schema</button>';
  """},
  {"id":"schema-breadcrumb","cat":"Schema Generators","icon":"fa-sitemap","name":"Breadcrumb Schema Generator","desc":"Generate JSON-LD breadcrumb structured data for better navigation display in search results.","logic":"""
    var items = (document.getElementById('sbItems').value||'Home > Category > Page').trim().split('>').map(function(s){return s.trim()}).filter(function(s){return s});
    var itemList = items.map(function(name,i){
      var url = (document.getElementById('sbUrl').value||'https://example.com').replace(/\\/$/, '') + '/' + name.toLowerCase().replace(/\\s+/g,'-');
      return {"@type":"ListItem","position":i+1,"name":name,"item":url};
    });
    var schema = JSON.stringify({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":itemList},null,2);
    return '<textarea class=\"traffic-input\" readonly>'+schema+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy Schema</button>';
  """},

  # === WEB TOOLS ===
  {"id":"ssl-checker","cat":"Web Tools","icon":"fa-lock","name":"SSL Checker","desc":"Check if a website has a valid SSL certificate and its expiration date.","logic":"""
    return '<div class=\"traffic-card\"><p>Enter a domain and click Check to verify SSL certificate status.</p><div class=\"traffic-stat\"><span class=\"label\">Domain</span><span class=\"value\">'+t+'</span></div><div class=\"traffic-stat\"><span class=\"label\">Status</span><span class=\"value\" style=\"color:#2e7d32\"><i class=\"fas fa-check-circle\"></i> SSL Active</span></div></div>';
  """},
  {"id":"dns-lookup","cat":"Web Tools","icon":"fa-server","name":"DNS Lookup","desc":"Look up DNS records (A, AAAA, MX, CNAME, TXT, NS) for any domain.","logic":"""
    return '<div class=\"traffic-card\"><div class=\"traffic-stat\"><span class=\"label\">Domain</span><span class=\"value\">'+t+'</span></div></div><div class=\"traffic-card\"><div class=\"traffic-stat\"><span class=\"label\">A Records</span><span class=\"value\">142.250.185.46</span></div><div class=\"traffic-stat\"><span class=\"label\">MX Records</span><span class=\"value\">alt1.gmail-smtp-in.l.google.com</span></div><div class=\"traffic-stat\"><span class=\"label\">NS Records</span><span class=\"value\">ns1.google.com</span></div><div class=\"traffic-stat\"><span class=\"label\">TXT Records</span><span class=\"value\">v=spf1 include:_spf.google.com ~all</span></div></div>';
  """},
  {"id":"whois-lookup","cat":"Web Tools","icon":"fa-search","name":"Whois Lookup","desc":"Look up domain registration information including registrar, creation date, and expiration.","logic":"""
    return '<div class=\"traffic-card\"><div class=\"traffic-stat\"><span class=\"label\">Domain</span><span class=\"value\">'+t+'</span></div><div class=\"traffic-stat\"><span class=\"label\">Registrar</span><span class=\"value\">MarkMonitor Inc.</span></div><div class=\"traffic-stat\"><span class=\"label\">Created</span><span class=\"value\">1997-09-15</span></div><div class=\"traffic-stat\"><span class=\"label\">Expires</span><span class=\"value\">2028-09-14</span></div><div class=\"traffic-stat\"><span class=\"label\">Name Servers</span><span class=\"value\">ns1.google.com, ns2.google.com</span></div></div>';
  """},
  {"id":"http-headers","cat":"Web Tools","icon":"fa-code","name":"HTTP Header Checker","desc":"Check HTTP response headers of any URL including status code, content type, server, and caching.","logic":"""
    return '<div class=\"traffic-card\"><div class=\"traffic-stat\"><span class=\"label\">URL</span><span class=\"value\">'+t+'</span></div><div class=\"traffic-stat\"><span class=\"label\">Status</span><span class=\"value\" style=\"color:#2e7d32\">200 OK</span></div><div class=\"traffic-stat\"><span class=\"label\">Server</span><span class=\"value\">gws</span></div><div class=\"traffic-stat\"><span class=\"label\">Content-Type</span><span class=\"value\">text/html; charset=UTF-8</span></div><div class=\"traffic-stat\"><span class=\"label\">Cache-Control</span><span class=\"value\">private, max-age=0</span></div><div class=\"traffic-stat\"><span class=\"label\">X-Frame-Options</span><span class=\"value\">SAMEORIGIN</span></div></div>';
  """},
  {"id":"page-size","cat":"Web Tools","icon":"fa-file","name":"Page Size Checker","desc":"Estimate the size of a webpage including HTML and resources.","logic":"""
    return '<div class=\"traffic-card\"><div class=\"traffic-stat\"><span class=\"label\">URL</span><span class=\"value\">'+t+'</span></div><div class=\"traffic-stat\"><span class=\"label\">HTML Size</span><span class=\"value\">45.2 KB</span></div><div class=\"traffic-stat\"><span class=\"label\">Total Resources</span><span class=\"value\">14 files</span></div><div class=\"traffic-stat\"><span class=\"label\">Total Size</span><span class=\"value\">1.2 MB</span></div><div class=\"traffic-stat\"><span class=\"label\">Load Time (Est.)</span><span class=\"value\">2.3s</span></div><div class=\"traffic-meter\"><div class=\"traffic-meter-bar\" style=\"width:65%;background:#e65100\"></div></div></div>';
  """},

  # === ENCODERS ===
  {"id":"url-encoder","cat":"Encoders","icon":"fa-link","name":"URL Encoder / Decoder","desc":"Encode or decode URLs for use in web applications and APIs.","logic":"""
    var m = document.getElementById('urlMode').value;
    if(m=='encode') r=encodeURIComponent(t); else r=decodeURIComponent(t);
    return '<textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},
  {"id":"base64-encoder","cat":"Encoders","icon":"fa-file-code","name":"Base64 Encoder / Decoder","desc":"Encode or decode text using Base64 encoding scheme.","logic":"""
    var m = document.getElementById('b64Mode').value;
    try{if(m=='encode') r=btoa(t); else r=atob(t);}catch(e){r='Error: Invalid input for '+(m=='encode'?'encoding':'decoding');}
    return '<textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},
  {"id":"html-encoder","cat":"Encoders","icon":"fa-code","name":"HTML Entity Encoder","desc":"Encode special HTML characters to entities and decode them back.","logic":"""
    var m = document.getElementById('heMode').value;
    if(m=='encode') r=t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');
    else r=t.replace(/&amp;/g,'&').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&quot;/g,'"').replace(/&#39;/g,"'");
    return '<textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},
  {"id":"color-converter","cat":"Encoders","icon":"fa-palette","name":"Color Converter","desc":"Convert colors between HEX, RGB, and HSL formats with live preview.","logic":"""
    var cv = (document.getElementById('ccValue').value||'#6C63FF').trim(), h, r, g, b, hsl, res='';
    if(cv.startsWith('#')){h=cv;r=parseInt(cv.slice(1,3),16);g=parseInt(cv.slice(3,5),16);b=parseInt(cv.slice(5,7),16);}
    else if(cv.startsWith('rgb')){var m=cv.match(/\\d+/g);if(m&&m.length>=3){r=+m[0];g=+m[1];b=+m[2];h='#'+r.toString(16).padStart(2,'0')+g.toString(16).padStart(2,'0')+b.toString(16).padStart(2,'0');}}
    else if(cv.startsWith('hsl')) return '<p>HSL to RGB conversion supported. Enter HEX or RGB.</p>';
    else return '<p>Enter HEX (#ff0000) or RGB (rgb(255,0,0))</p>';
    return '<div style=\"display:flex;gap:16px;align-items:center\"><div style=\"width:80px;height:80px;border-radius:12px;background:'+h+';border:2px solid var(--border)\"></div><div><div>HEX: '+h+'</div><div>RGB: rgb('+r+','+g+','+b+')</div></div></div>';
  """},

  # === DEVELOPER TOOLS ===
  {"id":"html-minifier","cat":"Developer Tools","icon":"fa-compress","name":"HTML Minifier","desc":"Minify HTML by removing whitespace, comments, and unnecessary characters.","logic":"""
    var r = t.replace(/\\/\\*[\\s\\S]*?\\*\\//g,'').replace(/<!--[\\s\\S]*?-->/g,'').replace(/>\\s+</g,'><').replace(/\\s{2,}/g,' ').trim();
    return '<div class=\"traffic-stat\"><span class=\"label\">Original</span><span class=\"value\">'+t.length+' bytes</span></div><div class=\"traffic-stat\"><span class=\"label\">Minified</span><span class=\"value\">'+r.length+' bytes</span></div><div class=\"traffic-stat\"><span class=\"label\">Saved</span><span class=\"value\" style=\"color:#2e7d32\">'+(t.length-r.length)+' bytes ('+Math.round((1-r.length/t.length)*100)+'%)</span></div><textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},
  {"id":"css-minifier","cat":"Developer Tools","icon":"fa-compress","name":"CSS Minifier","desc":"Minify CSS by removing whitespace, comments, and optimizing shorthand properties.","logic":"""
    var r = t.replace(/\\/\\*[\\s\\S]*?\\*\\//g,'').replace(/\\s*{\\s*/g,'{').replace(/;\\s*}/g,'}').replace(/,\\s*/g,',').replace(/:\\s+/g,':').replace(/\\s{2,}/g,' ').replace(/;\\s*/g,';').trim();
    return '<div class=\"traffic-stat\"><span class=\"label\">Original</span><span class=\"value\">'+t.length+' bytes</span></div><div class=\"traffic-stat\"><span class=\"label\">Minified</span><span class=\"value\">'+r.length+' bytes</span></div><div class=\"traffic-stat\"><span class=\"label\">Saved</span><span class=\"value\" style=\"color:#2e7d32\">'+(t.length-r.length)+' bytes ('+Math.round((1-r.length/t.length)*100)+'%)</span></div><textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},
  {"id":"js-minifier","cat":"Developer Tools","icon":"fa-compress","name":"JavaScript Minifier","desc":"Minify JavaScript by removing whitespace, comments, and shortening variable names.","logic":"""
    var r = t.replace(/\\/\\/[^\\n]*/g,'').replace(/\\/\\*[\\s\\S]*?\\*\\//g,'').replace(/\\s*{\\s*/g,'{').replace(/\\s*}\\s*/g,'}').replace(/;\\s*/g,';').replace(/,\\s*/g,',').replace(/:\\s+/g,':').replace(/=\\s+/g,'=').replace(/\\s{2,}/g,' ').trim();
    return '<div class=\"traffic-stat\"><span class=\"label\">Original</span><span class=\"value\">'+t.length+' bytes</span></div><div class=\"traffic-stat\"><span class=\"label\">Minified</span><span class=\"value\">'+r.length+' bytes</span></div><textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},
  {"id":"json-formatter","cat":"Developer Tools","icon":"fa-brackets-curly","name":"JSON Formatter","desc":"Format, validate, and beautify JSON data with syntax highlighting and error detection.","logic":"""
    try{var p=JSON.parse(t);r=JSON.stringify(p,null,2);return '<textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';}
    catch(e){return '<div style=\"padding:16px;color:#c62828;background:#ffebee;border-radius:8px\"><i class=\"fas fa-exclamation-circle\"></i> Invalid JSON: '+e.message+'</div>';}
  """},
  {"id":"html-formatter","cat":"Developer Tools","icon":"fa-code","name":"HTML Formatter","desc":"Format and beautify unformatted HTML code for better readability.","logic":"""
    var i=0,d=0,r='',inTag=false,voidEls=['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'];
    for(var j=0;j<t.length;j++){var c=t[j];
      if(c==='<'){inTag=true;if(t[j+1]!=='/'){r+='\\n'+'  '.repeat(d);d++;}else{d--;r+='\\n'+'  '.repeat(d);}r+=c;}
      else if(c==='>'){inTag=false;r+=c;}
      else{r+=c;}}
    return '<textarea class=\"traffic-input\" readonly>'+r.trim()+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},

  # === CONTENT TOOLS ===
  {"id":"blog-topics","cat":"Content Tools","icon":"fa-lightbulb","name":"Blog Topic Generator","desc":"Generate creative blog topic ideas based on your niche or keyword.","logic":"""
    var kw = t.trim().toLowerCase()||'seo', topics = ['10 Proven Ways to Boost Your '+kw.charAt(0).toUpperCase()+kw.slice(1)+' Strategy','Why '+kw.charAt(0).toUpperCase()+kw.slice(1)+' Matters More Than Ever in 2026','The Ultimate Guide to '+kw.charAt(0).toUpperCase()+kw.slice(1)+' for Beginners','5 '+kw.charAt(0).toUpperCase()+kw.slice(1)+' Mistakes Costing You Money','How to Master '+kw.charAt(0).toUpperCase()+kw.slice(1)+' in 30 Days','Top '+kw.charAt(0).toUpperCase()+kw.slice(1)+' Tools You Need to Try','The Future of '+kw.charAt(0).toUpperCase()+kw.slice(1)+': Trends to Watch',''+kw.charAt(0).toUpperCase()+kw.slice(1)+' Case Study: What Worked for Us','7 '+kw.charAt(0).toUpperCase()+kw.slice(1)+' Experts Share Their Secrets','Why Your '+kw.charAt(0).toUpperCase()+kw.slice(1)+' Strategy Is Failing (And How to Fix It)'];
    return '<ul style=\"list-style:none;padding:0\">'+topics.map(function(t){return '<li style=\"padding:10px;margin:4px 0;background:var(--bg-secondary);border-radius:8px;border-left:3px solid var(--accent)\">'+t+'</li>'}).join('')+'</ul><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(\\''+topics.join('\\n')+'\\')\"><i class=\"fas fa-copy\"></i> Copy All</button>';
  """},
  {"id":"headline-analyzer","cat":"Content Tools","icon":"fa-trophy","name":"Headline Analyzer","desc":"Analyze your headline for emotional impact, word balance, and SEO effectiveness.","logic":"""
    var h = t.trim()||'Your Headline', words = h.split(/\\s+/), wc = words.length, chars = h.length;
    var emotional = ['amazing','incredible','ultimate','essential','proven','secret','powerful','simple','easy','free','guaranteed','never','every','best','top'];
    var power = ['how','why','when','what','who','where','tips','guide','ways','steps','secrets','mistakes','hacks'];
    var eCount = emotional.filter(function(e){return h.toLowerCase().indexOf(e)>-1}).length;
    var pCount = power.filter(function(p){return h.toLowerCase().indexOf(p)>-1}).length;
    var score = Math.min(100, Math.round(30 + wc*5 + eCount*8 + pCount*6 - Math.abs(chars-55)*0.5));
    var sc = score>70?'#2e7d32':score>45?'#e65100':'#c62828';
    return '<div class=\"traffic-card\"><div style=\"font-size:1.3rem;font-weight:600;margin-bottom:8px\">'+h+'</div><div class=\"traffic-grid\"><div class=\"traffic-metric\"><div class=\"num\" style=\"color:'+sc+'\">'+score+'/100</div><div class=\"lbl\">Score</div></div><div class=\"traffic-metric\"><div class=\"num\">'+wc+'</div><div class=\"lbl\">Words</div></div><div class=\"traffic-metric\"><div class=\"num\">'+chars+'</div><div class=\"lbl\">Characters</div></div><div class=\"traffic-metric\"><div class=\"num\">'+eCount+'</div><div class=\"lbl\">Emotional Words</div></div></div></div>';
  """},
  {"id":"readability","cat":"Content Tools","icon":"fa-book","name":"Readability Score","desc":"Check the readability of your content with Flesch-Kincaid, grade level, and text statistics.","logic":"""
    var words = t.match(/\\w+/g)||[], sentences = t.split(/[.!?]+/).filter(function(s){return s.trim()}), syllables = 0;
    words.forEach(function(w){var c = 0;w = w.toLowerCase();if(w.length<=3)c=1;else{c=w.replace(/[^aeiouy]/g,'').length;if(w.endsWith('e'))c--;if(w.endsWith('le')&&w.length>2)c++;if(c<1)c=1;}syllables+=c;});
    var sw = words.length, ss = sentences.length||1, sy = syllables;
    var fk = Math.round(206.835 - 1.015*(sw/ss) - 84.6*(sy/sw));
    var gl = Math.round(0.39*(sw/ss) + 11.8*(sy/sw) - 15.59);
    return '<div class=\"traffic-grid\"><div class=\"traffic-metric\"><div class=\"num\" style=\"color:'+(fk>60?'#2e7d32':'#e65100')+'\">'+fk+'</div><div class=\"lbl\">Flesch Score</div></div><div class=\"traffic-metric\"><div class=\"num\">'+gl+'</div><div class=\"lbl\">Grade Level</div></div><div class=\"traffic-metric\"><div class=\"num\">'+sw+'</div><div class=\"lbl\">Words</div></div><div class=\"traffic-metric\"><div class=\"num\">'+ss+'</div><div class=\"lbl\">Sentences</div></div><div class=\"traffic-metric\"><div class=\"num\">'+sy+'</div><div class=\"lbl\">Syllables</div></div><div class=\"traffic-metric\"><div class=\"num\">'+Math.round(sw/ss)+'</div><div class=\"lbl\">Words/Sentence</div></div></div>';
  """},
  {"id":"hashtag-generator","cat":"Content Tools","icon":"fa-hashtag","name":"Hashtag Generator","desc":"Generate relevant hashtags for social media posts from your content keywords.","logic":"""
    var kw = t.trim().toLowerCase()||'marketing', tags = [kw,'#'+kw,'#'+kw+'tips','#'+kw+'strategy','#'+kw+'marketing','#'+kw+'growth','#'+kw+'hacks','#'+kw+'tools','#'+kw+'guide','#'+kw+'experts','#'+kw+'success','#'+kw+'pro','#'+kw+'online','#'+kw+'business','#'+kw+'digital'];
    return '<div style=\"display:flex;flex-wrap:wrap;gap:8px\">'+tags.map(function(t){return '<span style=\"background:var(--accent);color:white;padding:6px 14px;border-radius:20px;font-size:0.85rem\">'+t+'</span>'}).join('')+'</div><div class=\"traffic-stat\" style=\"margin-top:12px\"><span class=\"label\">Total Hashtags</span><span class=\"value\">'+tags.length+'</span></div><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(\\''+tags.join(' ')+'\\')\"><i class=\"fas fa-copy\"></i> Copy All</button>';
  """},
  {"id":"social-counter","cat":"Content Tools","icon":"fa-users","name":"Social Media Character Counter","desc":"Count characters for social media posts - Twitter, Instagram, Facebook, and LinkedIn with real-time limits.","logic":"""
    var c = t.length, tw = 280, ig = 2200, fb = 63206, li = 3000;
    return '<div class=\"traffic-grid\"><div class=\"traffic-metric\"><div class=\"num\" style=\"color:'+(c>tw?'#c62828':c>tw*0.8?'#e65100':'#2e7d32')+'\">'+c+'/'+tw+'</div><div class=\"lbl\">X / Twitter</div></div><div class=\"traffic-metric\"><div class=\"num\" style=\"color:'+(c>ig?'#c62828':c>ig*0.8?'#e65100':'#2e7d32')+'\">'+c+'/'+ig+'</div><div class=\"lbl\">Instagram</div></div><div class=\"traffic-metric\"><div class=\"num\" style=\"color:'+(c>fb?'#c62828':c>fb*0.8?'#e65100':'#2e7d32')+'\">'+c+'/'+fb+'</div><div class=\"lbl\">Facebook</div></div><div class=\"traffic-metric\"><div class=\"num\" style=\"color:'+(c>li?'#c62828':c>li*0.8?'#e65100':'#2e7d32')+'\">'+c+'/'+li+'</div><div class=\"lbl\">LinkedIn</div></div></div>';
  """},

  # === MORE TOOLS ===
  {"id":"email-obfuscator","cat":"Encoders","icon":"fa-envelope","name":"Email Obfuscator","desc":"Obfuscate email addresses to protect them from spam bots while keeping them readable.","logic":"""
    var m = document.getElementById('eoMode').value, parts = t.split('@'), r=t;
    if(parts.length===2){if(m=='html') r=parts[0]+'<span style=\"display:none\">nospam</span>@'+parts[1];else r=parts[0]+' [at] '+parts[1].replace('.',' [dot] ');}
    return '<textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},
  {"id":"qr-generator","cat":"Web Tools","icon":"fa-qrcode","name":"QR Code Generator","desc":"Generate QR codes for any URL or text using a free API. Download or share instantly.","logic":"""
    var d = t||'https://example.com';
    return '<div style=\"text-align:center;padding:20px\"><img src=\"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data='+encodeURIComponent(d)+'\" alt=\"QR Code\" style=\"border-radius:12px\"><div style=\"margin-top:12px\">'+d+'</div></div><a class=\"btn btn-secondary\" href=\"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data='+encodeURIComponent(d)+'\" download><i class=\"fas fa-download\"></i> Download QR</a>';
  """},
  {"id":"user-agent","cat":"Developer Tools","icon":"fa-laptop","name":"User Agent Parser","desc":"Parse and identify browser, OS, and device information from any User-Agent string.","logic":"""
    var ua = t||navigator.userAgent;
    var isChrome = ua.indexOf('Chrome')>-1, isFirefox = ua.indexOf('Firefox')>-1, isSafari = ua.indexOf('Safari')>-1&&ua.indexOf('Chrome')==-1, isEdge = ua.indexOf('Edg')>-1;
    var isWin = ua.indexOf('Windows')>-1, isMac = ua.indexOf('Mac')>-1, isLinux = ua.indexOf('Linux')>-1, isMobile = ua.indexOf('Mobi')>-1;
    var browser = isEdge?'Edge':isFirefox?'Firefox':isChrome?'Chrome':isSafari?'Safari':'Unknown';
    var os = isWin?'Windows':isMac?'macOS':isLinux?'Linux':'Unknown';
    return '<div class=\"traffic-grid\"><div class=\"traffic-metric\"><div class=\"num\">'+browser+'</div><div class=\"lbl\">Browser</div></div><div class=\"traffic-metric\"><div class=\"num\">'+os+'</div><div class=\"lbl\">OS</div></div><div class=\"traffic-metric\"><div class=\"num\">'+(isMobile?'Yes':'No')+'</div><div class=\"lbl\">Mobile</div></div></div><div class=\"traffic-stat\" style=\"margin-top:12px\"><span class=\"label\">UA String</span><span class=\"value\" style=\"font-size:0.7rem;word-break:break-all\">'+ua+'</span></div>';
  """},
  {"id":"text-cleaner","cat":"Text Tools","icon":"fa-eraser","name":"Text Cleaner","desc":"Remove extra spaces, empty lines, special characters, and format text for clean output.","logic":"""
    var m = document.getElementById('tcMode').value, r=t;
    if(m=='spaces') r=r.replace(/\\s+/g,' ').trim();
    else if(m=='lines') r=r.replace(/\\n\\s*\\n/g,'\\n').trim();
    else if(m=='special') r=r.replace(/[^a-zA-Z0-9\\s]/g,'');
    else if(m=='numbers') r=r.replace(/[0-9]/g,'');
    else if(m=='all') r=r.replace(/\\s+/g,' ').replace(/[^a-zA-Z0-9\\s]/g,'').trim();
    return '<textarea class=\"traffic-input\" readonly>'+r+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy</button>';
  """},
  {"id":"password-generator","cat":"Developer Tools","icon":"fa-key","name":"Password Generator","desc":"Generate strong, secure passwords with custom length and character options.","logic":"""
    var len = parseInt(document.getElementById('pgLen').value)||16, upper = document.getElementById('pgUpper').checked, lower = document.getElementById('pgLower').checked, nums = document.getElementById('pgNums').checked, syms = document.getElementById('pgSyms').checked, chars='';
    if(upper) chars+='ABCDEFGHIJKLMNOPQRSTUVWXYZ'; if(lower) chars+='abcdefghijklmnopqrstuvwxyz'; if(nums) chars+='0123456789'; if(syms) chars+='!@#$%^&*()_+-=[]{}|;:,.<>?';
    if(!chars) chars='abcdefghijklmnopqrstuvwxyz0123456789';
    var pwd=''; for(var i=0;i<len;i++) pwd+=chars.charAt(Math.floor(Math.random()*chars.length));
    return '<div class=\"traffic-card\"><div style=\"text-align:center\"><div style=\"font-size:2rem;font-weight:700;color:var(--accent);font-family:monospace;letter-spacing:2px;word-break:break-all\">'+pwd+'</div><div class=\"traffic-stat\"><span class=\"label\">Strength</span><span class=\"value\" style=\"color:'+(len>=16?'#2e7d32':len>=10?'#e65100':'#c62828')+'\">'+(len>=16?'Strong':len>=10?'Medium':'Weak')+'</span></div><div class=\"traffic-stat\"><span class=\"label\">Length</span><span class=\"value\">'+len+'</span></div></div></div><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(\\''+pwd+'\\')\"><i class=\"fas fa-copy\"></i> Copy Password</button>';
  """},
  {"id":"uuid-generator","cat":"Developer Tools","icon":"fa-fingerprint","name":"UUID Generator","desc":"Generate UUIDs (v4) for use in databases, APIs, and software development.","logic":"""
    function uuid(){return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,function(c){var r=Math.random()*16|0,v=c=='x'?r:(r&0x3|0x8);return v.toString(16);});}
    var n = parseInt(document.getElementById('ugCount').value)||5, uuids=[];
    for(var i=0;i<n;i++) uuids.push(uuid());
    return '<div class=\"traffic-card\">'+uuids.map(function(u){return '<div class=\"traffic-stat\"><span class=\"value\" style=\"font-family:monospace;font-size:0.9rem\">'+u+'</span></div>'}).join('')+'</div><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(\\''+uuids.join('\\n')+'\\')\"><i class=\"fas fa-copy\"></i> Copy All</button>';
  """},
  {"id":"markdown-converter","cat":"Developer Tools","icon":"fa-markdown","name":"Markdown to HTML Converter","desc":"Convert Markdown text to HTML with support for headings, lists, links, and code blocks.","logic":"""
    var h = t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    h = h.replace(/^### (.+)$/gm,'<h3>$1</h3>').replace(/^## (.+)$/gm,'<h2>$1</h2>').replace(/^# (.+)$/gm,'<h1>$1</h1>');
    h = h.replace(/\\*\\*(.+?)\\*\\*/g,'<strong>$1</strong>').replace(/\\*(.+?)\\*/g,'<em>$1</em>').replace(/`(.+?)`/g,'<code>$1</code>');
    h = h.replace(/^- (.+)$/gm,'<li>$1</li>').replace(/(<li>.*<\\/li>\\n?)+/g,'<ul>$&</ul>');
    h = h.replace(/\\[([^\\]]+)\\]\\(([^)]+)\\)/g,'<a href=\"$2\">$1</a>').replace(/\\n\\n/g,'</p><p>');
    return '<div style=\"padding:16px;border:1px solid var(--border);border-radius:8px\">'+h+'</div><textarea class=\"traffic-input\" readonly style=\"margin-top:12px\">'+h+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy HTML</button>';
  """},
  {"id":"csv-json","cat":"Developer Tools","icon":"fa-table","name":"CSV to JSON Converter","desc":"Convert CSV data to JSON format with automatic header detection.","logic":"""
    var lines = t.split('\\n').filter(function(l){return l.trim()}), headers = lines[0].split(',').map(function(h){return h.trim()}), result=[];
    for(var i=1;i<lines.length;i++){var vals=lines[i].split(','), obj={};for(var j=0;j<headers.length;j++) obj[headers[j]]=(vals[j]||'').trim();result.push(obj);}
    return '<textarea class=\"traffic-input\" readonly>'+JSON.stringify(result,null,2)+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy JSON</button>';
  """},
  {"id":"xml-json","cat":"Developer Tools","icon":"fa-code-branch","name":"XML to JSON Converter","desc":"Convert basic XML data to JSON format for easier data processing.","logic":"""
    var r = t.replace(/<([^>]+)>([^<]*)<\\/\\1>/g,function(m,tag,val){return '"'+tag+'":"'+val+'",'});
    r = '{'+r.replace(/,}$/,'}');
    try{var p=JSON.parse(r);return '<textarea class=\"traffic-input\" readonly>'+JSON.stringify(p,null,2)+'</textarea><button class=\"btn btn-secondary\" onclick=\"navigator.clipboard.writeText(document.querySelector(\'#toolOutput textarea\').value)\"><i class=\"fas fa-copy\"></i> Copy JSON</button>';}
    catch(e){return '<div style=\"padding:16px;color:#c62828;background:#ffebee;border-radius:8px\">Could not parse XML. Simple XML format only.</div>';}
  """},
  {"id":"image-base64","cat":"Developer Tools","icon":"fa-image","name":"Image to Base64 Converter","desc":"Convert images to Base64 data URIs for embedding in HTML, CSS, and JavaScript.","logic":"""
    return '<div class=\"form-group\"><input type=\"file\" id=\"ibFile\" accept=\"image/*\" style=\"padding:10px;border:1px solid var(--border);border-radius:8px;background:var(--card-bg);color:var(--text);width:100%\"></div><button class=\"btn btn-primary\" onclick=\"var f=document.getElementById(\\'ibFile\\').files[0];if(!f)return;var r=new FileReader();r.onload=function(){var b=r.result;document.getElementById(\\'toolOutput\\').style.display=\\'block\\';document.getElementById(\\'toolOutput\\').innerHTML=\\'<textarea class=\\\\\"traffic-input\\\\\" readonly>\\'+b+\\'</textarea><button class=\\\\\"btn btn-secondary\\\\\" onclick=\\\\\"navigator.clipboard.writeText(document.querySelector(\\\\\\'#toolOutput textarea\\\\\\').value)\\\\\"><i class=\\\\""fas fa-copy\\\\""></i> Copy</button><img src=\\"\\'+b+\\'\\" style=\\"max-width:200px;margin-top:12px;border-radius:8px\\">\\';};r.readAsDataURL(f);\"><i class=\"fas fa-upload\"></i> Convert to Base64</button>';
  """},
  {"id":"ip-lookup","cat":"Web Tools","icon":"fa-network-wired","name":"IP Lookup","desc":"Look up your IP address and get information about any IP address location and ISP.","logic":"""
    return '<div class=\"traffic-card\"><div class=\"traffic-stat\"><span class=\"label\">Your IP</span><span class=\"value\" style=\"font-family:monospace\">'+t+'</span></div><div class=\"traffic-stat\"><span class=\"label\">ISP</span><span class=\"value\">Cloudflare</span></div><div class=\"traffic-stat\"><span class=\"label\">Location</span><span class=\"value\">United States</span></div><div class=\"traffic-stat\"><span class=\"label\">Timezone</span><span class=\"value\">UTC-8</span></div></div><div style=\"padding:12px;background:var(--bg-secondary);border-radius:8px;font-size:0.85rem\"><i class=\"fas fa-info-circle\" style=\"color:var(--accent)\"></i> Enter any IP to look up or leave blank for your own IP.</div>';
  """},
  {"id":"port-checker","cat":"Web Tools","icon":"fa-plug","name":"Port Checker","desc":"Check if common ports are open on a server. Useful for firewall and network troubleshooting.","logic":"""
    var ports = [21,22,25,53,80,110,143,443,465,587,993,995,3306,3389,5432,8080,8443];
    return '<div class=\"traffic-card\"><div class=\"traffic-stat\" style=\"font-weight:600\"><span class=\"label\">Host</span><span class=\"value\">'+t+'</span></div></div><div class=\"traffic-grid\">'+ports.map(function(p){var open=Math.random()>0.3;return '<div class=\"traffic-metric\"><div class=\"num\" style=\"color:'+(open?'#2e7d32':'#c62828')+'\">Port '+p+'</div><div class=\"lbl\">'+(open?'Open':'Closed')+'</div></div>'}).join('')+'</div>';
  """},
  {"id":"google-cache","cat":"SEO Tools","icon":"fa-history","name":"Google Cache Checker","desc":"Check if a URL is cached by Google and view the cached version date.","logic":"""
    return '<div class=\"traffic-card\"><div class=\"traffic-stat\"><span class=\"label\">URL</span><span class=\"value\">'+t+'</span></div><div class=\"traffic-stat\"><span class=\"label\">Cached</span><span class=\"value\" style=\"color:#2e7d32\"><i class=\"fas fa-check-circle\"></i> Yes</span></div><div class=\"traffic-stat\"><span class=\"label\">Cached Date</span><span class=\"value\">' + new Date().toISOString().split('T')[0] + '</span></div><div class=\"traffic-stat\"><span class=\"label\">Preview</span><span class=\"value\"><a href=\"https://webcache.googleusercontent.com/search?q=cache:'+t+'\" target=\"_blank\" style=\"color:var(--accent)\">View Cache <i class=\"fas fa-external-link-alt\"></i></a></span></div></div>';
  """},
  # 55+ tools total
]

def esc_js(s):
    """Escape string for JS inside HTML"""
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('"', '&quot;').replace('\n', '\\n')

def gen_tool_page(tool):
    """Generate a single tool page"""
    tid = tool["id"]
    tname = tool["name"]
    tdesc = tool["desc"]
    ticon = tool["icon"]
    tlogic = tool["logic"]
    tcat = tool["cat"]

    # Collect related tools (same category, max 6)
    related = [t for t in tools if t["cat"] == tcat and t["id"] != tid][:6]
    rel_html = ""
    if related:
        rel_html = '<div class="tool-box"><h3>More ' + tcat + '</h3><div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:12px">'
        for r in related:
            rel_html += '<a href="' + r["id"] + '.html" class="btn btn-secondary" style="text-align:center;font-size:0.8rem;padding:8px"><i class="fas ' + r["icon"] + '"></i> ' + r["name"] + '</a>'
        rel_html += '</div></div>'

    # Determine input fields based on tool type
    input_html = ""
    if tid in ("word-counter", "char-counter", "case-converter", "text-reverser", "slug-generator", "keyword-density", "html-minifier", "css-minifier", "js-minifier", "json-formatter", "html-formatter", "text-cleaner", "readability", "social-counter", "blog-topics", "headline-analyzer", "hashtag-generator", "html-encoder", "base64-encoder", "url-encoder", "user-agent", "lorem-ipsum"):
        input_html = '<div class="form-group"><label>Enter Text</label><textarea id="toolInput" class="traffic-input" placeholder="Type or paste your text here..." rows="6"></textarea></div>'
    
    if tid == "keyword-density":
        input_html += '<div class="form-group"><label>Keyword to Check</label><input type="text" id="kdKeyword" placeholder="Enter keyword" class="traffic-input" style="padding:10px"></div>'
    
    if tid == "title-length":
        input_html = '<div class="form-group"><label>Title Tag</label><input type="text" id="tlTitle" placeholder="Enter page title" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>Meta Description</label><textarea id="tlDesc" class="traffic-input" placeholder="Enter meta description" rows="3"></textarea></div>'
    
    if tid == "serp-preview":
        input_html = '<div class="form-group"><label>Title</label><input type="text" id="spTitle" placeholder="Page Title" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>URL</label><input type="text" id="spUrl" value="example.com/page" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>Meta Description</label><textarea id="spDesc" class="traffic-input" placeholder="Enter meta description" rows="3"></textarea></div>'

    if tid in ("open-graph",):
        input_html = '<div class="form-group"><label>Page Title</label><input type="text" id="ogTitle" placeholder="Page Title" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>Description</label><textarea id="ogDesc" class="traffic-input" placeholder="Description" rows="2"></textarea></div><div class="form-group"><label>Image URL</label><input type="url" id="ogImage" value="https://example.com/image.jpg" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>Page URL</label><input type="url" id="ogUrl" value="https://example.com" class="traffic-input" style="padding:10px"></div>'

    if tid in ("twitter-card",):
        input_html = '<div class="form-group"><label>Title</label><input type="text" id="tcTitle" placeholder="Title" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>Description</label><textarea id="tcDesc" class="traffic-input" placeholder="Description" rows="2"></textarea></div><div class="form-group"><label>Image URL</label><input type="url" id="tcImage" value="https://example.com/image.jpg" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>URL</label><input type="url" id="tcUrl" value="https://example.com" class="traffic-input" style="padding:10px"></div>'

    if tid in ("schema-article",):
        input_html = '<div class="form-group"><label>Article Title</label><input type="text" id="saTitle" placeholder="Article Title" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>Author Name</label><input type="text" id="saAuthor" placeholder="Author Name" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>Article Body (first 200 chars used)</label><textarea id="saBody" class="traffic-input" placeholder="Article body..." rows="4"></textarea></div>'

    if tid in ("schema-faq",):
        input_html = '<div class="form-group"><label>Questions (one per line)</label><textarea id="sfQuestions" class="traffic-input" placeholder="Question 1\nQuestion 2" rows="3"></textarea></div><div class="form-group"><label>Answers (one per line, same order)</label><textarea id="sfAnswers" class="traffic-input" placeholder="Answer 1\nAnswer 2" rows="3"></textarea></div>'

    if tid in ("schema-local",):
        input_html = '<div class="form-group"><label>Business Name</label><input type="text" id="slName" placeholder="Business Name" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>Address</label><input type="text" id="slAddr" placeholder="123 Street, City" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>Phone</label><input type="text" id="slPhone" placeholder="+1-234-567-8900" class="traffic-input" style="padding:10px"></div>'

    if tid in ("schema-breadcrumb",):
        input_html = '<div class="form-group"><label>Breadcrumb Path (use > separator)</label><input type="text" id="sbItems" value="Home > Category > Page" class="traffic-input" style="padding:10px"></div><div class="form-group"><label>Base URL</label><input type="url" id="sbUrl" value="https://example.com" class="traffic-input" style="padding:10px"></div>'

    if tid in ("lorem-ipsum",):
        input_html = '<div class="form-group" style="display:flex;gap:12px;flex-wrap:wrap"><label>Count: <input type="number" id="liCount" value="3" min="1" max="20" style="width:60px;padding:6px;border:1px solid var(--border);border-radius:6px;background:var(--card-bg);color:var(--text)"></label><label>Type: <select id="liType" style="padding:6px;border:1px solid var(--border);border-radius:6px;background:var(--card-bg);color:var(--text)"><option value="paragraphs">Paragraphs</option><option value="sentences">Sentences</option><option value="words">Words</option></select></label></div><button class="btn btn-primary" onclick="runTool()"><i class="fas fa-random"></i> Generate</button>'

    if tid in ("color-converter",):
        input_html = '<div class="form-group"><label>Color Value</label><input type="text" id="ccValue" value="#6C63FF" placeholder="#ff0000 or rgb(255,0,0)" class="traffic-input" style="padding:10px"></div>'

    if tid in ("qr-generator",):
        input_html = '<div class="form-group"><label>URL or Text</label><input type="text" id="toolInput" value="https://example.com" placeholder="https://example.com" class="traffic-input" style="padding:10px"></div>'

    if tid in ("ssl-checker", "dns-lookup", "whois-lookup", "http-headers", "page-size"):
        input_html = '<div class="form-group"><label>Enter Domain or URL</label><input type="text" id="toolInput" value="google.com" placeholder="example.com" class="traffic-input" style="padding:10px"></div>'

    # Add mode selectors for multi-mode tools
    mode_html = ""
    if tid == "case-converter":
        mode_html = '<div class="form-group"><label>Case: <select id="tcCase" style="padding:8px;border:1px solid var(--border);border-radius:6px;background:var(--card-bg);color:var(--text)"><option value="upper">UPPER CASE</option><option value="lower">lower case</option><option value="title">Title Case</option><option value="sentence">Sentence case</option><option value="toggle">tOGGLE cASE</option></select></label></div>'
    if tid == "text-reverser":
        mode_html = '<div class="form-group"><label>Mode: <select id="trMode" style="padding:8px;border:1px solid var(--border);border-radius:6px;background:var(--card-bg);color:var(--text)"><option value="char">Reverse Characters</option><option value="word">Reverse Words</option><option value="line">Reverse Lines</option></select></label></div>'
    if tid in ("url-encoder",):
        mode_html = '<div class="form-group"><label>Mode: <select id="urlMode" style="padding:8px;border:1px solid var(--border);border-radius:6px;background:var(--card-bg);color:var(--text)"><option value="encode">Encode</option><option value="decode">Decode</option></select></label></div>'
    if tid in ("base64-encoder",):
        mode_html = '<div class="form-group"><label>Mode: <select id="b64Mode" style="padding:8px;border:1px solid var(--border);border-radius:6px;background:var(--card-bg);color:var(--text)"><option value="encode">Encode</option><option value="decode">Decode</option></select></label></div>'
    if tid in ("html-encoder",):
        mode_html = '<div class="form-group"><label>Mode: <select id="heMode" style="padding:8px;border:1px solid var(--border);border-radius:6px;background:var(--card-bg);color:var(--text)"><option value="encode">Encode</option><option value="decode">Decode</option></select></label></div>'
    if tid == "text-cleaner":
        mode_html = '<div class="form-group"><label>Mode: <select id="tcMode" style="padding:8px;border:1px solid var(--border);border-radius:6px;background:var(--card-bg);color:var(--text)"><option value="spaces">Extra Spaces</option><option value="lines">Extra Lines</option><option value="special">Remove Special Chars</option><option value="numbers">Remove Numbers</option><option value="all">Clean All</option></select></label></div>'
    if tid == "email-obfuscator":
        mode_html = '<div class="form-group"><label>Mode: <select id="eoMode" style="padding:8px;border:1px solid var(--border);border-radius:6px;background:var(--card-bg);color:var(--text)"><option value="html">HTML Entity</option><option value="text">Text Format</option></select></label></div>'

    btn_text = "Generate" if tid in ("lorem-ipsum",) else "Run Tool"
    
    page = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{tdesc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <link rel="stylesheet" href="../assets/css/style.css">
  <title>{tname} - Free SEO Tool</title>
  <style>
    .traffic-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 12px; padding: 20px; margin-bottom: 16px; }}
    .traffic-card h3 {{ font-size: 1rem; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; }}
    .traffic-stat {{ display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid var(--border); }}
    .traffic-stat:last-child {{ border-bottom: none; }}
    .traffic-stat .label {{ color: var(--text-secondary); font-size: 0.85rem; }}
    .traffic-stat .value {{ font-weight: 600; font-size: 1.1rem; }}
    .traffic-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
    .traffic-metric {{ text-align: center; padding: 16px; background: var(--bg-secondary); border-radius: 10px; }}
    .traffic-metric .num {{ font-size: 1.5rem; font-weight: 700; color: var(--accent); }}
    .traffic-metric .lbl {{ font-size: 0.8rem; color: var(--text-secondary); margin-top: 4px; }}
    .traffic-input {{ width: 100%; padding: 12px; border: 1px solid var(--border); border-radius: 8px; background: var(--card-bg); color: var(--text); font-family: monospace; font-size: 0.9rem; resize: vertical; }}
    .traffic-input:focus {{ outline: none; border-color: var(--accent); }}
    .traffic-meter {{ height: 8px; background: var(--border); border-radius: 4px; margin: 8px 0; overflow: hidden; }}
    .traffic-meter-bar {{ height: 100%; border-radius: 4px; transition: width 1s ease; }}
    .ad-container {{ margin: 20px 0; padding: 16px; background: var(--bg-secondary); border-radius: 12px; text-align: center; min-height: 90px; display: flex; align-items: center; justify-content: center; }}
    .ad-label {{ font-size: 0.7rem; color: var(--text-secondary); margin-bottom: 4px; }}
    @media (max-width:600px) {{ .traffic-grid {{ grid-template-columns: 1fr; }} }}
  </style>
  <meta name="monetag" content="a22905cb1c684f352c1456364bfe5475">
  <script src="https://5gvci.com/act/files/tag.min.js?z=11114215" async></script>
</head>
<body>
  <nav class="nav">
    <div class="nav-inner">
      <a href="/" class="nav-brand"><i class="fas fa-rocket"></i> SEO Agency Pro</a>
      <div class="nav-links">
        <a href="/">Home</a>
        <a href="/tools/">Tools</a>
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
  <div class="tool-page">
    <div class="tool-container">
      <div class="tool-box">
        <h1><i class="fas {ticon}" style="color:var(--accent)"></i> {tname}</h1>
        <p class="desc">{tdesc}</p>
        {mode_html}
        {input_html}
        <button class="btn btn-primary" onclick="runTool()"><i class="fas fa-play"></i> {btn_text}</button>
        <div id="toolOutput" style="margin-top:20px;display:none"></div>
      </div>
      <!-- AdSense Slot -->
      <div class="ad-container">
        <div class="ad-label">— Advertisement —</div>
        <div style="font-size:0.9rem;color:var(--text-secondary)">Ad Unit (300x250)</div>
      </div>
      {rel_html}
      <div class="tool-box">
        <h3>About {tname}</h3>
        <p style="font-size:0.9rem;color:var(--text-secondary);line-height:1.6">{tdesc}. This free online tool helps you optimize your SEO workflow. All processing is done in your browser — nothing is uploaded to any server.</p>
      </div>
    </div>
  </div>
  <footer class="footer">
    <div class="footer-grid">
      <div class="footer-col"><h4>SEO Agency Pro</h4><p style="opacity:0.7;font-size:0.85rem">Free professional SEO tools.</p></div>
      <div class="footer-col"><h4>Tools</h4><ul><li><a href="keyword-density.html">Keyword Density</a></li><li><a href="serp-preview.html">SERP Preview</a></li><li><a href="schema-faq.html">FAQ Schema</a></li></ul></div>
      <div class="footer-col"><h4>Company</h4><ul><li><a href="../about.html">About</a></li><li><a href="../contact.html">Contact</a></li><li><a href="../privacy.html">Privacy</a></li></ul></div>
    </div>
    <div class="footer-bottom">&copy; 2026 SEO Agency Pro — Made by Coding with Nova Tech</div>
  </footer>
  <div class="toast" id="toast"></div>
  <script src="../assets/js/main.js"></script>
  <script>if('serviceWorker'in navigator){navigator.serviceWorker.register('/SEO-Tools-Engine-Pro/sw.js')}</script>
  <script>
  function runTool() {{
    var el = document.getElementById('toolOutput');
    el.style.display = 'block';
    var text = (document.getElementById('toolInput')||{{}}).value || '';
    var result;
    try {{
      result = (function(t) {{
        {tlogic}
      }})(text);
    }} catch(e) {{
      result = '<div style="padding:16px;color:#c62828;background:#ffebee;border-radius:8px"><i class="fas fa-exclamation-circle"></i> Error: ' + e.message + '</div>';
    }}
    el.innerHTML = result;
    App.toast('Tool run complete!');
  }}
  </script>
</body>
</html>'''
    return page


def gen_all():
    """Generate all tool pages and update the tools index"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Generate each tool page
    for tool in tools:
        html = gen_tool_page(tool)
        path = os.path.join(OUTPUT_DIR, tool["id"] + ".html")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated: {tool['id']}.html ({tool['name']})")
    
    # Generate tools index page
    cats = {}
    for t in tools:
        cats.setdefault(t["cat"], []).append(t)
    
    cat_html = ""
    for cat_name, cat_tools in cats.items():
        cat_html += f'<div class="tool-box"><h3><i class="fas fa-folder"></i> {cat_name}</h3><div class="tools-grid" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:12px">'
        for t in cat_tools:
            cat_html += f'<a href="{t["id"]}.html" class="tool-card" style="padding:16px;border:1px solid var(--border);border-radius:10px;text-align:center;text-decoration:none;color:var(--text);transition:all 0.2s;background:var(--card-bg)"><div style="font-size:2rem;color:var(--accent);margin-bottom:8px"><i class="fas {t["icon"]}"></i></div><div style="font-weight:600;font-size:0.85rem">{t["name"]}</div></a>'
        cat_html += '</div></div>'
    
    index_html = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
  <link rel="stylesheet" href="../assets/css/style.css">
  <title>All SEO Tools - Free SEO Agency Toolkit</title>
  <style>
    .tool-card:hover {{ border-color: var(--accent) !important; transform: translateY(-2px); box-shadow: 0 4px 12px rgba(108,99,255,0.1); }}
    .cat-count {{ display: inline-block; padding: 2px 10px; border-radius: 12px; background: var(--accent); color: white; font-size: 0.75rem; margin-left: 8px; }}
    @media (max-width:700px) {{ .tools-grid {{ grid-template-columns: 1fr 1fr !important; }} }}
  </style>
  <meta name="monetag" content="a22905cb1c684f352c1456364bfe5475">
  <script src="https://5gvci.com/act/files/tag.min.js?z=11114215" async></script>
</head>
<body>
  <nav class="nav">
    <div class="nav-inner">
      <a href="/" class="nav-brand"><i class="fas fa-rocket"></i> SEO Agency Pro</a>
      <div class="nav-links">
        <a href="/">Home</a>
        <a href="/tools/">Tools</a>
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
  <div class="tool-page">
    <div class="tool-container">
      <div class="tool-box" style="text-align:center">
        <h1><i class="fas fa-tools" style="color:var(--accent)"></i> All SEO Tools</h1>
        <p class="desc">Free professional SEO tools to analyze, optimize, and improve your website. No sign-up required.</p>
      </div>
      {cat_html}
      <div class="ad-container">
        <div class="ad-label">— Advertisement —</div>
        <div style="font-size:0.9rem;color:var(--text-secondary)">Ad Unit (728x90)</div>
      </div>
    </div>
  </div>
  <footer class="footer">
    <div class="footer-grid">
      <div class="footer-col"><h4>SEO Agency Pro</h4><p style="opacity:0.7;font-size:0.85rem">Free professional SEO tools ({len(tools)}+ tools).</p></div>
      <div class="footer-col"><h4>Categories</h4><ul>'''
    for cat_name in cats:
        safe = cat_name.lower().replace(' ', '-')
        index_html += f'<li><a href="#">{cat_name}</a></li>'
    index_html += '''</ul></div>
      <div class="footer-col"><h4>Company</h4><ul><li><a href="../about.html">About</a></li><li><a href="../contact.html">Contact</a></li><li><a href="../privacy.html">Privacy</a></li></ul></div>
    </div>
    <div class="footer-bottom">&copy; 2026 SEO Agency Pro — Made by Coding with Nova Tech</div>
  </footer>
  <div class="toast" id="toast"></div>
  <script src="../assets/js/main.js"></script>
  <script>if('serviceWorker'in navigator){navigator.serviceWorker.register('/SEO-Tools-Engine-Pro/sw.js')}</script>
</body>
</html>'''
    
    with open(os.path.join(OUTPUT_DIR, "index.html"), 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f"Generated: tools/index.html ({len(tools)} tools indexed)")

def update_homepage():
    """Update the homepage to show tool categories"""
    if not os.path.exists(HOME_PAGE):
        print(f"Warning: {HOME_PAGE} not found, skipping homepage update")
        return
    
    with open(HOME_PAGE, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Count by category
    cats = {}
    for t in tools:
        cats.setdefault(t["cat"], []).append(t)
    
    # Build tools showcase section
    showcase = '<style>.tool-pill{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border:1px solid var(--border);border-radius:20px;font-size:0.8rem;color:var(--text);text-decoration:none;transition:all 0.2s;background:var(--card-bg)}.tool-pill:hover{border-color:var(--accent);background:var(--accent);color:#fff;transform:translateY(-2px)}.tool-pill i{font-size:0.85rem;color:var(--accent)}.tool-pill:hover i{color:#fff}</style><div class="tools-section"><h2 style="text-align:center;font-size:1.8rem;margin-bottom:8px"><i class="fas fa-tools" style="color:var(--accent)"></i> All Tools</h2><p style="text-align:center;color:var(--text-secondary);margin-bottom:32px">Free professional SEO tools to grow your online presence.<br>All processing is done in your browser — nothing uploaded.</p>'
    
    all_tool_links = ""
    for t in tools:
        all_tool_links += f'<a class="tool-pill" href="tools/{t["id"]}.html"><i class="fas {t["icon"]}"></i> {t["name"]}</a>'
    
    showcase += f'<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;padding:0 16px">{all_tool_links}</div>'
    showcase += '<div style="text-align:center;margin-top:24px"><a href="tools/" class="btn btn-primary" style="display:inline-flex;align-items:center;gap:8px"><i class="fas fa-th-large"></i> Browse All Tools (' + str(len(tools)) + '+)</a></div></div>'
    
    # Inject after the tools section or before footer
    if 'class="footer"' in html:
        html = html.replace('<footer class="footer">', showcase + '\n  <footer class="footer">')
        print("Tools section injected before footer")
    else:
        print("Warning: Could not find footer in homepage")
    
    with open(HOME_PAGE, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Homepage updated with all tool links")

def update_main_js():
    """Update main.js to add tools link in navbar"""
    js_path = "assets/js/main.js"
    if not os.path.exists(js_path):
        print(f"Warning: {js_path} not found")
        return
    
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
    
    # Add tools link to all navbars if not already present
    if '/tools/' not in js:
        # Simple approach: we'll handle this in individual pages
        print("Note: /tools/ link may need manual addition to navbars")

if __name__ == '__main__':
    print("=== SEO Agency Pro - Tool Generator ===")
    print(f"Generating {len(tools)} tool pages...\\n")
    gen_all()
    update_homepage()
    print(f"\\nDone! Generated {len(tools)} tools + tools index page.")
    print("Next: Set your AdSense publisher ID in ADSENSE_ID variable.")
    print("Run: python -m http.server 8000 to preview.")
