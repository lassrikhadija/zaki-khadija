/* NEXTIWEB — design 2026 : JS partagé (header, menu mobile, reveal fail-open, FAQ, halo souris, Loi 25) */

/* ---- Consentement cookies (Loi 25) — même clé/mécanisme partout ---- */
(function(){
  var KEY='nextiweb-cookie-consent-v1';
  function apply(p){var ds=document.documentElement.dataset;ds.cookieEssential='granted';ds.cookieAnalytics=p.analytics?'granted':'denied';ds.cookieMarketing=p.marketing?'granted':'denied';try{window.dispatchEvent(new CustomEvent('nextiweb:cookie-consent-updated',{detail:p}));}catch(e){}}
  function persist(p){try{localStorage.setItem(KEY,JSON.stringify({analytics:!!p.analytics,marketing:!!p.marketing}));}catch(e){}apply(p);}
  var c=document.getElementById('consent');
  var stored=null;try{stored=JSON.parse(localStorage.getItem(KEY));}catch(e){}
  if(stored&&typeof stored.analytics==='boolean'){apply(stored);}
  else if(c){c.hidden=false;}
  if(c){
    c.addEventListener('click',function(e){
      var btn=e.target.closest&&e.target.closest('[data-consent]');if(!btn)return;
      var a=btn.getAttribute('data-consent');
      if(a==='custom'){var o=document.getElementById('consentOpts');if(o)o.classList.toggle('show');return;}
      var p;
      if(a==='all')p={analytics:true,marketing:true};
      else if(a==='none')p={analytics:false,marketing:false};
      else if(a==='save')p={analytics:document.getElementById('cAnalytics').checked,marketing:document.getElementById('cMarketing').checked};
      else return;
      persist(p);c.hidden=true;
    });
  }
  document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-open-cookie-settings]');if(b&&c){c.hidden=false;var o=document.getElementById('consentOpts');if(o)o.classList.add('show');}});
})();

/* ---- Interactions UI partagées ---- */
(function(){
  var mq = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Header sticky : état "scrolled"
  var header=document.getElementById('header');
  if(header){ window.addEventListener('scroll',function(){header.classList.toggle('scrolled',window.scrollY>20);},{passive:true}); }

  // Menu mobile (tiroir)
  var t=document.getElementById('navToggle'),d=document.getElementById('drawer'),s=document.getElementById('scrim'),cl=document.getElementById('drawerClose');
  if(t&&d){
    function openD(){d.classList.add('open');if(s)s.classList.add('open');t.classList.add('open');}
    function closeD(){d.classList.remove('open');if(s)s.classList.remove('open');t.classList.remove('open');}
    t.addEventListener('click',openD);if(cl)cl.addEventListener('click',closeD);if(s)s.addEventListener('click',closeD);
    d.querySelectorAll('a').forEach(function(a){a.addEventListener('click',closeD);});
  }

  // Reveal au scroll — FAIL-OPEN (si le JS plante, le contenu reste visible)
  function nwRevealAll(){ document.querySelectorAll('.reveal').forEach(function(el){el.classList.add('in');}); }
  try{
    if('IntersectionObserver' in window && !mq){
      document.documentElement.classList.add('has-js');
      var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -8% 0px'});
      document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});
    } else { nwRevealAll(); }
  }catch(err){ nwRevealAll(); }

  // Accordéon FAQ
  document.querySelectorAll('.faq__item').forEach(function(item){
    var q=item.querySelector('.faq__q'),a=item.querySelector('.faq__a');
    if(!q||!a)return;
    q.addEventListener('click',function(){
      var isOpen=item.classList.contains('open');
      document.querySelectorAll('.faq__item').forEach(function(i){i.classList.remove('open');var aa=i.querySelector('.faq__a');if(aa)aa.style.maxHeight=null;});
      if(!isOpen){item.classList.add('open');a.style.maxHeight=a.scrollHeight+'px';}
    });
  });

  // Accordéon FAQ des articles de blog (.article-faq) — un seul ouvert à la fois
  document.querySelectorAll('.article-faq__btn').forEach(function(btn){
    btn.addEventListener('click',function(){
      var item=this.closest('.article-faq__item');if(!item)return;
      var isOpen=item.classList.contains('is-open');
      document.querySelectorAll('.article-faq__item').forEach(function(el){
        el.classList.remove('is-open');
        var b=el.querySelector('.article-faq__btn');if(b)b.setAttribute('aria-expanded','false');
      });
      if(!isOpen){item.classList.add('is-open');this.setAttribute('aria-expanded','true');}
    });
  });

  // Compteurs animés (data-count)
  function animateCount(el){var target=+el.getAttribute('data-count'),small=el.querySelector('small'),suffix=small?small.outerHTML:'';if(mq){el.innerHTML=target+suffix;return;}var start=null,dur=1100;function tick(ts){if(!start)start=ts;var p=Math.min((ts-start)/dur,1);el.innerHTML=Math.floor((1-Math.pow(1-p,3))*target)+suffix;if(p<1)requestAnimationFrame(tick);}requestAnimationFrame(tick);}
  if('IntersectionObserver' in window){var co=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){animateCount(e.target);co.unobserve(e.target);}});},{threshold:.6});document.querySelectorAll('[data-count]').forEach(function(el){co.observe(el);});}
  else{document.querySelectorAll('[data-count]').forEach(animateCount);}

  // Halo du hero (seulement si .hero + #spot présents)
  if(!mq){var hero=document.querySelector('.hero'),spot=document.getElementById('spot');if(hero&&spot){hero.addEventListener('mousemove',function(e){var r=hero.getBoundingClientRect();spot.style.left=(e.clientX-r.left)+'px';spot.style.top=(e.clientY-r.top)+'px';},{passive:true});}}

  // Halo discret qui suit la souris sur toute la page (souris fine)
  if(!mq && window.matchMedia('(pointer:fine)').matches){
    var glow=document.getElementById('cursorGlow');
    if(glow){
      var gx=0,gy=0,gRaf=0;
      window.addEventListener('mousemove',function(e){gx=e.clientX;gy=e.clientY;if(glow.style.opacity!=='1')glow.style.opacity='1';if(!gRaf)gRaf=requestAnimationFrame(function(){glow.style.transform='translate('+gx+'px,'+gy+'px) translate(-50%,-50%)';gRaf=0;});},{passive:true});
      window.addEventListener('mouseleave',function(){glow.style.opacity='0';},{passive:true});
    }
  }
})();
