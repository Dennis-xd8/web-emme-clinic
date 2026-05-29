# EMME CLINIC — Contexto completo para desarrollo web
> Documento de briefing para Claude Code. Leer íntegro antes de escribir una sola línea de código.

---

## 1. QUIÉN ES EL CLIENTE

**Nombre de la clínica:** Emme Clinic  
**Tipo:** Clínica de medicina estética  
**Ubicación:** Calle Madrid 10, Castellón de la Plana (España)  
**Instagram clínica:** https://www.instagram.com/emme_clinic/

**Dos cofundadoras:**
- **Dra. Heidy Rodríguez** — @dra.heidyrodriguezl — Especialista en armonización facial, bótox avanzado y rellenos. Formación en medicina de familia vía MIR + especialización estética.
- **Dra. Diana López** — @dra.dianalopezp — Especialista en calidad de piel, longevidad y medicina anti-aging. Enfoque integrativo que combina estética y bienestar global.

Las fundadoras son el **corazón de la marca**. Deben tener protagonismo claro en toda la web, no aparecer como un apartado secundario.

---

## 2. CONCEPTO DE MARCA (NO NEGOCIABLE)

### Frase central
> **"Medicina estética de autor, con enfoque natural y trato humano."**

### Lo que Emme Clinic ES:
- Una clínica donde se practica medicina con **criterio propio**, no protocolos genéricos
- Un espacio de **escucha, diagnóstico honesto y resultados naturales**
- Una marca con **identidad doble** (las dos doctoras) que se complementan
- **Premium accesible**: lujo sobrio, no ostentoso ni inalcanzable

### Lo que Emme Clinic NO ES:
- Una clínica de ofertas o promociones agresivas
- Una web genérica de "tratamientos estéticos"
- Una marca que vende transformaciones extremas
- Una clínica clínica-fría o excesivamente corporativa

### Tagline definitivo
**"Realzamos. No transformamos."**

### Mensajes de apoyo que encajan con su comunicación pública:
- "Tratamientos personalizados con criterio médico."
- "Belleza natural, armonía y cuidado de la piel."
- "Escuchamos, valoramos y diseñamos contigo el mejor plan."
- "El resultado nunca debe gritar que has pasado por una clínica."

---

## 3. DISEÑO VISUAL (DIRECCIÓN ESTÉTICA)

### Concepto: "Lujo sobrio médico" — no clínico frío, no excesivamente rosa

### Paleta de colores
```
--crema:    #F7F3EE   → fondo principal cálido (casi blanco)
--marfil:   #EDE8E0   → superficies, tarjetas
--arena:    #D9C9B8   → bordes, separadores
--topo:     #A89585   → texto secundario, muted
--salvia:   #8A9E8C   → acento verde suave (etiquetas, tags)
--burdeos:  #7A3F3F   → acento cálido oscuro (hover states)
--carbon:   #1E1A18   → texto principal, fondos oscuros
--blanco:   #FDFAF7   → blanco cálido
--gold:     #B8956A   → acento dorado (el color especial de la marca)
```

**IMPORTANTE:** Sin rosas dominantes. Sin dorados excesivos. Sin gradientes agresivos. Sobriedad con calidez.

### Tipografía (OBLIGATORIA)
- **Display / Títulos:** `Cormorant Garamond` (Google Fonts) — weights 300, 400, italic
- **Cuerpo / UI:** `Montserrat` (Google Fonts) — weights 300, 400, 500

```html
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
```

### Estilo tipográfico
- Títulos principales: Cormorant Garamond, weight 300, letra-spacing ajustado, palabras en cursiva para énfasis en dorado
- Subtítulos y etiquetas: Montserrat uppercase, letter-spacing 0.15-0.22em, tamaño 10-11px
- Cuerpo: Montserrat weight 300, line-height 1.8-1.9
- Números decorativos: Cormorant Garamond weight 300, tamaño grande

### Estilo fotográfico (para placeholders y notas al cliente)
- Luz natural suave, tonos piel cálidos
- Retratos editoriales de las doctoras (no posadas clínicas)
- Detalles: manos, jeringas, texturas de piel, aparatología
- Interior de la clínica limpio y con personalidad
- Pacientes reales (con consentimiento), no modelos de stock

---

## 4. ARQUITECTURA WEB (SITEMAP COMPLETO)

```
/                         → Home
/nosotras                 → Sobre nosotras (historia, fundadoras, equipo, valores)
/tratamientos             → Índice de tratamientos
  /tratamientos/armonizacion-facial
  /tratamientos/labios
  /tratamientos/lineas-expresion
  /tratamientos/rejuvenecimiento
  /tratamientos/calidad-piel
  /tratamientos/microneedling
  /tratamientos/corporales
  /tratamientos/bienestar-longevidad
/metodo-emme              → El proceso de la clínica
/resultados               → Galería antes/después
/biblioteca               → Blog / artículos educativos
/faq                      → Preguntas frecuentes
/contacto                 → Contacto y reserva de cita
```

---

## 5. HOME — ESTRUCTURA SECCIÓN A SECCIÓN

La home responde 4 preguntas de forma inmediata: **quiénes somos · qué tratamos · por qué confiar · cómo reservar**

### 5.1 NAV (fija, scroll)
- Logo: `EMME` con la última E en dorado → `EMM<span style="color:gold">E</span>`
- Links: Nosotras · Tratamientos · Resultados · Biblioteca · Contacto
- CTA derecha: botón "Pide cita" (borde carbón, hover fondo carbón)
- Fondo: blanco cálido con backdrop-filter blur al hacer scroll
- Altura: 72px

### 5.2 HERO (100vh, grid 2 columnas)
**Columna izquierda:**
- Tag pequeño: `Medicina Estética · Castellón`
- Título grande (Cormorant 300): `Realzamos. No transformamos.` (o variación)
- Subtítulo (Montserrat 300, 13px): descripción breve de la propuesta de valor
- Dos CTAs: `Descubre los tratamientos` (botón sólido) + `Conoce a las doctoras` (ghost)
- Stats debajo: `+1.200 Pacientes · 2 Especialistas · 100% Resultados naturales`

**Columna derecha:**
- Fotografía editorial de las doctoras (placeholder marfil con formas)
- Badge flotante con cita de la marca: `"Escuchamos, valoramos y diseñamos contigo el mejor plan."` + `— El método Emme`

### 5.3 STRIP / MARQUEE
- Fondo carbón oscuro
- Texto desfilando: los tratamientos y valores de la marca en loop infinito
- Puntos dorados como separadores

### 5.4 ESPECIALIDADES (grid 4 columnas con borde)
- Numeradas 01–04: Facial · Piel · Corporal · Bienestar
- Cada tarjeta: número grande decorativo + nombre + lista de tratamientos
- Flecha ↗ en esquina, animada al hover
- Al hover: fondo marfil suave

### 5.5 EL MÉTODO EMME (fondo carbón, texto claro)
- Grid 2 columnas: izquierda texto + CTA / derecha 4 pasos
- Pasos: 01 Primera valoración · 02 Diagnóstico personalizado · 03 Plan de tratamiento · 04 Tratamiento & seguimiento
- Texto de fondo decorativo: `EMME` en enorme, opacidad muy baja
- CTA: `Reservar valoración gratuita`

### 5.6 FUNDADORAS (fondo crema)
- Grid 2 columnas, una tarjeta por doctora
- Cada tarjeta: foto editorial + nombre + especialidad + bio corta + pills de especialización + link `Ver perfil completo` + footer con @instagram
- Dra. Heidy: tono crema/salmón suave · Dra. Diana: tono verde salvia suave (diferenciadas visualmente)

### 5.7 DIAGNÓSTICO POR NECESIDAD
- Grid 2×2
- Orientado al problema del paciente, no al nombre técnico:
  1. "Quiero mejorar la calidad de mi piel" → tratamientos de piel
  2. "Quiero suavizar líneas y rejuvenecer" → bótox, rellenos
  3. "Quiero armonizar mis rasgos naturalmente" → armonización
  4. "Quiero cuidarme por dentro y por fuera" → bienestar & longevidad

### 5.8 LOS 4 PILARES FILOSOFÍA (franja horizontal, fondo marfil)
- I Naturalidad · II Seguridad · III Personalización · IV Armonía
- Numerales romanos decorativos en Cormorant grande, color arena
- 4 columnas con separadores

### 5.9 TESTIMONIOS
- 3 tarjetas con: estrellas + cita en cursiva (Cormorant) + nombre + tratamiento
- Comilla tipográfica decorativa grande en fondo
- Reseñas reales a añadir cuando el cliente las proporcione

### 5.10 ANTES / DESPUÉS
- 3 tarjetas con slider visual (conceptual en primera versión, funcional después)
- Pie de cada tarjeta: tratamiento + tiempo de resultado
- Aviso legal discreto: "resultados pueden variar"

### 5.11 BIBLIOTECA ESTÉTICA (Blog preview)
- Grid asimétrico: artículo destacado grande (izquierda) + 2 pequeños (derecha)
- Categorías: Armonización · Piel · Bienestar
- CTA a la sección completa de blog

### 5.12 CTA RESERVA / CONTACTO (fondo carbón)
- Grid 2 columnas: izquierda info + derecha formulario
- Formulario: Nombre · Teléfono · Email · Área de interés (dropdown) · Mensaje opcional
- Info: dirección Calle Madrid 10 Castellón + horario + "primera consulta gratuita"
- Decoración: círculo con borde fino en esquina derecha (fondo)

### 5.13 FOOTER
- Grid 4 columnas: logo+descripción · Tratamientos · Clínica · Contacto
- Links sociales: IG de la clínica + de cada doctora
- Aviso legal, política de privacidad

### 5.14 WHATSAPP FLOTANTE (fixed, bottom-right)
- Círculo verde #25D366
- Icono SVG de WhatsApp
- Animación suave al hover (scale 1.1)
- Link a: `https://wa.me/34XXXXXXXXX` (número a confirmar con cliente)

---

## 6. CATÁLOGO DE TRATAMIENTOS

### Faciales médicos
- Armonización facial completa
- Toxina botulínica (Bótox) — líneas de expresión
- Rellenos de ácido hialurónico
- Perfilado y aumento de labios
- Rinomodelación sin cirugía
- Remodelación de pómulos
- Corrección de ojeras (tear trough)
- Lifting de cola de ceja
- Jaw contouring (mandíbula)
- Proyección del mentón

### Calidad de piel
- Microneedling / Dermapen
- PRP facial (plasma rico en plaquetas)
- Mesoterapia facial
- Peelings químicos
- Bioestimuladores de colágeno (Sculptra, Radiesse)
- Tratamiento de manchas y melasma
- Hydrafacial
- Vitamina C intravenosa

### Corporales
- Radiofrecuencia corporal
- Lipolisis inyectable
- Tratamiento de celulitis
- Reducción de grasa localizada
- Tensado de piel post-parto
- Eliminación de estrías
- Depilación láser

### Bienestar & Longevidad
- Terapia IV vitamínica (vitaminas, glutatión)
- PRP capilar (alopecia)
- Mesoterapia capilar
- Medicina anti-aging
- Análisis de composición corporal
- Nutrición médica

### Estructura de cada ficha de tratamiento (página individual)
```
1. Qué problema o necesidad aborda
2. En qué consiste el tratamiento
3. Para quién está indicado
4. Valoración previa y personalización
5. Duración aproximada de la sesión
6. Cuidados posteriores
7. Resultados esperables
8. Galería antes/después del tratamiento
9. Preguntas frecuentes (FAQ)
10. CTA: "Solicitar primera valoración"
```

---

## 7. PÁGINA "SOBRE NOSOTRAS"

### Estructura
1. **Hero**: Título editorial + foto de las dos juntas
2. **Historia de origen**: cómo se conocieron, por qué fundaron Emme Clinic
3. **Dra. Heidy Rodríguez** — perfil completo:
   - Foto editorial (no clínica)
   - Formación médica (UASD + MIR medicina de familia + especialización estética)
   - Especialidades: armonización facial, bótox avanzado, rellenos
   - Filosofía personal de trabajo
   - Frase propia
4. **Dra. Diana López** — perfil completo:
   - Foto editorial
   - Formación y especialización en longevidad/anti-aging
   - Especialidades: calidad de piel, mesoterapia, bienestar integral
   - Filosofía personal
   - Frase propia
5. **Misión y valores** (los 4 pilares)
6. **Certificaciones y marcas** (Allergan, Galderma, etc. — a confirmar con cliente)
7. **El equipo** (si hay más personal)

---

## 8. FUNCIONALIDADES TÉCNICAS

### Prioridad alta (v1.0)
- [ ] Formulario de contacto funcional (email o integración)
- [ ] WhatsApp flotante con número real
- [ ] Navegación suave entre secciones (scroll behavior)
- [ ] Diseño 100% responsive (mobile-first)
- [ ] Optimización de imágenes (lazy loading)
- [ ] Meta tags SEO básicos por página
- [ ] Google Analytics 4
- [ ] Certificado SSL

### Prioridad media (v1.1)
- [ ] Slider antes/después interactivo (drag to compare)
- [ ] Feed de Instagram embebido en vivo
- [ ] Sistema de reserva de citas (Calendly o Doctoralia embed)
- [ ] Blog/CMS básico (Notion, Sanity, o similar)
- [ ] Reseñas de Google Maps en vivo (widget)

### Prioridad baja (v2.0)
- [ ] Chatbot de orientación por necesidad
- [ ] Área de pacientes (login)
- [ ] Newsletter

---

## 9. SEO — PALABRAS CLAVE OBJETIVO

### Primarias (alta intención)
- `clínica medicina estética Castellón`
- `armonización facial Castellón`
- `bótox Castellón`
- `rellenos ácido hialurónico Castellón`
- `microneedling Castellón`

### Secundarias
- `mejora calidad piel Castellón`
- `medicina estética natural Castellón`
- `aumento labios Castellón`
- `tratamientos antienvejecimiento Castellón`

### Técnico
- Una página por tratamiento (no agrupar todos en una sola)
- Schema markup: `MedicalClinic`, `Physician`, `MedicalProcedure`
- Open Graph tags para redes sociales
- Meta description única por página
- Sitemap XML
- Robots.txt
- NAP consistente: `Emme Clinic · Calle Madrid 10 · Castellón de la Plana`

---

## 10. STACK TÉCNICO RECOMENDADO

### Opción A — Astro + Tailwind (RECOMENDADA para SEO + velocidad)
```
Astro        → SSG, velocidad extrema, SEO perfecto
Tailwind CSS → utility-first, fácil de mantener
Netlify/Vercel → deploy
Sanity.io    → CMS para blog y tratamientos (opcional)
```

### Opción B — Next.js + Tailwind
```
Next.js      → SSR/SSG, buen SEO, ecosistema amplio
Tailwind CSS → estilos
Vercel       → deploy nativo
```

### Opción C — HTML/CSS/JS puro (más simple, sin framework)
```
HTML5 + CSS3 + Vanilla JS
Sin dependencias, máxima portabilidad
Ideal si no hay intención de blog o CMS
```

**El prototipo HTML ya existe** (ver archivo `emme-clinic.html`) y puede usarse como referencia visual exacta o como punto de partida para migrar a cualquier framework.

---

## 11. PROTOTIPO HTML DE REFERENCIA

Se ha desarrollado un prototipo navegable completo (`emme-clinic.html`) que incluye:
- ✅ Nav fija con scroll
- ✅ Hero 2 columnas con stats
- ✅ Strip marquee animado
- ✅ Grid de especialidades con hover
- ✅ Sección Método Emme (fondo oscuro)
- ✅ Tarjetas de las fundadoras
- ✅ Diagnóstico por necesidad (2×2)
- ✅ Los 4 pilares filosóficos
- ✅ Testimonios
- ✅ Antes/después (placeholder)
- ✅ Blog preview asimétrico
- ✅ Formulario de reserva
- ✅ Footer completo
- ✅ WhatsApp flotante

**Este archivo HTML es la fuente de verdad visual.** Usar como referencia exacta de colores, tipografía, espaciado y estructura.

---

## 12. INSTRUCCIONES PARA CLAUDE CODE

1. **Leer este documento completo** antes de escribir código.
2. **Respetar el concepto de marca** definido en la sección 2. No añadir elementos que contradigan el tono (sin rosas dominantes, sin gradientes de color, sin estética genérica de clínica).
3. **Usar las fuentes especificadas** (Cormorant Garamond + Montserrat). No sustituir por otras.
4. **Respetar la paleta de colores** definida en la sección 3. Usar variables CSS para toda la paleta.
5. **Empezar por la Home** siguiendo el orden de secciones del punto 5.
6. **Mobile-first**: diseñar pensando en móvil, escalar a desktop.
7. **El prototipo HTML** (`emme-clinic.html`) es la referencia visual. Puede usarse como base directa o como guía estética para reconstruir en el framework elegido.
8. **Textos en castellano** en toda la interfaz.
9. **Placeholders claros** donde vayan fotos reales (el cliente las aportará).
10. **Comentarios en el código** indicando dónde el cliente debe añadir: número de WhatsApp, fotos, reseñas reales, número de Google Analytics, etc.

### Comentarios de marcador a incluir en el código:
```html
<!-- TODO: Reemplazar con número de WhatsApp real -->
<!-- TODO: Añadir foto editorial Dra. Heidy -->
<!-- TODO: Añadir foto editorial Dra. Diana -->
<!-- TODO: Foto interior clínica -->
<!-- TODO: ID de Google Analytics -->
<!-- TODO: Reseñas reales de pacientes -->
<!-- TODO: Fotos antes/después con consentimiento -->
<!-- TODO: Número de colegiado médico -->
<!-- TODO: Registro sanitario -->
```

---

## 13. LO QUE EVITAR (explícitamente)

- ❌ Rosas dominantes o tonos demasiado "beauty influencer"
- ❌ Dorados excesivos (el gold es un ACENTO, no el color principal)
- ❌ Gradientes de color agresivos
- ❌ Fondos oscuros en toda la web (solo en la sección Método Emme y footer)
- ❌ Exceso de texto en bloques largos sin respiro visual
- ❌ Iconos genéricos de stock (emojis médicos, jeringas clipart)
- ❌ Tablas de precios en la home (las clínicas premium no muestran precios en portada)
- ❌ Promociones o descuentos en portada
- ❌ Galería de antes/después sin contexto médico-legal
- ❌ Diseño tipo "plantilla de clínica" (todo blanco + azul turquesa)
- ❌ Tipografías genéricas (Arial, Roboto, System-ui como display)
- ❌ Animaciones excesivas o llamativas
- ❌ Pop-ups intrusivos

---

## 14. CHECKLIST ANTES DEL LANZAMIENTO

- [ ] Todas las páginas tienen meta title + meta description únicos
- [ ] Open Graph tags configurados (para compartir en redes)
- [ ] Imágenes comprimidas y con atributo `alt` descriptivo
- [ ] Formulario probado (envía email de confirmación)
- [ ] WhatsApp flotante apunta al número correcto
- [ ] Google Analytics 4 instalado y verificado
- [ ] Google Search Console verificada
- [ ] Certificado SSL activo (HTTPS)
- [ ] Sitemap XML generado y enviado a Google
- [ ] Robots.txt configurado
- [ ] Política de privacidad publicada (RGPD — es España)
- [ ] Aviso de cookies implementado
- [ ] Registro sanitario visible (obligatorio para clínicas médicas en España)
- [ ] Textos legales revisados por el cliente
- [ ] Pruebas en: Chrome, Safari, Firefox + iOS y Android
- [ ] Velocidad de carga < 3 segundos (PageSpeed Insights)
- [ ] Accesibilidad básica (contrastes, etiquetas aria)
