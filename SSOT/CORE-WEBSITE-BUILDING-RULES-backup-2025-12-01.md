# Core Website Building Rules

**Purpose**: Universal principles and rules for building effective websites
**Date**: 2025-11-30
**Status**: Production reference - Industry standards
**Version**: 1.0
**Sources**: Nielsen Norman Group, W3C WCAG, Material Design, Smashing Magazine, Web.dev, U.S. Web Design System

---

## Table of Contents

1. [Foundation Principles](#foundation-principles)
2. [Accessibility Standards (WCAG)](#accessibility-standards-wcag)
3. [Typography Rules](#typography-rules)
4. [Spacing & Whitespace System](#spacing--whitespace-system)
5. [Color & Contrast](#color--contrast)
6. [Layout & Grid Systems](#layout--grid-systems)
7. [Responsive Design Rules](#responsive-design-rules)
8. [Content & UX Writing](#content--ux-writing)
9. [Navigation & Interaction](#navigation--interaction)
10. [Performance & Technical](#performance--technical)
11. [Quick Reference Checklist](#quick-reference-checklist)

---

## Foundation Principles

### Nielsen's 10 Usability Heuristics

**1. Visibility of System Status**
- Always inform users about what's happening
- Provide feedback within reasonable time
- Examples: Loading spinners, progress bars, success messages
- **Rule**: Every user action should have immediate visual feedback

**2. Match Between System and Real World**
- Use familiar language and concepts
- Follow real-world conventions
- Avoid internal jargon or technical terms
- **Rule**: Speak the user's language, not yours

**3. User Control and Freedom**
- Provide clear "undo" and "redo" options
- Allow users to cancel actions
- Always offer escape routes
- **Rule**: Users should never feel trapped

**4. Consistency and Standards**
- Use same words, colors, layouts for same things
- Follow platform conventions (iOS, Android, Web)
- Don't reinvent standard UI patterns
- **Rule**: Be boring in a good way - predictable patterns build trust

**5. Error Prevention**
- Design to prevent errors before they happen
- Use constraints, confirmations, and defaults
- Better than good error messages
- **Rule**: Eliminate error-prone conditions

**6. Recognition Rather than Recall**
- Make options visible
- Don't force users to remember information
- Show hints, tooltips, examples
- **Rule**: Don't make users remember things from page to page

**7. Flexibility and Efficiency**
- Provide shortcuts for experts
- Allow customization
- Support both novice and expert users
- **Rule**: Accommodate different skill levels

**8. Aesthetic and Minimalist Design**
- Remove unnecessary elements
- Every element competes for attention
- Focus on essentials
- **Rule**: When in doubt, leave it out

**9. Help Users Recognize, Diagnose, and Recover from Errors**
- Use plain language error messages
- Clearly identify the problem
- Suggest constructive solutions
- **Rule**: Error messages should help, not blame

**10. Help and Documentation**
- Provide searchable, contextual help
- Use concrete, step-by-step guidance
- Keep it brief and task-focused
- **Rule**: Best help is no help needed (intuitive design)

---

### 10 Principles of Effective Web Design

**1. Don't Make Users Think**
- Obvious, self-explanatory interfaces
- Minimize conscious decision-making
- **Rule**: If a user has to ask "Can I click this?", you've failed

**2. Don't Squander Users' Patience**
- Minimize barriers to entry
- Don't force registration upfront
- Let users explore first
- **Rule**: Ask for minimum information, only when needed

**3. Manage Focus and Attention**
- Guide attention strategically
- Use visual hierarchy
- Motion and contrast = attention magnets
- **Rule**: One primary action per screen

**4. Strive for Feature Exposure**
- Make functions clearly visible
- Use visual guidelines
- Prominent calls-to-action
- **Rule**: Users can't use what they can't see

**5. Make Use of Effective Writing**
- Short phrases, scannable layout
- Multiple heading levels
- Plain language
- **Rule**: 50-80 characters per line for body text

**6. Strive for Simplicity**
- Prioritize content delivery
- Avoid unnecessary complexity
- **Rule**: Users come for content despite design, not because of it

**7. Don't Be Afraid of White Space**
- Reduce cognitive load
- Aid perception and scannability
- **Rule**: Whitespace is not wasted space

**8. Communicate Effectively with Visible Language**
- Organize consistently
- Use max 3 typefaces in max 3 sizes
- **Rule**: Typography = 95% of web design

**9. Conventions Are Our Friends**
- Follow established patterns
- Build on user expectations
- **Rule**: Don't reinvent the wheel

**10. Test Early, Test Often**
- Iterative usability testing
- Test with real users
- **Rule**: Testing one user is 100% better than testing none

---

## Accessibility Standards (WCAG)

### Four Core Principles: POUR

**1. Perceivable**
- Provide text alternatives for images (`alt` text)
- Captions for videos
- Adequate color contrast (minimum 4.5:1 for normal text)
- Content distinguishable (don't rely on color alone)
- Text resizable up to 200%

**Rules**:
- All images: `alt` attribute (empty if decorative)
- Videos: Captions and transcripts
- Color contrast: 4.5:1 for normal text, 3:1 for large text
- Don't use color as only visual indicator

**2. Operable**
- Full keyboard functionality (no mouse required)
- Sufficient time for user responses
- No seizure-inducing content (no flashing > 3 times/second)
- Clear navigation structures
- Skip navigation links

**Rules**:
- Every interactive element: keyboard accessible (Tab, Enter, Space, Arrow keys)
- Focus indicators: Always visible
- No time limits (or adjustable)
- Skip to main content link

**3. Understandable**
- Readable language
- Consistent navigation
- Logical sequencing
- Helpful error identification
- Clear labels and instructions

**Rules**:
- Specify page language (`<html lang="en">`)
- Navigation same order on all pages
- Form labels: Always visible (not just placeholder)
- Error messages: Specific, constructive

**4. Robust**
- Valid HTML markup
- Meaningful element names and roles
- Compatible with assistive technologies
- Works across browsers and devices

**Rules**:
- Semantic HTML (not `<div>` for everything)
- ARIA labels when semantic HTML insufficient
- Validate HTML (W3C validator)
- Test with screen readers (NVDA, JAWS, VoiceOver)

---

## Typography Rules

### Font Scale & Hierarchy

**Material Design System** (13 levels):
- Headlines 1-6 (largest → smallest)
- Subtitles 1-2 (medium emphasis)
- Body 1-2 (long-form)
- Caption, Overline (smallest)

**Practical Scale** (Recommended):
```
H1: 48px (3rem)     - Page title
H2: 36px (2.25rem)  - Section title
H3: 24px (1.5rem)   - Subsection title
H4: 20px (1.25rem)  - Card title
Body: 16px (1rem)   - Default text
Small: 14px (0.875rem) - Captions, meta
```

**Scale Ratio Rules**:
- Desktop: 1.250 (Major Third)
- Tablet: 1.200 (Minor Third)
- Mobile: 1.125 (Major Second)

**Rule**: Tighter ratios on small screens, greater contrast on large screens

### Line Length (Characters Per Line)

**Optimal**: 45-75 characters
**Ideal**: 66 characters (counting letters + spaces)

**Rule**:
- Desktop body text: 600-700px max width
- Mobile: 100% width (naturally limited)
- Never exceed 100 characters per line

### Line Height (Leading)

**Formula**: `line-height = 1.5` for body text

**Rules**:
- Body text (16px): 24px line-height (1.5)
- Headings: 1.2 - 1.3
- Small text: 1.4 - 1.5
- Large paragraphs: 1.6 - 1.8

**Why**: Larger blocks of text need more line height for readability

### Font Pairing

**Safe Combinations**:
1. Serif heading + Sans-serif body (classic)
2. Sans-serif heading + Serif body (modern)
3. Sans-serif heading + Sans-serif body (clean)

**Rules**:
- Maximum 2 font families per site
- Maximum 3 font weights
- Headings: Display, serif, or sans-serif
- Body text: ONLY serif or sans-serif (never display, script, handwritten)
- Buttons: Sans-serif, uppercase

### Web Units

**Use `rem` for typography**:
- Base: 16px = 1rem (browser default)
- Calculation: `px ÷ 16 = rem`
- Example: 24px = 1.5rem

**Why**: Respects user browser font size settings (accessibility)

---

## Spacing & Whitespace System

### 8-Point Grid System

**Base Unit**: 8px
**Half Step**: 4px (for icons, small text)

**Spacing Scale**:
```
4px   - Micro spacing (icon padding, tight elements)
8px   - Small gap (related items)
16px  - Default gap (most common)
24px  - Medium gap (section spacing)
32px  - Large gap (between distinct sections)
40px  - Extra large (major section breaks)
48px  - XXL (page sections)
64px  - Huge (hero sections)
80px  - Maximum (major divisions)
```

**Rule**: All spacing values should be multiples of 4px or 8px

### Spacing Hierarchy

```
Page Padding (60-80px)
  ├── Section Padding (40-60px)
  │   ├── Container Padding (24-40px)
  │   │   ├── Card Padding (16-32px)
  │   │   │   ├── Element Margin (8-16px)
  │   │   │   └── Micro Spacing (4-8px)
```

### Whitespace Types

**Micro Whitespace** (Between elements):
- Line spacing (leading)
- Letter spacing (tracking)
- Paragraph spacing
- List item gaps

**Macro Whitespace** (Around sections):
- Margins around major blocks
- Padding inside containers
- Page gutters
- Section breaks

**Rules**:
- More whitespace = More emphasis
- Related items: Less space between
- Unrelated items: More space between
- **Gestalt Proximity Principle**: Things close together = perceived as related

### Padding vs Margin

**Padding** (Internal spacing):
- Inside the element's border
- Affects element's clickable area
- Affects background color area

**Margin** (External spacing):
- Outside the element's border
- Creates gap between elements
- Collapses vertically (largest wins)

**Rule**:
- Use padding for internal spacing (cards, buttons)
- Use margin for gaps between elements
- Don't use both for same purpose (choose one pattern)

---

## Color & Contrast

### WCAG Contrast Requirements

**Normal Text** (< 18px or < 14px bold):
- **Minimum (AA)**: 4.5:1
- **Enhanced (AAA)**: 7:1

**Large Text** (≥ 18px or ≥ 14px bold):
- **Minimum (AA)**: 3:1
- **Enhanced (AAA)**: 4.5:1

**UI Components & Graphics**:
- **Minimum**: 3:1

**Tool**: Use WebAIM Contrast Checker (https://webaim.org/resources/contrastchecker/)

### Color System Rules

**Color Palette Size**:
- Primary: 1 main brand color
- Secondary: 1 accent color
- Neutral: 5-7 shades of gray
- Semantic: Success (green), warning (yellow), error (red), info (blue)
- Total: 8-12 colors maximum

**60-30-10 Rule**:
- 60%: Dominant color (usually neutral background)
- 30%: Secondary color (supporting areas)
- 10%: Accent color (calls-to-action, highlights)

**Don't Rely on Color Alone**:
- Use icons + color (not just color)
- Use text labels + color
- Use patterns + color (for charts)

**Rule**: If you remove all color (grayscale), interface should still be usable

### Color Psychology (Cultural Context)

**Western Culture**:
- Red: Urgency, error, passion
- Blue: Trust, calm, professional
- Green: Success, growth, natural
- Yellow: Warning, optimism, energy
- Orange: Friendly, affordable, playful
- Purple: Luxury, creativity, wisdom

**Rule**: Test colors with target audience (cultural differences exist)

---

## Layout & Grid Systems

### Grid Fundamentals

**12-Column Grid** (Most common):
- Flexible: 1, 2, 3, 4, 6, 12 columns
- Desktop: 1140px - 1200px max width
- Gutters: 24px - 32px

**8-Column Grid** (Alternative):
- Simpler: 1, 2, 4, 8 columns
- Mobile-friendly

**Rule**: Use grid consistently across all pages

### Container Widths

**Fixed Container**:
```
Desktop (> 1200px): 1140px
Laptop (992-1199px): 960px
Tablet (768-991px): 720px
Mobile (< 768px): 100% (with 16px padding)
```

**Fluid Container**:
- Width: 100%
- Max-width: 1200px
- Padding: 16px - 24px

**Rule**: Always add horizontal padding on 100% width containers

### Visual Hierarchy

**Z-Pattern** (Western reading):
```
[Top Left] ----→ [Top Right]
    ↓               ↓
[Bottom Left] -→ [Bottom Right]
```
Use for simple pages, landing pages

**F-Pattern** (Content-heavy):
```
[Full Width Header]
[Left Content] + [Right Sidebar]
[Left Content]
```
Use for articles, documentation

**Rule**: Place most important content in top-left, CTAs in top-right or center

### Layout Patterns

**Hero Section**:
- Full width or contained
- Large heading (48px+)
- 1-2 sentence description
- 1-2 clear CTAs
- Optional: Hero image/video

**Card Grid**:
- Equal height cards
- Consistent padding (24px - 32px)
- Clear hover states
- 2-4 columns on desktop
- 1 column on mobile

**Content + Sidebar**:
- Main: 66% width (8 columns)
- Sidebar: 33% width (4 columns)
- Swap on mobile (content first)

---

## Responsive Design Rules

### Mobile-First Approach

**Order**:
1. Design for mobile (320px - 480px)
2. Expand to tablet (768px - 1024px)
3. Expand to desktop (1200px+)

**Why**: Easier to add features than remove them

### Breakpoints

**Standard Breakpoints**:
```css
/* Mobile (default) */
/* No media query needed */

/* Tablet */
@media (min-width: 768px) { ... }

/* Desktop */
@media (min-width: 1024px) { ... }

/* Large Desktop */
@media (min-width: 1440px) { ... }
```

**Rule**: Let content determine breakpoints, not devices

### Responsive Typography

**Fluid Typography** (Scales with viewport):
```css
font-size: clamp(16px, 4vw, 24px);
/* min: 16px, ideal: 4% of viewport, max: 24px */
```

**Stepped Typography** (Breakpoint-based):
```css
h1 {
  font-size: 32px; /* Mobile */
}

@media (min-width: 768px) {
  h1 { font-size: 40px; } /* Tablet */
}

@media (min-width: 1024px) {
  h1 { font-size: 48px; } /* Desktop */
}
```

**Rule**: Base font should be 16px minimum (never smaller)

### Responsive Images

**Rules**:
```css
img {
  max-width: 100%;
  height: auto;
}
```

**Why**: Prevents overflow, maintains aspect ratio

**Responsive Images (HTML)**:
```html
<img
  src="image-800.jpg"
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 800px"
  alt="Description"
  width="800"
  height="600"
>
```

### Touch Targets

**Minimum Size**: 44px × 44px (Apple), 48px × 48px (Material Design)

**Spacing**: 8px minimum between touch targets

**Rule**: All interactive elements must be easily tappable on mobile

### Content Priority

**Mobile**: Show essential content only
**Desktop**: Can show additional features

**Don't Hide Critical Content on Mobile!**

---

## Content & UX Writing

### Writing for the Web

**Rules**:
1. **Scannable**: Use headings, bullets, short paragraphs
2. **Front-load**: Most important info first (inverted pyramid)
3. **Active voice**: "Click the button" not "The button should be clicked"
4. **Short sentences**: 15-20 words maximum
5. **Simple words**: Write at 8th-grade reading level
6. **Specific**: "Save 20%" not "Save money"

### Content Structure

**Paragraph Length**:
- Mobile: 2-3 sentences
- Desktop: 3-5 sentences
- Maximum: 7 sentences

**Heading Hierarchy**:
- One H1 per page (page title)
- H2 for main sections
- H3 for subsections
- Don't skip levels (H1 → H3)

**Bullet Points**:
- 3-7 items per list
- Parallel structure
- Each item: 1-2 lines
- Use when order doesn't matter

**Numbered Lists**:
- Use when order/sequence matters
- Maximum 10 items
- Each step: 1-2 sentences

### Call-to-Action (CTA) Rules

**Button Text**:
- **Good**: "Start Free Trial", "Download Guide", "Get Started"
- **Bad**: "Click Here", "Submit", "Learn More" (too vague)

**Rules**:
- Action-oriented verbs
- Specific outcome
- 2-4 words maximum
- One primary CTA per screen

**CTA Hierarchy**:
1. Primary (filled button, brand color)
2. Secondary (outline button)
3. Tertiary (text link)

---

## Navigation & Interaction

### Navigation Best Practices

**Main Navigation**:
- 5-7 items maximum
- Clear labels (1-2 words)
- Current page indicator
- Mobile: Hamburger menu

**Mega Menu** (If needed):
- Maximum 3 levels deep
- Organize by category
- Include visuals/icons

**Breadcrumbs**:
- Show on pages 3+ levels deep
- Format: Home > Category > Subcategory > Page
- Clickable links

**Footer Navigation**:
- Secondary pages (privacy, terms, etc.)
- Social media links
- Contact info

### Links & Buttons

**Link Rules**:
- Underlined or clearly different color
- Change on hover/focus
- Descriptive text ("Read our pricing guide" not "Click here")
- External links: Indicate (icon or note)

**Button States**:
- Default
- Hover (lighter/darker)
- Focus (outline for keyboard)
- Active (pressed)
- Disabled (grayed out, 50% opacity)

**Rule**: All interactive elements need all 5 states

### Forms

**Form Best Practices**:
1. **Label above input** (not inside placeholder)
2. **Required fields**: Clearly marked (asterisk)
3. **Input width**: Match expected content length
4. **Logical order**: Group related fields
5. **Error messages**: Inline, specific, helpful
6. **Success message**: Confirm submission

**Form Layout**:
- Single column (easier on mobile)
- Full-width fields (except short fields like ZIP)
- Sufficient spacing (16px between fields)

**Validation**:
- Inline validation (as user types or on blur)
- Clear error styling (red border, icon, message)
- Don't clear field on error (let user fix it)

---

## Performance & Technical

### Page Speed Rules

**Core Web Vitals**:
1. **LCP (Largest Contentful Paint)**: < 2.5s
2. **FID (First Input Delay)**: < 100ms
3. **CLS (Cumulative Layout Shift)**: < 0.1

**Page Size**:
- Total: < 2MB
- Images: Optimize (WebP format, lazy loading)
- Scripts: Minimize, defer non-critical

**Rules**:
- Optimize images (compress, correct dimensions)
- Lazy load images below fold
- Minimize HTTP requests
- Use browser caching
- Minify CSS/JS

### SEO Basics

**On-Page SEO**:
- One H1 per page (with target keyword)
- Unique page titles (50-60 characters)
- Meta descriptions (150-160 characters)
- Descriptive URLs (kebab-case)
- Image alt text (descriptive, keyword-rich)
- Internal links (3-5 per page)

**Technical SEO**:
- XML sitemap
- Robots.txt
- 301 redirects (not 302)
- HTTPS (SSL certificate)
- Mobile-friendly
- Fast loading (see Core Web Vitals)

### Cross-Browser Compatibility

**Test On**:
- Chrome (most users)
- Safari (iOS)
- Firefox
- Edge
- Mobile browsers (iOS Safari, Chrome Android)

**Progressive Enhancement**:
- Core content: Works everywhere
- Enhanced features: Modern browsers
- Fallbacks: For older browsers

---

## Quick Reference Checklist

### Before Launch Checklist

**Content**:
- [ ] All placeholder text replaced
- [ ] Spelling/grammar checked
- [ ] All images have alt text
- [ ] All links work (no 404s)
- [ ] Contact info correct

**Design**:
- [ ] Consistent typography (2 fonts max)
- [ ] Color contrast passes WCAG AA (4.5:1)
- [ ] Spacing consistent (8px grid)
- [ ] Responsive on mobile/tablet/desktop
- [ ] Touch targets 44px minimum

**Accessibility**:
- [ ] Keyboard navigation works
- [ ] Focus indicators visible
- [ ] Forms have labels
- [ ] HTML valid (W3C validator)
- [ ] Screen reader tested

**Performance**:
- [ ] Images optimized
- [ ] Page load < 3 seconds
- [ ] Core Web Vitals pass
- [ ] No console errors

**SEO**:
- [ ] Page titles unique
- [ ] Meta descriptions added
- [ ] XML sitemap created
- [ ] HTTPS enabled
- [ ] Google Search Console setup

**Technical**:
- [ ] Favicon added
- [ ] 404 page custom
- [ ] Forms tested (submit works)
- [ ] Analytics installed
- [ ] Privacy policy/terms added

---

## Rule Priority Levels

### P0 - Critical (Must Have)
- Accessibility (WCAG A level minimum)
- Mobile responsive
- Readable text (contrast, size)
- Working links/forms
- Fast load time (< 3s)

### P1 - Important (Should Have)
- WCAG AA compliance
- Consistent spacing
- Clear navigation
- Error prevention
- SEO basics

### P2 - Nice to Have
- WCAG AAA compliance
- Advanced animations
- Micro-interactions
- Performance optimization beyond basics

---

## Golden Rules Summary

1. **Users first**: Design for actual user needs, not your preferences
2. **Mobile-first**: Start small, expand up
3. **Accessibility**: Not optional - it's for everyone
4. **Consistency**: Use patterns, grids, spacing systems
5. **Simplicity**: When in doubt, remove it
6. **Whitespace**: Your friend, not enemy
7. **Typography**: 95% of web design
8. **Test**: With real users, real devices, real assistive technologies
9. **Performance**: Every KB matters
10. **Iterate**: Ship, measure, improve, repeat

---

**Last Updated**: 2025-11-30
**Version**: 1.0
**Status**: Production Reference

**Sources**:
- Nielsen Norman Group (Usability Heuristics)
- W3C WCAG 2.1 (Accessibility)
- Material Design (Typography System)
- Smashing Magazine (Web Design Principles)
- Web.dev (Responsive Design, Performance)
- U.S. Web Design System (Government Standards)
- Interaction Design Foundation (Whitespace)

**Companion Guides**:
- `ELEMENTOR-API-TECHNICAL-GUIDE.md` - Technical implementation
- `ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md` - Layout patterns
- `COLOR-AND-STYLE-VISION.md` - Project-specific design system
