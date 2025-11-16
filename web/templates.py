def generate_menu_html():
    """
    Genera HTML per il menu: minimal, assurdo, estremamente user friendly.

    Nota tecnica: usiamo un placeholder @@ITEMS@@ nel template per evitare
    errori dovuti a parentesi graffe presenti in CSS/JS quando si usa f-strings.
    """

    items_html = ""
    for idx, item in enumerate(Config.MENU_ITEMS):
        badge = f'<span class="badge">{item["badge"]}</span>' if item.get("badge") else ""
        img = item.get("image") or ""
        img_html = (
            f'<div class="product-obj" data-img="{img}"><span class="emoji">{item["emoji"]}</span></div>'
            if not img else
            f'<div class="product-obj" data-img="{img}"><img src="{img}" alt="{item["name"]}"/></div>'
        )

        items_html += f'''
  <article class="menu-card" tabindex="0" role="button" data-name="{item['name']}" data-price="{item['price']}">
    {img_html}

    <div class="info">
      <div class="top">
        <h3 class="title">{item['name']}</h3>
        {badge}
      </div>
      <p class="desc">{item['description']}</p>
      <div class="meta">
        <div class="price">{item['price']:.2f} €</div>
        <div class="controls">
          <button class="btn preview" aria-label="Anteprima {item['name']}">Anteprima</button>
          <button class="btn add" aria-label="Aggiungi {item['name']} al carrello">Aggiungi</button>
        </div>
      </div>
    </div>
  </article>
'''

    # TEMPLATE con placeholder semplice @@ITEMS@@ (Nessun f-string su tutto il blocco)
    html_template = """<!doctype html>
<html lang="it" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Menu — Minimal & Absurd</title>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700;900&display=swap" rel="stylesheet">
  <style>
    /* —— ROOT & THEME —— */
    :root{
      --bg: #f7f7fc;
      --card: #ffffff;
      --muted: #7b7f89;
      --accent: #111827;
      --accent-2: #7c3aed;
      --success: #10b981;
      --radius: 20px;
      --glass: rgba(255,255,255,0.6);
      --shadow: 0 6px 30px rgba(16,24,40,0.08);
      --transition: 240ms cubic-bezier(.2,.9,.3,1);
    }

    [data-theme="dark"]{
      --bg: #07070b;
      --card: rgba(255,255,255,0.03);
      --muted: rgba(255,255,255,0.6);
      --accent: #eef2ff;
      --glass: rgba(255,255,255,0.04);
    }

    *{box-sizing:border-box;margin:0;padding:0;font-synthesis:none}
    html,body{height:100%}
    body{font-family:Inter,system-ui,Segoe UI,Roboto,Arial; background:var(--bg); color:var(--accent); padding:28px; -webkit-font-smoothing:antialiased}

    /* —— LAYOUT —— */
    .wrap{max-width:980px;margin:0 auto}
    header{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px}
    .brand{display:flex;flex-direction:column;gap:2px}
    .brand h1{font-weight:900;font-size:20px;letter-spacing:-0.6px}
    .brand p{font-size:12px;color:var(--muted);font-weight:600}

    .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:18px}

    /* —— CARD (VERY MINIMAL) —— */
    .menu-card{display:flex;gap:16px;align-items:center;background:var(--card);border-radius:var(--radius);padding:18px;box-shadow:var(--shadow);transition:transform var(--transition),box-shadow var(--transition);cursor:pointer;outline:none}
    .menu-card:focus,.menu-card:hover{transform:translateY(-6px);box-shadow:0 18px 44px rgba(15,23,42,0.08)}

    .product-obj{width:104px;height:104px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:46px;flex-shrink:0;background:linear-gradient(135deg,transparent,transparent);position:relative;cursor:grab;user-select:none;transition:transform var(--transition)}
    .product-obj img{width:100%;height:100%;object-fit:cover;border-radius:12px}

    .info{flex:1;display:flex;flex-direction:column;gap:8px}
    .title{font-size:16px;font-weight:800;color:var(--accent)}
    .desc{font-size:13px;color:var(--muted);line-height:1.3}

    .meta{display:flex;justify-content:space-between;align-items:center;margin-top:6px}
    .price{font-weight:900;font-size:18px;color:var(--accent)}
    .controls{display:flex;gap:8px}
    .btn{border:none;background:transparent;padding:8px 12px;border-radius:12px;font-weight:700;cursor:pointer;transition:all var(--transition);font-size:13px}
    .btn.preview{background:transparent;color:var(--muted);border:1px solid rgba(0,0,0,0.04)}
    .btn.add{background:linear-gradient(90deg,var(--accent),var(--accent-2));color:white;box-shadow:0 10px 30px rgba(124,58,237,0.14)}

    /* —— CART BAR —— */
    .cart-bar{position:fixed;left:50%;transform:translateX(-50%);bottom:20px;background:var(--card);padding:14px;border-radius:14px;display:flex;gap:14px;align-items:center;box-shadow:var(--shadow);z-index:60;min-width:360px}
    .cart-summary{display:flex;flex-direction:column}
    .cart-total{font-weight:900;font-size:18px}
    .order-btn{background:var(--accent-2);color:white;padding:10px 18px;border-radius:12px;border:none;font-weight:800;cursor:pointer}
    .order-btn:disabled{opacity:0.45;cursor:not-allowed}

    /* —— MODALS —— */
    .overlay{position:fixed;inset:0;background:linear-gradient(180deg,rgba(2,6,23,0.55),transparent);display:none;align-items:center;justify-content:center;z-index:999}
    .overlay.active{display:flex}
    .panel{background:var(--card);padding:20px;border-radius:20px;min-width:320px;max-width:720px;box-shadow:0 30px 80px rgba(2,6,23,0.3);}

    .panel h2{margin-bottom:10px;font-size:18px}

    /* —— ORDER LIST —— */
    .order-list{max-height:50vh;overflow:auto;padding-right:6px}
    .order-row{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(0,0,0,0.04)}

    /* —— 3D PRODUCT PREVIEW —— */
    .preview-3d{width:320px;height:320px;margin:0 auto;display:flex;align-items:center;justify-content:center;touch-action:pan-y}
    .stage{width:260px;height:260px;border-radius:18px;background:var(--glass);display:flex;align-items:center;justify-content:center;transform-style:preserve-3d;transition:transform 300ms cubic-bezier(.2,.9,.3,1);box-shadow:0 8px 40px rgba(2,6,23,0.15)}
    .stage img,.stage .emoji{width:92%;height:92%;object-fit:contain;border-radius:14px}

    /* subtle instruction */
    .hint{font-size:12px;color:var(--muted);text-align:center;margin-top:8px}

    /* Accessibility focus */
    .menu-card:focus-visible{box-shadow:0 0 0 4px rgba(124,58,237,0.12)}

    @media (max-width:640px){
      .grid{grid-template-columns:1fr}
      .cart-bar{min-width:unset;left:16px;transform:none}
    }
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="brand">
        <h1>Durger — Menu</h1>
        <p>Minimal & absurd experience · Anteprima 3D · Checkout step-by-step</p>
      </div>
      <div class="actions">
        <button id="themeToggle" aria-label="Toggle theme">Tema</button>
      </div>
    </header>

    <main class="grid" id="menu">
      @@ITEMS@@
    </main>
  </div>

  <div class="cart-bar" role="region" aria-label="Carrello">
    <div class="cart-summary">
      <div id="cartBadge">0 articoli</div>
      <div class="cart-total" id="cartTotal">0,00 €</div>
    </div>
    <button class="order-btn" id="orderBtn" disabled>Anteprima ordine</button>
  </div>

  <div class="overlay" id="overlay" aria-hidden="true">
    <div class="panel" role="dialog" aria-modal="true" id="panel"></div>
  </div>

  <script>
    const cart = [];
    const menu = Array.from(document.querySelectorAll('.menu-card'));
    const fmt = p => p.toFixed(2).replace('.', ',') + ' €';

    document.addEventListener('DOMContentLoaded', () => {
      try { Telegram.WebApp.ready(); Telegram.WebApp.expand(); } catch(e){}
      attachHandlers(); updateCart();
    });

    function findCart(name) { return cart.find(i => i.name === name); }

    function updateCart() {
      const totalItems = cart.reduce((s,i)=>s+i.qty,0);
      const totalPrice = cart.reduce((s,i)=>s + i.qty * i.price,0);
      document.getElementById('cartBadge').textContent = totalItems + (totalItems===1? ' articolo':' articoli');
      document.getElementById('cartTotal').textContent = fmt(totalPrice);
      document.getElementById('orderBtn').disabled = totalItems === 0;
    }

    function attachHandlers() {
      document.querySelectorAll('.menu-card').forEach(card => {
        const addBtn = card.querySelector('.btn.add');
        const previewBtn = card.querySelector('.btn.preview');
        addBtn.addEventListener('click', (e) => { e.stopPropagation(); addToCart(card); });
        previewBtn.addEventListener('click', (e) => { e.stopPropagation(); openProductPreview(card); });
        card.addEventListener('click', () => openProductPreview(card));
      });
      document.getElementById('orderBtn').addEventListener('click', openOrderPreview);
      document.getElementById('themeToggle').addEventListener('click', toggleTheme);
    }

    function addToCart(card) {
      const name = card.dataset.name;
      const price = parseFloat(card.dataset.price);
      const found = findCart(name);
      if(found) found.qty += 1; else cart.push({name,price,qty:1});
      card.animate([{transform:'translateY(0)'},{transform:'translateY(-6px)'}],{duration:160,fill:'forwards'});
      updateCart();
      flash(card);
    }

    function flash(el) {
      el.style.transition = 'box-shadow 220ms';
      el.style.boxShadow = '0 18px 50px rgba(124,58,237,0.12)';
      setTimeout(()=>el.style.boxShadow='',220);
    }

    function openProductPreview(card) {
      const img = card.querySelector('.product-obj').dataset.img || '';
      const emoji = card.querySelector('.product-obj .emoji')?.textContent || '';
      const name = card.dataset.name;
      const price = parseFloat(card.dataset.price);
      const desc = card.querySelector('.desc').textContent;

      const panel = document.getElementById('panel');
      panel.innerHTML = `
        <h2>Anteprima: ${name} — ${price.toFixed(2).replace('.',',')} €</h2>
        <div class="preview-3d">
          <div class="stage" id="stage">
            ${img ? `<img src="${img}" alt="${name}"/>` : `<div class="emoji">${emoji}</div>`}
          </div>
        </div>
        <p class="hint">Trascina per ruotare • Tocca Aggiungi per metterlo nel carrello</p>
        <div style="display:flex;gap:10px;margin-top:14px;justify-content:flex-end;">
          <button class="btn" id="closePreview">Chiudi</button>
          <button class="btn add" id="addFromPreview">Aggiungi</button>
        </div>
      `;
      showOverlay();
      makeStageInteractive();
      document.getElementById('closePreview').addEventListener('click', hideOverlay);
      document.getElementById('addFromPreview').addEventListener('click', () => { addToCart(card); hideOverlay(); });
    }

    function makeStageInteractive() {
      const stage = document.getElementById('stage');
      if(!stage) return;
      let dragging = false; let last = null; let rotation = {x:0,y:0}; let vx = 0, vy = 0;
      stage.style.transform = `rotateX(${rotation.x}deg) rotateY(${rotation.y}deg)`;
      stage.addEventListener('pointerdown', (e) => { dragging = true; last = {x:e.clientX,y:e.clientY}; stage.setPointerCapture(e.pointerId); });
      stage.addEventListener('pointermove', (e) => {
        if(!dragging) return;
        const dx = e.clientX - last.x; const dy = e.clientY - last.y;
        rotation.y += dx * 0.35; rotation.x -= dy * 0.35;
        last = {x:e.clientX,y:e.clientY};
        vx = dx; vy = dy;
        stage.style.transform = `rotateX(${rotation.x}deg) rotateY(${rotation.y}deg)`;
      });
      stage.addEventListener('pointerup', (e) => {
        dragging = false; last = null; stage.releasePointerCapture(e.pointerId);
        const decay = 0.95; let rafId;
        (function inertia() {
          vx *= decay; vy *= decay;
          if(Math.abs(vx) < 0.05 && Math.abs(vy) < 0.05) return cancelAnimationFrame(rafId);
          rotation.y += vx * 0.5; rotation.x -= vy * 0.5;
          stage.style.transform = `rotateX(${rotation.x}deg) rotateY(${rotation.y}deg)`;
          rafId = requestAnimationFrame(inertia);
        })();
      });
      stage.addEventListener('pointercancel', () => { dragging=false; });
    }

    function openOrderPreview() {
      const panel = document.getElementById('panel');
      let total = 0;
      const rows = cart.map(item => { total += item.price * item.qty; return `<div class="order-row"><div>${item.name} × ${item.qty}</div><div>${fmt(item.price*item.qty)}</div></div>` }).join('');
      panel.innerHTML = `
        <h2>Anteprima ordine</h2>
        <div class="order-list">${rows || '<div class="hint">Il carrello è vuoto</div>'}</div>
        <div style="margin-top:12px;display:flex;justify-content:space-between;align-items:center"><strong>Totale</strong><strong>${fmt(total)}</strong></div>
        <div style="display:flex;gap:10px;margin-top:16px;justify-content:flex-end">
          <button class="btn" id="editCart">Modifica</button>
          <button class="btn add" id="checkout">Procedi al pagamento</button>
        </div>
      `;
      showOverlay();
      document.getElementById('editCart').addEventListener('click', () => { hideOverlay(); });
      document.getElementById('checkout').addEventListener('click', () => { confirmAndSend(); });
    }

    function confirmAndSend() {
      const panel = document.getElementById('panel');
      panel.innerHTML = '<h2>Invio ordine…</h2><p class="hint">Un attimo — prepariamo le pietanze.</p>';
      setTimeout(() => {
        try { Telegram.WebApp.sendData(JSON.stringify(cart)); Telegram.WebApp.close(); } catch(e){ console.log('send fallback', cart); hideOverlay(); alert('Ordine simulato: ' + JSON.stringify(cart)); }
      }, 800);
    }

    function showOverlay() {
      document.getElementById('overlay').classList.add('active');
      document.getElementById('overlay').setAttribute('aria-hidden','false');
    }
    function hideOverlay() {
      document.getElementById('overlay').classList.remove('active');
      document.getElementById('overlay').setAttribute('aria-hidden','true');
    }

    let dark = false;
    function toggleTheme() { dark = !dark; document.documentElement.setAttribute('data-theme', dark? 'dark':'light'); }

    window._menu = menu; window._cart = cart;
  </script>
</body>
</html>
"""

    # sostituisco il placeholder con l'HTML generato per gli items
    return html_template.replace('@@ITEMS@@', items_html)
