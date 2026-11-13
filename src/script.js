(function(){
  'use strict';
  var D=document, W=window, I=W.I18N||{};
  D.documentElement.classList.add('js');

  /* ---- tracking: pushes to dataLayer, and forwards to gtag / plausible if you add them ---- */
  function track(name,params){
    try{
      W.dataLayer=W.dataLayer||[];
      W.dataLayer.push(Object.assign({event:name},params||{}));
      if(typeof W.gtag==='function'){W.gtag('event',name,params||{});}
      if(typeof W.plausible==='function'){W.plausible(name,{props:params||{}});}
    }catch(e){}
  }

  /* ---- mobile menu ---- */
  var btn=D.getElementById('menu-btn'), links=D.getElementById('nav-links');
  if(btn&&links){
    btn.addEventListener('click',function(){
      var open=links.classList.toggle('open');
      btn.setAttribute('aria-expanded',open?'true':'false');
    });
    links.addEventListener('click',function(e){
      if(e.target.closest('a[href^="#"]')){links.classList.remove('open');btn.setAttribute('aria-expanded','false');}
    });
    D.addEventListener('keydown',function(e){
      if(e.key==='Escape'&&links.classList.contains('open')){links.classList.remove('open');btn.setAttribute('aria-expanded','false');btn.focus();}
    });
  }

  /* ---- reveal on scroll ---- */
  var rv=[].slice.call(D.querySelectorAll('.rv'));
  if('IntersectionObserver' in W){
    var ro=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');ro.unobserve(e.target);}});},{rootMargin:'0px 0px -8% 0px',threshold:.05});
    rv.forEach(function(el){ro.observe(el);});
  }else{rv.forEach(function(el){el.classList.add('in');});}

  /* ---- language switch keeps the current section ---- */
  var current='';
  var secs=[].slice.call(D.querySelectorAll('main section[id]'));
  if('IntersectionObserver' in W){
    var so=new IntersectionObserver(function(es){
      es.forEach(function(e){if(e.isIntersecting){current=e.target.id;}});
    },{rootMargin:'-35% 0px -55% 0px'});
    secs.forEach(function(s){so.observe(s);});
  }
  [].forEach.call(D.querySelectorAll('[data-lang-link]'),function(a){
    a.addEventListener('click',function(e){
      var id=(W.location.hash||'').replace('#','')||current;
      var base=a.getAttribute('href').split('#')[0];
      track('language_switch',{to:a.getAttribute('hreflang')});
      if(id&&id!=='top'){e.preventDefault();W.location.href=base+'#'+id;}
    });
  });

  /* ---- CTA / email tracking ---- */
  D.addEventListener('click',function(e){
    var a=e.target.closest('a');
    if(!a)return;
    if(a.classList.contains('btn')){track('cta_click',{label:(a.textContent||'').trim().slice(0,60),target:a.getAttribute('href')});}
    if((a.getAttribute('href')||'').indexOf('mailto:')===0){track('email_click');}
  });

  /* ---- calculator ---- */
  var calc=D.getElementById('calc');
  if(calc){
    var f=function(id){return D.getElementById(id);};
    var nf=new Intl.NumberFormat(I.locale||'sv-SE',{maximumFractionDigits:0});
    var touched=false;
    var update=function(){
      var n=Math.max(0,parseFloat(f('c-n').value)||0);
      var m=Math.max(0,parseFloat(f('c-m').value)||0);
      var r=Math.max(0,parseFloat(f('c-r').value)||0);
      var p=parseFloat(f('c-p').value)||0;
      f('c-p-out').textContent=p+' %';
      var hours=n*m/60*4.33*(p/100);
      var money=hours*r;
      f('r-h').textContent=nf.format(hours);
      f('r-m').textContent=nf.format(money);
      calc.dataset.hours=Math.round(hours);
      calc.dataset.money=Math.round(money);
    };
    calc.addEventListener('input',function(){update();if(!touched){touched=true;track('calculator_use');}});
    update();
    var cc=D.getElementById('calc-cta');
    if(cc){cc.addEventListener('click',function(){
      var msg=D.getElementById('f-msg');
      if(msg&&!msg.value){
        msg.value=(I.calcMsg||'').replace('{h}',nf.format(calc.dataset.hours)).replace('{m}',nf.format(calc.dataset.money)).replace('{n}',f('c-n').value).replace('{min}',f('c-m').value);
      }
      var sel=D.getElementById('f-topic');if(sel)sel.value='automation';
    });}
  }

  /* ---- contact form ---- */
  var form=D.getElementById('contact-form');
  if(form){
    var status=D.getElementById('form-status');
    var submit=form.querySelector('button[type=submit]');
    form.addEventListener('submit',function(e){
      e.preventDefault();
      status.className='status';status.textContent='';
      if(!form.checkValidity()){form.reportValidity();return;}
      var data=new FormData(form);
      if(data.get('_honey')){return;}
      var payload={
        name:data.get('name'),email:data.get('email'),company:data.get('company')||'-',
        topic:form.topic.options[form.topic.selectedIndex].text,message:data.get('message'),
        language:I.lang,_subject:I.subject,_template:'table',_captcha:'false'
      };
      submit.disabled=true;var old=submit.textContent;submit.textContent=I.sending;
      fetch(form.dataset.endpoint,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(payload)})
        .then(function(r){if(!r.ok)throw new Error('http '+r.status);return r.json();})
        .then(function(){
          status.className='status ok';status.textContent=I.ok;form.reset();
          track('generate_lead',{form:'contact',language:I.lang,topic:payload.topic});
        })
        .catch(function(){
          status.className='status err';
          status.innerHTML=I.err+' <a href="mailto:'+I.email+'">'+I.email+'</a>';
          track('form_error');
        })
        .then(function(){submit.disabled=false;submit.textContent=old;});
    });
  }
})();
