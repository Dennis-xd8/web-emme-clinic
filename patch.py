import re

content = open('index.html', encoding='utf-8').read()

# ── 1. Quitar sección biblioteca ──────────────────────────────────
bib_start = content.find('<!-- BIBLIOTECA -->')
bib_end   = content.find('<!-- CTA RESERVA -->')
content = content[:bib_start] + content[bib_end:]

# ── 2. Quitar WhatsApp flotante ───────────────────────────────────
wa_start = content.find('<!-- WHATSAPP FLOTANTE -->')
wa_end   = content.find('</a>', wa_start) + 4
content = content[:wa_start] + content[wa_end:]

# ── 3. Fix nec-header: 1 columna, texto debajo título ────────────
content = content.replace(
    '  .nec-header {\n    display: grid; grid-template-columns: 1fr 1fr; gap: 80px;\n    margin-bottom: 64px; align-items: end;\n  }',
    '  .nec-header {\n    display: flex; flex-direction: column; gap: 20px;\n    margin-bottom: 64px;\n  }'
)

# ── 4. Footer 2 cols en móvil small ──────────────────────────────
content = content.replace(
    '    .footer-grid { grid-template-columns: 1fr; gap: 20px; }',
    '    .footer-grid { grid-template-columns: 1fr 1fr; gap: 16px; }'
)

# ── 5. CSS carrusel (reemplaza .testi-section CSS) ────────────────
OLD_CSS = (
    '  /* ─── TESTIMONIOS ─── */\n'
    '  .testi-section {\n'
    '    padding: 100px 80px; background: var(--blanco);\n'
    '  }\n'
    '\n'
    '  .testi-grid {\n'
    '    display: grid; grid-template-columns: repeat(3,1fr); gap: 24px;\n'
    '    margin-top: 56px;\n'
    '  }\n'
    '\n'
    '  .testi-card {\n'
    '    padding: 36px 32px;\n'
    '    border: 0.5px solid var(--arena); position: relative;\n'
    '  }'
)

NEW_CSS = (
    '  /* ─── TESTIMONIOS CARRUSEL ─── */\n'
    '  .testi-section {\n'
    '    padding: 100px 80px; background: var(--blanco); overflow: hidden;\n'
    '  }\n'
    '  .testi-carousel-wrap { position: relative; margin-top: 56px; }\n'
    '  .testi-track-outer { overflow: hidden; }\n'
    '  .testi-track {\n'
    '    display: flex;\n'
    '    transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);\n'
    '    will-change: transform;\n'
    '  }\n'
    '  .testi-card {\n'
    '    padding: 36px 32px;\n'
    '    border: 0.5px solid var(--arena); position: relative;\n'
    '    flex: 0 0 calc(33.333% - 16px);\n'
    '    margin-right: 24px;\n'
    '    box-sizing: border-box;\n'
    '  }'
)

content = content.replace(OLD_CSS, NEW_CSS)

# ── 6. CSS dots/arrows/mobile carrusel (después de .quote-mark) ──
content = content.replace(
    '  /* ─── ANTES / DESPUÉS ─── */',
    '  .testi-dots {\n'
    '    display: flex; justify-content: center; gap: 8px; margin-top: 36px;\n'
    '  }\n'
    '  .testi-dot {\n'
    '    width: 6px; height: 6px; border-radius: 50%;\n'
    '    background: var(--arena); cursor: pointer;\n'
    '    transition: background .3s, transform .3s;\n'
    '    border: none; padding: 0;\n'
    '  }\n'
    '  .testi-dot.active { background: var(--carbon); transform: scale(1.3); }\n'
    '  .testi-arrows {\n'
    '    display: flex; justify-content: center; gap: 12px; margin-top: 20px;\n'
    '  }\n'
    '  .testi-arrow {\n'
    '    width: 40px; height: 40px; border: 0.5px solid var(--arena);\n'
    '    background: transparent; cursor: pointer; display: flex;\n'
    '    align-items: center; justify-content: center;\n'
    '    font-family: var(--font-body); font-size: 14px; color: var(--carbon);\n'
    '    transition: all .25s;\n'
    '  }\n'
    '  .testi-arrow:hover { background: var(--carbon); color: var(--blanco); border-color: var(--carbon); }\n'
    '\n'
    '  /* ─── ANTES / DESPUÉS ─── */'
)

# ── 7. HTML: reemplazar testi-section ────────────────────────────
old_testi = '''<section class="testi-section">
  <div class="label-tag">Lo que dicen nuestras pacientes</div>
  <h2 class="section-title">Resultados que <em>hablan</em></h2>

  <div class="testi-grid">
    <div class="testi-card">
      <div class="quote-mark">"</div>
      <div class="testi-stars">★★★★★</div>
      <p class="testi-text">"Llevaba tiempo queriendo hacerme algo en los labios pero tenía miedo de quedar exagerada. El resultado fue exactamente lo que buscaba: natural, armónico y yo misma."</p>
      <div class="testi-footer">
        <div class="testi-avatar">L</div>
        <div>
          <p class="testi-name">Laura M.</p>
          <p class="testi-tratamiento">Perfilado de labios</p>
        </div>
      </div>
    </div>
    <div class="testi-card">
      <div class="quote-mark">"</div>
      <div class="testi-stars">★★★★★</div>
      <p class="testi-text">"La Dra. Diana me explicó todo con una claridad increíble. Me hizo sentir que el tratamiento era mío, no el de una lista de procedimientos genéricos."</p>
      <div class="testi-footer">
        <div class="testi-avatar">S</div>
        <div>
          <p class="testi-name">Sofía R.</p>
          <p class="testi-tratamiento">Armonización facial</p>
        </div>
      </div>
    </div>
    <div class="testi-card">
      <div class="quote-mark">"</div>
      <div class="testi-stars">★★★★★</div>
      <p class="testi-text">"Nunca pensé que un microneedling me fuera a cambiar tanto la textura de la piel. Llevo 3 sesiones y la diferencia es brutal. Muy profesionales."</p>
      <div class="testi-footer">
        <div class="testi-avatar">M</div>
        <div>
          <p class="testi-name">María T.</p>
          <p class="testi-tratamiento">Microneedling · 3 sesiones</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

new_testi = '''<section class="testi-section">
  <div class="label-tag">Lo que dicen nuestras pacientes</div>
  <h2 class="section-title">Resultados que <em>hablan</em></h2>

  <div class="testi-carousel-wrap">
    <div class="testi-track-outer">
      <div class="testi-track" id="testiTrack">

        <div class="testi-card">
          <div class="quote-mark">"</div>
          <div class="testi-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="testi-text">"Me he realizado un tratamiento con la Dra. Heidy y la verdad que maravilloso. Una gran profesional, muy cercana con el paciente y muy pendiente de todo. Si buscas atenci&#243;n y asesoramiento de verdad, sin duda este es el lugar."</p>
          <div class="testi-footer">
            <div class="testi-avatar">Y</div>
            <div>
              <p class="testi-name">Yaya ll</p>
              <p class="testi-tratamiento">Tratamiento &middot; Google Local Guide</p>
            </div>
          </div>
        </div>

        <div class="testi-card">
          <div class="quote-mark">"</div>
          <div class="testi-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="testi-text">"Me acabo de hacer un aumento de labios con ellas. Iba super asustada pero no pueden ser m&#225;s profesionales, me calmaron desde el principio y me trataron como una reina. Han quedado super naturales."</p>
          <div class="testi-footer">
            <div class="testi-avatar">L</div>
            <div>
              <p class="testi-name">Lorena Gonz&#225;lez</p>
              <p class="testi-tratamiento">Labios &middot; Google Local Guide</p>
            </div>
          </div>
        </div>

        <div class="testi-card">
          <div class="quote-mark">"</div>
          <div class="testi-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="testi-text">"Mi madre se ha hecho un microblading de cejas con Diana y no podemos estar m&#225;s contentas. Las dos doctoras son s&#250;per profesionales, meticulosas con su trabajo y siempre preocupadas por el bienestar del paciente. Recomendad&#237;simas."</p>
          <div class="testi-footer">
            <div class="testi-avatar">L</div>
            <div>
              <p class="testi-name">Laura Panis</p>
              <p class="testi-tratamiento">Microblading &middot; Google Local Guide</p>
            </div>
          </div>
        </div>

        <div class="testi-card">
          <div class="quote-mark">"</div>
          <div class="testi-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="testi-text">"He ido ya unas 3 veces a hacerme peeling con dermapen y estoy encantada. La Dra. Heidy Rodr&#237;guez es muy profesional, cercana y est&#225; muy pendiente de que est&#233;s c&#243;moda. Los resultados: inmejorables."</p>
          <div class="testi-footer">
            <div class="testi-avatar">S</div>
            <div>
              <p class="testi-name">Sarita CD</p>
              <p class="testi-tratamiento">Peeling Dermapen &middot; Google Local Guide</p>
            </div>
          </div>
        </div>

        <div class="testi-card">
          <div class="quote-mark">"</div>
          <div class="testi-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <p class="testi-text">"Una cl&#237;nica que ofrece varios servicios y tratamientos. Me ayudan con los temas de la piel, siempre tienen en cuenta tu caso y son muy atentas. Adem&#225;s de profesionales, por supuesto. Muchas gracias."</p>
          <div class="testi-footer">
            <div class="testi-avatar">O</div>
            <div>
              <p class="testi-name">Olga Malinauskaite</p>
              <p class="testi-tratamiento">Piel &middot; Google Reviews</p>
            </div>
          </div>
        </div>

      </div>
    </div>
    <div class="testi-arrows">
      <button class="testi-arrow" id="testiPrev">&#8592;</button>
      <button class="testi-arrow" id="testiNext">&#8594;</button>
    </div>
    <div class="testi-dots" id="testiDots"></div>
  </div>
</section>'''

content = content.replace(old_testi, new_testi)

# ── 8. JS carrusel ───────────────────────────────────────────────
CAROUSEL_JS = r"""
  // Carrusel testimonios
  (function() {
    var track   = document.getElementById('testiTrack');
    var dotsEl  = document.getElementById('testiDots');
    var prevBtn = document.getElementById('testiPrev');
    var nextBtn = document.getElementById('testiNext');
    if (!track) return;

    var cards   = Array.from(track.children);
    var total   = cards.length;
    var current = 0;
    var timer;
    var dots    = [];

    function perView() { return window.innerWidth <= 900 ? 1 : 3; }
    function maxIndex() { return Math.max(0, total - perView()); }
    function cardWidth() { return cards[0].offsetWidth + 24; }

    function goTo(idx) {
      idx = Math.max(0, Math.min(idx, maxIndex()));
      current = idx;
      track.style.transform = 'translateX(-' + (cardWidth() * current) + 'px)';
      dots.forEach(function(d, i) { d.classList.toggle('active', i === current); });
    }

    function buildDots() {
      dotsEl.innerHTML = '';
      dots = [];
      for (var i = 0; i <= maxIndex(); i++) {
        (function(i) {
          var d = document.createElement('button');
          d.className = 'testi-dot' + (i === current ? ' active' : '');
          d.addEventListener('click', function() { goTo(i); resetTimer(); });
          dotsEl.appendChild(d);
          dots.push(d);
        })(i);
      }
    }

    prevBtn.addEventListener('click', function() { goTo(current - 1); resetTimer(); });
    nextBtn.addEventListener('click', function() { goTo(current + 1); resetTimer(); });

    function autoNext() { goTo(current >= maxIndex() ? 0 : current + 1); }
    function startTimer() { timer = setInterval(autoNext, 4500); }
    function resetTimer() { clearInterval(timer); startTimer(); }

    window.addEventListener('resize', function() { buildDots(); goTo(Math.min(current, maxIndex())); });

    var touchStartX = 0;
    track.addEventListener('touchstart', function(e) { touchStartX = e.touches[0].clientX; }, {passive:true});
    track.addEventListener('touchend', function(e) {
      var diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 40) { diff > 0 ? goTo(current + 1) : goTo(current - 1); resetTimer(); }
    });

    buildDots();
    goTo(0);
    startTimer();
  })();
"""

content = content.replace(
    "  const hamburger = document.getElementById('hamburger');",
    CAROUSEL_JS + "\n  const hamburger = document.getElementById('hamburger');"
)

# ── 9. Limpiar mobile CSS sobrante de blog y testi-grid ──────────
content = content.replace(
    '\n    /* ─── Blog ─── */\n    .blog-grid { grid-template-columns: 1fr; }\n    .blog-card.featured .blog-img { height: 200px; }\n',
    '\n'
)
content = content.replace(
    '    .testi-grid { grid-template-columns: 1fr; gap: 16px; }\n',
    ''
)
# Mobile testi card: 1 visible
mob_testi_css = (
    '    /* Mobile carrusel: 1 card */\n'
    '    .testi-card { flex: 0 0 calc(100% - 20px); margin-right: 20px; }\n'
)
content = content.replace(
    '    /* ─── Testimonios ─── */\n    .testi-grid { grid-template-columns: 1fr; }',
    mob_testi_css
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
