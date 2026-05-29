import re

content = open('index.html', encoding='utf-8').read()

# ══════════════════════════════════════════════════════
# 1. NAV – quitar Biblioteca, Nosotras → #fundadoras
# ══════════════════════════════════════════════════════
content = content.replace(
    '<li><a href="nosotras.html">Nosotras</a></li>\n    <li><a href="#tratamientos">Tratamientos</a></li>\n    <li><a href="#resultados">Resultados</a></li>\n    <li><a href="#biblioteca">Biblioteca</a></li>\n    <li><a href="#reserva">Contacto</a></li>',
    '<li><a href="#fundadoras">Nosotras</a></li>\n    <li><a href="#tratamientos">Tratamientos</a></li>\n    <li><a href="#resultados">Resultados</a></li>\n    <li><a href="#reserva">Contacto</a></li>'
)
content = content.replace(
    '<a href="nosotras.html">Nosotras</a>\n  <a href="#tratamientos" class="nav-mobile-close">Tratamientos</a>\n  <a href="#resultados" class="nav-mobile-close">Resultados</a>\n  <a href="#biblioteca" class="nav-mobile-close">Biblioteca</a>\n  <a href="#reserva" class="nav-mobile-close">Contacto</a>\n  <a href="#reserva" class="nav-mobile-close">Pide cita →</a>',
    '<a href="#fundadoras" class="nav-mobile-close">Nosotras</a>\n  <a href="#tratamientos" class="nav-mobile-close">Tratamientos</a>\n  <a href="#resultados" class="nav-mobile-close">Resultados</a>\n  <a href="#reserva" class="nav-mobile-close">Contacto</a>\n  <a href="#reserva" class="nav-mobile-close">Pide cita →</a>'
)

# ══════════════════════════════════════════════════════
# 2. MOBILE NAV CSS – rediseño premium oscuro
# ══════════════════════════════════════════════════════
OLD_NAV_MOBILE_CSS = (
    '  .nav-mobile {\n'
    '    display: none;\n'
    '    position: fixed;\n'
    '    top: 72px;\n'
    '    left: 0; right: 0;\n'
    '    background: rgba(253,250,247,0.97);\n'
    '    backdrop-filter: blur(16px);\n'
    '    padding: 16px 24px 24px;\n'
    '    border-bottom: 0.5px solid rgba(168,149,133,0.2);\n'
    '    z-index: 99;\n'
    '    flex-direction: column;\n'
    '    gap: 0;\n'
    '  }\n'
    '  .nav-mobile.open { display: flex; }\n'
    '  .nav-mobile a {\n'
    '    font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase;\n'
    '    color: var(--topo); text-decoration: none; font-weight: 400;\n'
    '    padding: 14px 0; border-bottom: 0.5px solid rgba(168,149,133,0.15);\n'
    '    transition: color .25s;\n'
    '  }\n'
    '  .nav-mobile a:last-child { border-bottom: none; color: var(--carbon); font-weight: 500; }\n'
    '  .nav-mobile a:hover { color: var(--carbon); }'
)
NEW_NAV_MOBILE_CSS = (
    '  .nav-mobile {\n'
    '    display: none;\n'
    '    position: fixed;\n'
    '    top: 72px;\n'
    '    left: 0; right: 0;\n'
    '    background: var(--carbon);\n'
    '    z-index: 99;\n'
    '    flex-direction: column;\n'
    '    padding: 8px 0 16px;\n'
    '    box-shadow: 0 12px 40px rgba(0,0,0,0.25);\n'
    '  }\n'
    '  .nav-mobile.open { display: flex; }\n'
    '  .nav-mobile a {\n'
    '    font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase;\n'
    '    color: var(--arena); text-decoration: none; font-weight: 300;\n'
    '    padding: 18px 32px;\n'
    '    border-bottom: 0.5px solid rgba(196,185,174,0.10);\n'
    '    transition: all .2s;\n'
    '    display: flex; align-items: center; justify-content: space-between;\n'
    '  }\n'
    '  .nav-mobile a::after { content: "—"; color: var(--gold); font-size: 10px; opacity: 0; transition: opacity .2s; }\n'
    '  .nav-mobile a:hover { color: var(--blanco); padding-left: 40px; }\n'
    '  .nav-mobile a:hover::after { opacity: 1; }\n'
    '  .nav-mobile a:last-child { border-bottom: none; color: var(--gold); font-weight: 500; letter-spacing: 0.22em; }\n'
    '  .nav-mobile a:last-child:hover { color: var(--blanco); }'
)
content = content.replace(OLD_NAV_MOBILE_CSS, NEW_NAV_MOBILE_CSS)

# ══════════════════════════════════════════════════════
# 3. STRIP – más rápido en móvil
# ══════════════════════════════════════════════════════
content = content.replace(
    '    animation: marquee 24s linear infinite;',
    '    animation: marquee 28s linear infinite;'
)
# Insertar velocidad móvil después de @keyframes marquee
content = content.replace(
    '  @keyframes marquee {\n'
    '    from { transform: translateX(0); }\n'
    '    to { transform: translateX(-50%); }\n'
    '  }',
    '  @keyframes marquee {\n'
    '    from { transform: translateX(0); }\n'
    '    to { transform: translateX(-50%); }\n'
    '  }\n'
    '  @media (max-width: 900px) {\n'
    '    .strip-inner { animation-duration: 14s; }\n'
    '  }'
)

# ══════════════════════════════════════════════════════
# 4. TRATAMIENTOS – CSS nuevo (insertar antes de MÉTODO)
# ══════════════════════════════════════════════════════
content = content.replace(
    '  /* ─── MÉTODO EMME ─── */',
    '  /* ─── TRATAMIENTOS REDISEÑO ─── */\n'
    '  .trat-cat { margin-top: 52px; }\n'
    '  .trat-cat-header {\n'
    '    display: flex; align-items: baseline; gap: 20px;\n'
    '    padding-bottom: 16px; margin-bottom: 28px;\n'
    '    border-bottom: 0.5px solid var(--arena);\n'
    '  }\n'
    '  .trat-cat-num {\n'
    '    font-family: var(--font-display); font-size: 40px;\n'
    '    font-weight: 300; color: var(--arena); line-height: 1; flex-shrink: 0;\n'
    '  }\n'
    '  .trat-cat-title {\n'
    '    font-family: var(--font-display); font-size: 26px;\n'
    '    font-weight: 400; color: var(--carbon); line-height: 1.2;\n'
    '  }\n'
    '  .trat-services {\n'
    '    display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;\n'
    '  }\n'
    '  .trat-service { cursor: default; }\n'
    '  .trat-service-img {\n'
    '    background: var(--marfil);\n'
    '    height: 140px; margin-bottom: 10px;\n'
    '    overflow: hidden; transition: background .3s;\n'
    '  }\n'
    '  .trat-service:hover .trat-service-img { background: var(--arena); }\n'
    '  .trat-service-name {\n'
    '    font-size: 12px; letter-spacing: 0.03em;\n'
    '    color: var(--carbon); font-weight: 400;\n'
    '    line-height: 1.5; text-align: center;\n'
    '  }\n'
    '\n'
    '  /* ─── MÉTODO EMME ─── */'
)

# ══════════════════════════════════════════════════════
# 4b. TRATAMIENTOS – HTML completo (reemplaza sección)
# ══════════════════════════════════════════════════════
old_trat_start = content.find('<section class="section" id="tratamientos">')
old_trat_end   = content.find('</section>', old_trat_start) + len('</section>')
old_trat_html  = content[old_trat_start:old_trat_end]

new_trat_html = '''<section class="section" id="tratamientos">
  <div class="label-tag">Áreas de especialización</div>
  <h2 class="section-title">Tratamientos pensados<br>para ti, no para <em>todas.</em></h2>
  <p class="section-sub">Cada protocolo es único. Realizamos una valoración personalizada para diseñar el plan más adecuado a tus objetivos.</p>

  <!-- FACIAL -->
  <div class="trat-cat">
    <div class="trat-cat-header">
      <span class="trat-cat-num">01</span>
      <h3 class="trat-cat-title">Facial</h3>
    </div>
    <div class="trat-services">
      <div class="trat-service"><div class="trat-service-img" style="background-image:url(\'Fotos_tratamientos/foto_facial.jpg\');background-size:cover;background-position:center"></div><p class="trat-service-name">Armonización facial</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Arrugas tercio superior</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Pómulos</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Labios</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Marcación mandibular</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Mentón</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Skinbosters</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Bioestimuladores</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Vitaminas</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Peeling químico</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Radiofrecuencia facial con microagujas</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Luz pulsada intensa (IPL)</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Radiofrecuencia Diamond Polar</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Limpieza facial profunda</p></div>
    </div>
  </div>

  <!-- CORPORAL -->
  <div class="trat-cat">
    <div class="trat-cat-header">
      <span class="trat-cat-num">02</span>
      <h3 class="trat-cat-title">Corporal</h3>
    </div>
    <div class="trat-services">
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Radiofrecuencia Octipolar</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Carboxiterapia</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Endoliften</p></div>
    </div>
  </div>

  <!-- REDUCTORES NO QUIRÚRGICOS -->
  <div class="trat-cat">
    <div class="trat-cat-header">
      <span class="trat-cat-num">03</span>
      <h3 class="trat-cat-title">Tratamientos reductores<br>no quirúrgicos</h3>
    </div>
    <div class="trat-services">
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Mesoterapia</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Maderoterapia</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Masajes reductores<br>(Técnica Colombian Sculpting)</p></div>
      <div class="trat-service"><div class="trat-service-img"></div><p class="trat-service-name">Masajes drenantes</p></div>
    </div>
  </div>
</section>'''

content = content.replace(old_trat_html, new_trat_html)

# ══════════════════════════════════════════════════════
# 4c. TRATAMIENTOS – mobile CSS (dentro del @media 900px)
# ══════════════════════════════════════════════════════
content = content.replace(
    '    /* ─── DIAGNÓSTICO ─── */\n'
    '    .nec-header { grid-template-columns: 1fr; gap: 16px; margin-bottom: 32px; }\n'
    '    .nec-grid { grid-template-columns: 1fr 1fr; }',
    '    /* ─── TRATAMIENTOS ─── */\n'
    '    .trat-services { grid-template-columns: repeat(2, 1fr); gap: 14px; }\n'
    '    .trat-service-img { height: 110px; }\n'
    '    .trat-cat-num { font-size: 28px; }\n'
    '    .trat-cat-title { font-size: 20px; }\n'
    '\n'
    '    /* ─── DIAGNÓSTICO ─── */\n'
    '    .nec-header { grid-template-columns: 1fr; gap: 16px; margin-bottom: 32px; }\n'
    '    .nec-grid { grid-template-columns: 1fr 1fr; }'
)

# ══════════════════════════════════════════════════════
# 5. TESTIMONIOS – quitar "· Google Local Guide" / "· Google Reviews"
# ══════════════════════════════════════════════════════
content = content.replace('Tratamiento &middot; Google Local Guide', 'Tratamiento')
content = content.replace('Labios &middot; Google Local Guide', 'Labios')
content = content.replace('Microblading &middot; Google Local Guide', 'Microblading')
content = content.replace('Peeling Dermapen &middot; Google Local Guide', 'Peeling Dermapen')
content = content.replace('Piel &middot; Google Reviews', 'Piel')

# ══════════════════════════════════════════════════════
# 6. FUENTE – subir tamaños clave
# ══════════════════════════════════════════════════════
# label-tag: 10→11px
content = content.replace(
    '  .label-tag {\n    font-size: 10px;',
    '  .label-tag {\n    font-size: 11px;'
)
# hero-sub: 13→14px
content = content.replace(
    '  .hero-sub {\n    font-size: 13px; color: var(--topo); line-height: 1.9;',
    '  .hero-sub {\n    font-size: 14px; color: var(--topo); line-height: 1.9;'
)
# section-sub: 13→14px
content = content.replace(
    '  .section-sub {\n    font-size: 13px; color: var(--topo); line-height: 1.9; max-width: 520px;',
    '  .section-sub {\n    font-size: 14px; color: var(--topo); line-height: 1.9; max-width: 520px;'
)
# nav-links: 11→12px
content = content.replace(
    '    font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase;\n'
    '    color: var(--topo); text-decoration: none; font-weight: 400;',
    '    font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase;\n'
    '    color: var(--topo); text-decoration: none; font-weight: 400;'
)
# strip: 11→12px
content = content.replace(
    '    font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase;\n'
    '    color: var(--arena);',
    '    font-size: 12px; letter-spacing: 0.2em; text-transform: uppercase;\n'
    '    color: var(--arena);'
)
# testi-text: 17→18px
content = content.replace(
    '    font-family: var(--font-display); font-size: 17px; font-style: italic;',
    '    font-family: var(--font-display); font-size: 18px; font-style: italic;'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('patch2 OK')
