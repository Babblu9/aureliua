# Aurelius Academy of Global Studies — Design System

## 1. Visual Theme & Atmosphere

Aurelius Academy presents itself as a refined, scholarly brand for global university admissions coaching. The visual direction marries the gravitas of an established academic institution with the warmth of personalized mentorship. A deep navy dominates the brand, punctuated by a metallic gold accent that signals prestige and achievement. Generous whitespace, classical serif display type, and subtle card-based layouts create a calm, confident reading experience.

The atmosphere is intentionally institutional without feeling cold. Cream and off-white surfaces replace stark white, softening long-form content sections, while dark navy sections (hero, global outlook, pathways preview) provide dramatic contrast and visual rhythm. The recurring motif of gold rules, gradient top/bottom borders, and circular icon tiles reinforces a consistent visual language across pages.

**keyCharacteristics**

- Deep navy + metallic gold palette evoking academic prestige and global ambition
- Classical serif display typography (Cormorant Garamond) paired with clean sans-serif body copy (Poppins)
- Section-based page architecture, each introduced by a centered or left-aligned header with a small gold label and divider
- Card-driven content organization with hover-lift interactions
- Full-viewport hero with an animated canvas globe as the primary visual centerpiece
- Cream/off-white section backgrounds alternating with dark navy immersive bands
- Rounded corners kept modest (4–12 px) to maintain a formal, editorial feel
- Consistent uppercase micro-labels with wide letter-spacing for hierarchy

## 2. Color Palette & Roles

All base colors are defined as CSS custom properties in `css/style.css` `:root`. Alpha tints are derived from these variables and used throughout component backgrounds, borders, and text on dark surfaces. This document was grounded from local CSS/HTML/JS files without a live browser screenshot.

### Primary

| Hex | Role | Where seen |
| --- | --- | --- |
| `#1B2860` | Navy primary (`--navy`) | Hero gradient, section titles, buttons, contact icons, footer headings |
| `#0F1940` | Navy dark (`--navy-dark`) | Navbar background, footer background, darkest hero gradient stop |
| `#243480` | Navy mid (`--navy-mid`) | Hero gradient accent, page-hero gradient end |

### Accent

| Hex | Role | Where seen |
| --- | --- | --- |
| `#B8892A` | Gold primary (`--gold`) | Primary CTA buttons, active nav CTA, section labels, dividers, stat numerals |
| `#D4A843` | Gold light (`--gold-light`) | Hover states, logo dot, italic hero emphasis, icon strokes on dark tiles |
| `#F5EDD6` | Gold pale (`--gold-pale`) | Icon tile backgrounds, program tags, soft gold-tinted surfaces |

### Semantic

| Hex | Role | Where seen |
| --- | --- | --- |
| `#1A1A2E` | Text primary (`--text`) | Body copy on light surfaces |
| `#3D3D5C` | Text mid (`--text-mid`) | Secondary body copy, descriptions, form labels |
| `#4A4A5A` | Text light (`--text-light`) | Tertiary captions, university-card meta |

### Surfaces

| Hex | Role | Where seen |
| --- | --- | --- |
| `#FFFFFF` | White (`--white`) | Cards, contact form, general page background |
| `#FAF9F6` | Cream (`--cream`) | Alternating section backgrounds, programs section, contact section |
| `#F0F0EC` | Light gray (`--light-gray`) | Subject tags, subtle fills |

### Borders

| Hex | Role | Where seen |
| --- | --- | --- |
| `#E0DFDA` | Border default (`--border`) | Card borders, section separators, form borders, footer divider |

### Derived tints (qualitative)

- `rgba(27, 40, 96, 0.09–0.15)` — navy shadow tints used for card elevation
- `rgba(184, 137, 42, 0.10–0.40)` — gold glows, hover shadows, pill backgrounds
- `rgba(255, 255, 255, 0.04–0.10)` — glassy dark-card fills
- `rgba(255, 255, 255, 0.72)` — secondary text on navy backgrounds

## 3. Typography Rules

The type system pairs a high-contrast serif display face with a humanist sans-serif for UI and body copy. Both families are loaded from Google Fonts: Cormorant Garamond (300–700, italic 400) and Poppins (300–700).

**Font families**

- **Display / Headings:** `Cormorant Garamond`, Georgia, serif
- **Body / UI:** `Poppins`, -apple-system, sans-serif
- **Mono / Code:** not used

### Type scale

| Role | Font | Size | Weight | Line height | Letter spacing |
| --- | --- | --- | --- | --- | --- |
| Display (Hero H1) | Cormorant Garamond | `clamp(3rem, 5.5vw, 5rem)` | 600 | 1.07 | — |
| H1 (Section title) | Cormorant Garamond | `clamp(2rem, 4vw, 3rem)` | 600 | 1.15 | — |
| H2 (Page hero) | Cormorant Garamond | `clamp(2.4rem, 5vw, 4rem)` | 600 | 1.10 | — |
| H3 (Card title) | Cormorant Garamond | 1.5 rem | 600 | 1.20 | — |
| Body | Poppins | 1 rem | 400 | 1.70 | — |
| Body small | Poppins | 0.875 rem | 400 | 1.75 | — |
| Micro label | Poppins | 0.72 rem | 600–700 | 1.00 | 0.12–0.18 em |
| Button | Poppins | 0.82 rem | 600 | 1.00 | 0.07 em |
| Nav link | Poppins | 0.78 rem | 500 | 1.00 | 0.06 em |
| Mono / Code | — | not used | — | — | — |

Uppercase micro-labels are used for section labels, program tags, CTA badges, and footer headings. Italic Cormorant Garamond is reserved for pull quotes and the highlighted word in the hero title.

## 4. Component Stylings

### Buttons

| Variant | Background | Border | Text | Hover |
| --- | --- | --- | --- | --- |
| Primary gold | `var(--gold)` | none | white | `var(--gold-light)`, lift 2 px, gold shadow |
| Navy | `var(--navy)` | none | white | `var(--navy-dark)`, lift 2 px, navy shadow |
| Outline white | transparent | 1.5 px white/40 % | white | gold text + border, lift 2 px |
| Outline navy | transparent | 1.5 px navy | navy | navy fill, white text, lift 2 px |
| Outline gold | transparent | 2 px navy-dark | navy-dark | navy-dark fill, white text |

All buttons use `padding: 13px 32px`, `border-radius: 4px`, uppercase text, and `transition: all 0.3s ease`.

### Cards

- **Program card:** white background, 1 px `var(--border)` border, `border-radius: 8px`, `padding: 36px 32px`. A 3 px gold-to-gold-light gradient line sits at the top and scales in on hover (`transform: scaleX(1)`).
- **Why / Service / Value / Team card:** same 8 px radius and 1 px border; hover lifts 3 px and applies `box-shadow: var(--shadow)`.
- **Pathway card (dark):** translucent white fill (`rgba(255,255,255,0.04)`), white/8 % border; a 2 px gold bottom line scales in on hover.
- **Founder badge:** white card with 1 px border, 10 px radius, centered over the founder portrait.

### Inputs

Contact form inputs use `width: 100%`, `padding: 12px 16px`, `border: 1.5px solid var(--border)`, `border-radius: 6px`, Poppins 0.875 rem. Focus state darkens the border to `var(--navy)` with a 2 px outline offset.

### Navigation

- Fixed navbar, 76 px tall, `rgba(15,25,64,0.96)` background with `backdrop-filter: blur(16px)`.
- Logo combines an inline SVG monogram with wordmark: serif “Aurelius” uppercase (0.18 em tracking) over a gold “Academy of Global Studies” subtitle.
- Nav links are uppercase, 0.78 rem, white/80 %, with 8 px 14 px padding and 4 px radius. Active/hover states use gold text on a gold/10 % background.
- “Enquire Now” CTA is filled gold with white text.
- On scroll past 60 px, the navbar shrinks to 64 px and gains a stronger shadow (`js/main.js`).

### Image treatment

- Images are responsive (`max-width: 100%`, `display: block`).
- Founder photo uses `aspect-ratio: 4 / 5`, `border-radius: 12px`, `object-fit: cover`; currently displays a large gold serif “A” placeholder.
- Team avatars and pathway icons are circular (50 % radius).
- The hero relies on a canvas-drawn 3D globe rather than raster imagery.

### Distinctive components

1. **Hero 3D globe** — canvas element (`#heroGlobe`) rendered with a world map, graticule, surface dots, great-circle arcs from Hyderabad to global destinations, and a gold rim gradient. Respects `prefers-reduced-motion`.
2. **Section header module** — a reusable block of micro-label, serif title, and 56 px × 2 px gold divider, centered by default and left-aligned with `.left`.
3. **Admissions CTA band** — full-width gold-to-gold-light gradient section with navy-dark text, two action buttons, and translucent white badges.
4. **Comparison table** (programs page) — rounded 8 px table with gold and navy column heads and alternating rule rows.
5. **Timeline** (global pathways page) — two-column date/content list with gold uppercase month labels.

## 5. Layout Principles

### Spacing scale

The project does not enforce a fixed 4-pt scale, but the following pixel values recur across margins, padding, and gaps:

- **Micro:** 4, 8, 10, 12, 14, 16 px
- **Component:** 18, 20, 24, 28, 32, 36, 40 px
- **Section:** 48, 56, 64, 72, 80, 100 px

Key layout tokens:

- Section vertical padding: `100px 0` (desktop), `72px 0` (mobile)
- Container max-width: `1200px`
- Container horizontal padding: `40px` (desktop), `24px` (mobile)
- Navbar height: `76px` (scrolled `64px`)

### Grid behavior

- Default content container is a single centered column.
- Multi-column sections use CSS Grid with gaps of 24–80 px.
- Common patterns: `1fr 1fr`, `1.2fr 0.8fr`, `repeat(3, 1fr)`, `repeat(4, 1fr)`.
- The program grid includes a wide card spanning 2 columns on desktop.

### Whitespace philosophy

Large section gutters and a restrained 1200 px max-width create an airy, editorial layout. Dark sections (hero, global outlook, pathways preview) bleed full-width, while light sections are anchored by the container. Generous top/bottom padding separates narrative sections clearly.

### Radius scale

| Token | Value | Use |
| --- | --- | --- |
| Small | 4 px | Buttons, nav links, region nav pills |
| Default | 8 px | Cards, inputs, icon tiles, team avatars |
| Medium | 10–12 px | Founder badge, founder photo, program icons |
| Large | 20–24 px | Pills, badges, CTA labels |
| Pill | 999 px | Hero program chips, pathway university tags |

## 6. Depth & Elevation

Elevation is subtle and purposeful; most cards sit flat with only a border, gaining shadow on hover or scroll.

| Level | Shadow value | Role |
| --- | --- | --- |
| Rest | none (1 px border only) | Default card state |
| Soft | `0 4px 24px rgba(27,40,96,0.09)` | Hover on why/service/value/team cards; founder badge |
| Medium | `0 12px 48px rgba(27,40,96,0.15)` | Large structural shadow (`--shadow-lg`) |
| Lifted | `0 16px 48px rgba(27,40,96,0.13)` | Program card hover |
| Button | `0 8px 24px rgba(184,137,42,0.4)` / `rgba(15,25,64,0.4)` | Primary/navy button hover |
| Sticky nav | `0 4px 32px rgba(0,0,0,0.35)` | Navbar scrolled state |

**Philosophy:** Shadows are used sparingly as feedback for interactivity or to separate the sticky navigation from content, rather than to create persistent floating layers.

## 7. Interaction & Motion

### Hover states

- Buttons: background lightens, `translateY(-2px)`, and a colored shadow appears.
- Cards: `translateY(-3px to -5px)`, border color shifts toward gold/30 %, and `var(--shadow)` is applied.
- Links: color transitions to gold (`0.3s ease`).
- Program/pathway cards: a gold gradient line animates from `scaleX(0)` to `scaleX(1)`.

### Focus states

- Default focus: 2 px outline in `var(--navy)`, 2 px offset.
- Navbar/footer/dark-section links use `var(--gold-light)` outline for visibility.
- Form inputs gain a navy border and outline on focus.

### Scroll-driven motion

- **Fade-in elements:** `.fade-in` and `.fade-card` start at `opacity: 0` and `translateY(20–24px)`, transitioning to visible over `0.5–0.6s ease` when they enter the viewport.
- **Card stagger:** observed cards reveal with an 80 ms delay between siblings.
- **Stat counters:** numbers count up over `1800 ms` with a 16 ms interval when the stats bar is intersected.
- **Navbar:** shrinks and darkens after 60 px of scroll.

### Transitions

- Default easing is `0.3s ease` (`--ease`).
- Hero program pills and nav links use slightly snappier `0.2s` transitions for background/border.
- Globe animation uses a continuous rotation unless `prefers-reduced-motion: reduce` is enabled.

## 8. Responsive Behavior

The stylesheet uses a desktop-down approach with `max-width` media queries.

| Breakpoint | Actual query | Key changes |
| --- | --- | --- |
| Large desktop | default | Full multi-column grids, 1200 px container, 76 px navbar |
| Tablet landscape | `@media (max-width: 1024px)` | Hero becomes single column and globe hides; grids collapse to 1–2 columns; section padding unchanged |
| Tablet portrait | `@media (max-width: 900px)` | Pathway split and comparison table adapt (inline page styles) |
| Mobile | `@media (max-width: 768px)` | Hamburger replaces nav links; container padding 24 px; sections 72 px vertical; all grids single column |
| Small mobile | `@media (max-width: 600px)` | Programme component/journey grids stack (inline page styles) |

### Navigation collapse

At `768px` the nav links are hidden and replaced by a three-line hamburger. Clicking the hamburger opens a full-width navy dropdown (`nav-links.open`) and animates the lines into an X via inline transforms in `js/main.js`.

### Touch targets

- Hamburger button: visual 24 × 24 px lines with 8 px padding (40 px total tap area).
- Mobile nav links: `padding: 12px 16px`.
- Buttons: minimum height ~44 px including padding (inferred from `padding: 13px 32px` and font size).

### Image behavior

- The hero globe is removed on tablet and below (`display: none` at `1024px`).
- Founder portrait maxes at 340 px and centers on mobile.
- All images remain fluid via `max-width: 100%`.

## 9. Agent Prompt Guide

### Quick color reference

- Navy: `#1B2860`
- Navy dark: `#0F1940`
- Gold: `#B8892A`
- Gold light: `#D4A843`
- Cream: `#FAF9F6`
- Border: `#E0DFDA`
- Text: `#1A1A2E`

### Example prompts

1. “Build a landing page for an academic coaching brand using navy `#1B2860`, gold `#B8892A`, cream `#FAF9F6`, Cormorant Garamond headings, Poppins body, 8 px card radius, and a hero with an animated globe.”
2. “Create a responsive program-card grid with a gold top-border reveal on hover, using the Aurelius spacing scale and 1200 px container.”
3. “Design a contact form and footer in the Aurelius style: white card on cream section, navy inputs with 6 px radius, navy-dark footer, and gold-light section headings.”

### Iteration tips

- Keep gold as an accent only; never let it dominate a full section background except the admissions CTA band.
- Maintain the navy/gold/white rhythm by alternating one light section, one dark section, then back to light.
- Use uppercase micro-labels with 0.12–0.18 em letter-spacing before every major heading.
- Preserve the 8 px default radius for cards; use 4 px for buttons and 999 px for pills/tags.
- On dark sections, set secondary text to `rgba(255,255,255,0.72)` and subtle borders to `rgba(255,255,255,0.08–0.12)`.
- Ensure hover states combine a small lift (`translateY(-2px to -5px)`) with a border/shadow change rather than color alone.
