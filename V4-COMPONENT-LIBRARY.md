# V4 Component Library - Reusable Patterns

**Created**: 2025-11-30
**Purpose**: Reusable Elementor component specs for ALL pages (Homepage, About, Programs, Contact, FAQ, Blog)
**Version**: V4 Design System
**Reference**: COLOR-AND-STYLE-VISION.md, design-mockup-v4.html

---

## 🎨 GLOBAL DESIGN TOKENS

### Colors (Use these exact values everywhere)
```
Primary Yellow:     var(--e-global-color-primary)   = #FABA29
Secondary Teal:     var(--e-global-color-secondary) = #46b19d
Accent Coral:       var(--e-global-color-accent)    = #FF8C7A
Text Dark Teal:     var(--e-global-color-text)      = #1d3234
White:              #FFFFFF
Warm Cream:         #FEFCF5
Light Yellow:       #fff4d9
Warm Yellow:        #ffe8b3
Cream Yellow:       #fff9e6
```

### Typography
```
H1: clamp(2.25rem, 5vw, 3.25rem) - Bold 700 - Line-height 1.15
H2: clamp(1.85rem, 4vw, 2.5rem) - Bold 700 - Line-height 1.3
H3: clamp(1.4rem, 3vw, 1.65rem) - Bold 700 - Line-height 1.3
Body: clamp(1rem, 2vw, 1.05rem) - Regular 400 - Line-height 1.75
```

### Spacing Standards
```
Section Padding (Desktop): 90px top/bottom, 20px left/right
Section Padding (Mobile): 70px top/bottom, 20px left/right
Card Padding: 45px vertical, 35px horizontal
Button Padding: 18px vertical, 40px horizontal
Card Gap: 40px
```

### Border Radius
```
Buttons: 12px
Cards: 20px
Icons: 50% (perfect circle)
Dividers: 2px
```

### Shadows
```
Card Shadow: 0 10px 35px rgba(0, 0, 0, 0.1)
Card Hover Shadow: 0 20px 50px rgba(250, 186, 41, 0.2)
Button Shadow: 0 6px 20px rgba(250, 186, 41, 0.35)
Icon Shadow: 0 6px 20px rgba(250, 186, 41, 0.3)
```

### Transitions
```
Standard: all 0.35s ease
Button: all 0.35s cubic-bezier(0.4, 0, 0.2, 1)
Hover Lift: transform 0.35s ease
```

---

## 🧩 REUSABLE COMPONENTS

---

## 1️⃣ **PRIMARY BUTTON** (Main CTA)

**Widget**: Button
**Use Cases**: "Безплатен пробен урок", "Запази се сега", "Свържи се с нас"

**Settings JSON Pattern**:
```json
{
  "widgetType": "button",
  "settings": {
    "text": "Безплатен пробен урок",
    "link": {"url": "#contact"},
    "align": "center",
    "button_type": "default",
    "button_text_color": "#FFFFFF",
    "background_color": "var(--e-global-color-primary)",
    "border_radius": {"unit": "px", "top": 12, "right": 12, "bottom": 12, "left": 12},
    "button_padding": {"unit": "px", "top": 18, "right": 40, "bottom": 18, "left": 40},
    "button_box_shadow": {
      "horizontal": 0,
      "vertical": 6,
      "blur": 20,
      "spread": 0,
      "color": "rgba(250, 186, 41, 0.35)"
    },
    "hover_color": "#FFFFFF",
    "button_background_hover_color": "var(--e-global-color-secondary)",
    "hover_animation": "grow"
  }
}
```

**Visual Recipe**:
1. Add Button widget
2. **Content Tab**:
   - Text: "Безплатен пробен урок"
   - Link: #contact (or page URL)
3. **Style Tab**:
   - Text Color: White (#FFFFFF)
   - Background: Primary (Yellow #FABA29)
   - Border Radius: 12px all sides
   - Padding: 18px top/bottom, 40px left/right
   - Box Shadow: 0px 6px 20px, spread 0, color rgba(250,186,41,0.35)
4. **Hover**:
   - Background: Secondary (Teal #46b19d)
   - Animation: Grow

---

## 2️⃣ **SECONDARY BUTTON** (Supporting CTA)

**Widget**: Button
**Use Cases**: "Вижте програмите", "Прочети повече", "Разгледай"

**Settings JSON Pattern**:
```json
{
  "widgetType": "button",
  "settings": {
    "text": "Вижте програмите",
    "link": {"url": "/programs/"},
    "button_text_color": "#FFFFFF",
    "background_color": "var(--e-global-color-accent)",
    "border_radius": {"unit": "px", "top": 12, "right": 12, "bottom": 12, "left": 12},
    "button_padding": {"unit": "px", "top": 18, "right": 40, "bottom": 18, "left": 40},
    "button_box_shadow": {
      "horizontal": 0,
      "vertical": 6,
      "blur": 20,
      "spread": 0,
      "color": "rgba(255, 140, 122, 0.35)"
    },
    "button_background_hover_color": "var(--e-global-color-secondary)"
  }
}
```

**Visual Recipe**: Same as Primary, but:
- Background: Accent (Coral #FF8C7A)
- Box Shadow color: rgba(255,140,122,0.35)

---

## 3️⃣ **ICON BOX CARD** (Standard Card with Icon)

**Widget**: Icon Box
**Use Cases**: Benefits cards, Features, Services

**Settings JSON Pattern**:
```json
{
  "widgetType": "icon-box",
  "settings": {
    "icon": {"value": "fas fa-brain", "library": "fa-solid"},
    "title_text": "По-добра концентрация",
    "description_text": "Вашето дете ще научи да се фокусира върху задачи за по-дълго време.",
    "position": "top",
    "title_color": "var(--e-global-color-text)",
    "description_color": "#5a6c6d",

    "icon_primary_color": "#FFFFFF",
    "icon_size": {"unit": "px", "size": 38},
    "icon_space": {"unit": "px", "size": 22},
    "icon_padding": {"unit": "px", "top": 18, "right": 18, "bottom": 18, "left": 18},
    "icon_border_radius": {"unit": "%", "top": 50, "right": 50, "bottom": 50, "left": 50},
    "icon_background_color": "var(--e-global-color-primary)",

    "border_border": "solid",
    "border_width": {"unit": "px", "top": 5, "right": 0, "bottom": 0, "left": 0},
    "border_color": "var(--e-global-color-primary)",
    "border_radius": {"unit": "px", "top": 20, "right": 20, "bottom": 20, "left": 20},

    "background_color": "#FFFFFF",
    "padding": {"unit": "px", "top": 45, "right": 35, "bottom": 45, "left": 35},

    "box_shadow": {
      "horizontal": 0,
      "vertical": 10,
      "blur": 35,
      "spread": 0,
      "color": "rgba(0, 0, 0, 0.1)"
    }
  }
}
```

**Visual Recipe**:
1. Add Icon Box widget
2. **Content Tab**:
   - Icon: Choose from library (or use emoji)
   - Title: Card title
   - Description: Card text
   - Position: Top (icon above text)
3. **Style Tab → Icon**:
   - Primary Color: White (#FFFFFF)
   - Size: 38px
   - Padding: 18px all sides
   - Background: Gradient (Yellow #FABA29 → #f5a500)
   - Border Radius: 50% (circle)
   - Space Below: 22px
4. **Style Tab → Content**:
   - Title Color: Text (Dark Teal #1d3234)
   - Description Color: #5a6c6d
   - Alignment: Center
5. **Advanced Tab → Border**:
   - Border Type: Solid
   - Width: 5px top, 0 others
   - Color: Varies (Yellow, Gradient, or Teal)
   - Border Radius: 20px
6. **Advanced Tab → Background**:
   - Background: White (#FFFFFF)
   - Padding: 45px top/bottom, 35px left/right
7. **Advanced Tab → Box Shadow**:
   - Type: Drop Shadow
   - Shadow: 0px 10px 35px, color rgba(0,0,0,0.1)

**Color Variations** (Top Border):
- Card 1: Yellow (#FABA29)
- Card 2: Gradient (linear-gradient(90deg, #FABA29, #FF8C7A))
- Card 3: Teal (#46b19d)

---

## 4️⃣ **CARD WITH BUTTON** (Programs Teaser Style)

**Widgets**: Icon Box + Button (inside)
**Use Cases**: Program teasers, Service cards, CTA cards

**Structure**:
```
Icon Box Widget
├─ Icon: 📚 (emoji or icon)
├─ Title: "5 нива на обучение"
├─ Description: Brief text
└─ Button: "Прочети повече" (embedded in description area)
```

**Visual Recipe**:
1. Create Icon Box (same as Component #3)
2. In Description field, add button shortcode OR:
3. Add Button widget below Icon Box in same column
4. Style button as Secondary Button (Component #2)

**Alternative**: Use **Column** with multiple widgets:
```
Column (with card styling)
├─ Heading widget (emoji + title)
├─ Text Editor widget (description)
└─ Button widget (CTA)
```

---

## 5️⃣ **SECTION TITLE WITH UNDERLINE**

**Widget**: Heading
**Use Cases**: All section titles

**Settings JSON Pattern**:
```json
{
  "widgetType": "heading",
  "settings": {
    "title": "Предимства на нашата програма",
    "header_size": "h2",
    "align": "center",
    "title_color": "var(--e-global-color-text)",
    "typography_font_size": {"unit": "rem", "size": 2.5},
    "typography_font_weight": "700",
    "typography_line_height": {"unit": "em", "size": 1.3}
  }
}
```

**Visual Recipe**:
1. Add Heading widget
2. **Content Tab**:
   - Title: Section name
   - HTML Tag: H2
   - Alignment: Center
3. **Style Tab**:
   - Text Color: Text (Dark Teal #1d3234)
   - Typography: 2.5rem (clamp in responsive), Bold 700, Line-height 1.3
4. **Below heading**: Add Divider widget
   - Width: 80px
   - Height: 4px
   - Color: Gradient (Yellow → Coral) or Yellow
   - Alignment: Center
   - Margin Top: 12px

---

## 6️⃣ **GRADIENT BACKGROUND SECTION**

**Element**: Section
**Use Cases**: Hero, alternate sections

**Settings JSON Pattern** (Yellow Gradient):
```json
{
  "elType": "section",
  "settings": {
    "background_background": "gradient",
    "background_color": "#FEFCF5",
    "background_color_stop": {"unit": "%", "size": 0},
    "background_color_b": "#fff4d9",
    "background_color_b_stop": {"unit": "%", "size": 40},
    "background_gradient_type": "linear",
    "background_gradient_angle": {"unit": "deg", "size": 120},
    "padding": {"unit": "px", "top": 100, "right": 20, "bottom": 100, "left": 20}
  }
}
```

**Visual Recipe**:
1. Edit Section → Style Tab
2. **Background**:
   - Type: Gradient
   - Color 1: #FEFCF5 at 0%
   - Color 2: #fff4d9 at 40%
   - Color 3 (optional): #ffe8b3 at 100%
   - Type: Linear
   - Angle: 120deg
3. **Padding**:
   - Desktop: 100px top/bottom
   - Mobile: 70px top/bottom

**Background Options**:
- Hero: `linear-gradient(120deg, #FEFCF5 0%, #fff4d9 40%, #ffe8b3 100%)`
- Benefits: `linear-gradient(135deg, #FEFCF5 0%, #fff9e6 100%)`
- White Section: Solid #FFFFFF

---

## 7️⃣ **IMAGE CAROUSEL** (Blog/Gallery)

**Widget**: Image Carousel
**Use Cases**: Blog previews, Galleries, Testimonials

**Settings JSON Pattern**:
```json
{
  "widgetType": "image-carousel",
  "settings": {
    "carousel": [
      {"id": 123, "url": "image1.jpg"},
      {"id": 124, "url": "image2.jpg"},
      {"id": 125, "url": "image3.jpg"}
    ],
    "slides_to_show": "1",
    "slides_to_scroll": "1",
    "navigation": "arrows",
    "arrows": "yes",
    "dots": "no",
    "autoplay": "yes",
    "autoplay_speed": 5000,
    "infinite": "yes",
    "speed": 500
  }
}
```

**Visual Recipe**:
1. Add Image Carousel widget
2. **Content Tab**:
   - Add images (upload or media library)
   - Slides to Show: 1
   - Slides to Scroll: 1
3. **Navigation**:
   - Arrows: Yes
   - Dots: No (or Yes if preferred)
   - Infinite Loop: Yes
4. **Autoplay**:
   - Autoplay: Yes
   - Speed: 5000ms (5 seconds)
5. **Style Tab → Arrows**:
   - Color: Primary (Yellow #FABA29)
   - Size: 55px
   - Background: Circular with shadow
   - Hover: Secondary (Teal #46b19d)

---

## 8️⃣ **RESPONSIVE GRID** (3-2-1 Pattern)

**Element**: Section with Columns
**Use Cases**: Benefits, Features, Team, Programs

**Structure**:
```
Section
└─ Column (repeat 3x)
   └─ Widget (Icon Box, Image, etc.)
```

**Settings**:
```json
{
  "section": {
    "layout": "boxed",
    "content_width": {"unit": "px", "size": 1200},
    "column_gap": {"unit": "px", "size": 40}
  },
  "columns": [
    {"_column_size": 33, "_inline_size": 33},
    {"_column_size": 33, "_inline_size": 33},
    {"_column_size": 33, "_inline_size": 33}
  ]
}
```

**Visual Recipe**:
1. Add Section
2. Set columns: 3 columns (33% each)
3. **Desktop**: 3 columns
4. **Tablet**: 2 columns (50% each) - set in responsive mode
5. **Mobile**: 1 column (100%) - set in responsive mode
6. Gap: 40px

**Responsive Settings**:
- Desktop: `grid-template-columns: repeat(3, 1fr)`
- Tablet: `grid-template-columns: repeat(2, 1fr)`
- Mobile: `grid-template-columns: 1fr`

---

## 9️⃣ **TWO-COLUMN HERO LAYOUT**

**Element**: Section with 2 Columns
**Use Cases**: Hero sections, About intro

**Structure**:
```
Section (Gradient Background)
├─ Column 1 (60% - Text Content)
│  ├─ Heading widget
│  ├─ Text Editor widget
│  └─ 2x Button widgets
└─ Column 2 (40% - Image)
   └─ Image widget (Mascot)
```

**Settings**:
```json
{
  "section": {
    "background": "gradient (see Component #6)",
    "padding": {"top": 100, "bottom": 100},
    "min_height": {"unit": "px", "size": 650}
  },
  "columns": [
    {"_column_size": 60},
    {"_column_size": 40}
  ]
}
```

**Visual Recipe**:
1. Add Section with gradient background
2. Add 2 columns: 60% / 40%
3. **Left Column**:
   - Vertical Align: Middle
   - Padding Right: 40px
4. **Right Column**:
   - Content Align: Center
   - Image: Max-width 520px, drop-shadow filter
5. **Responsive (Mobile)**:
   - Stack columns (100% each)
   - Text centered
   - Image centered, smaller (380px)

---

## 🔟 **ACCORDION/FAQ ITEM**

**Widget**: Accordion
**Use Cases**: FAQ page, Collapsible content

**Settings JSON Pattern**:
```json
{
  "widgetType": "accordion",
  "settings": {
    "tabs": [
      {
        "tab_title": "Колко струва обучението?",
        "tab_content": "Месечната такса е 120 лв за 4 урока по 90 минути."
      }
    ],
    "icon": {"value": "fas fa-plus", "library": "fa-solid"},
    "icon_active": {"value": "fas fa-minus", "library": "fa-solid"},
    "title_color": "var(--e-global-color-text)",
    "title_background": "var(--e-global-color-accent)",
    "border_border": "solid",
    "border_width": {"unit": "px", "top": 0, "right": 0, "bottom": 1, "left": 0},
    "border_color": "#e0e0e0"
  }
}
```

**Visual Recipe**:
1. Add Accordion widget
2. **Content Tab**:
   - Add items (title + content for each Q&A)
   - Icon: Plus (+) when closed
   - Active Icon: Minus (−) when open
3. **Style Tab**:
   - Title Color: Dark Teal (#1d3234)
   - Title Background: Light cream or white
   - Content Color: #5a6c6d
   - Border: 1px bottom, light gray
   - Padding: 20px

---

## 📋 **PAGE TEMPLATES**

---

### **HOMEPAGE STRUCTURE** (4 Sections)

```
Section 1: Hero (Gradient Yellow)
├─ Column 1 (Text)
│  ├─ Heading (H1 with title)
│  ├─ Text Editor (subtitle)
│  └─ 2x Buttons (Primary + Secondary)
└─ Column 2 (Image - Zhara mascot)

Section 2: Blog Carousel (White)
├─ Heading (section title)
├─ Divider (gradient underline)
├─ Image Carousel (blog previews)
└─ Navigation arrows

Section 3: Benefits (Gradient Cream)
├─ Heading (section title)
├─ Divider (gradient underline)
└─ 3x Icon Box Cards (3-2-1 responsive grid)

Section 4: Programs Teaser (White)
├─ Heading (section title)
├─ Divider (gradient underline)
└─ 3x Icon Box Cards with Buttons (3-2-1 grid)
   ├─ Card 1: Levels overview
   ├─ Card 2: Promotions
   └─ Card 3: FAQ link
```

---

### **ABOUT PAGE STRUCTURE** (Suggested)

```
Section 1: Hero (Gradient)
├─ Heading (About Us)
├─ Text (Mission statement)
└─ Image (Team photo or mascot)

Section 2: Mission (White)
└─ Text + Icon Box

Section 3: Values (Gradient Cream)
└─ 3x Icon Box Cards

Section 4: Team (White)
└─ Image widgets or Icon Box with photos

Section 5: CTA (Gradient Yellow)
└─ Heading + Button
```

---

### **PROGRAMS PAGE STRUCTURE** (Suggested)

```
Section 1: Hero (Gradient)
├─ Heading (Нашите програми)
└─ Text (Overview)

Section 2: 5 Levels (Alternating backgrounds)
└─ 5x Icon Box Cards (full descriptions)

Section 3: Pricing (White)
└─ Icon Box with pricing info

Section 4: Promotions (Gradient Cream)
└─ Icon Box with offers

Section 5: CTA (Gradient Yellow)
└─ Button (Запази се сега)
```

---

### **CONTACT PAGE STRUCTURE** (Suggested)

```
Section 1: Hero (Gradient)
├─ Heading (Свържи се с нас)
└─ Text

Section 2: Contact Info + Form (White)
├─ Column 1 (40% - Info)
│  └─ Icon Box with address, phone, email
└─ Column 2 (60% - Form + Map)
   ├─ Contact Form 7 shortcode
   └─ Google Maps widget
```

---

### **FAQ PAGE STRUCTURE** (Suggested)

```
Section 1: Hero (Gradient)
├─ Heading (Често задавани въпроси)
└─ Text

Section 2: FAQ List (White)
└─ Accordion widget (10+ Q&A items)

Section 3: CTA (Gradient Cream)
├─ Text ("Не намерихте отговор?")
└─ Button ("Свържи се с нас")
```

---

### **BLOG PAGE STRUCTURE** (Suggested)

```
Section 1: Hero (Gradient)
├─ Heading (Нашият блог)
└─ Text

Section 2: Blog Posts Grid (White)
└─ 3x Image Box widgets (manual posts)
   OR use Posts widget if available

Section 3: CTA (Gradient Cream)
└─ Newsletter signup or CTA
```

---

## ⚡ QUICK REFERENCE CHEAT SHEET

### **Colors by Use Case:**
- **Primary CTA**: Yellow (#FABA29)
- **Secondary CTA**: Coral (#FF8C7A)
- **Hover State**: Teal (#46b19d)
- **All Text**: Dark Teal (#1d3234)
- **Card Backgrounds**: White (#FFFFFF)
- **Section Backgrounds**: Alternate White / Cream gradients

### **Shadows by Element:**
- **Cards**: 0 10px 35px rgba(0,0,0,0.1)
- **Buttons**: 0 6px 20px rgba(250,186,41,0.35)
- **Icons**: 0 6px 20px rgba(250,186,41,0.3)
- **Hover**: Increase blur by 15px, add yellow tint

### **Border Radius:**
- **Buttons**: 12px
- **Cards**: 20px
- **Icons**: 50% (circle)

### **Padding Standards:**
- **Sections**: 90px (desktop), 70px (mobile)
- **Cards**: 45px vertical, 35px horizontal
- **Buttons**: 18px vertical, 40px horizontal

---

## 🔧 WIDGET PROPERTY NAMES (Important!)

**These are NOT intuitive** - memorize these:

```javascript
// Heading Widget
{
  "title_color": "...",          // NOT "color"!
  "typography_font_size": {...}
}

// Text Editor Widget
{
  "text_color": "...",            // NOT "color"!
}

// Button Widget
{
  "button_text_color": "...",     // NOT "text_color"!
  "background_color": "...",      // Button background
  "button_background_hover_color": "..." // Hover
}

// Icon Box Widget
{
  "title_color": "...",           // Title text color
  "description_color": "...",     // Description color
  "icon_primary_color": "...",    // Icon color
  "icon_background_color": "..."  // Icon circle background
}

// Image Widget
{
  "image": {"url": "...", "id": 123}
}
```

---

## 📝 USAGE INSTRUCTIONS

### **For Homepage (Now):**
1. Use Components #1-9
2. Follow Homepage Structure exactly
3. Reference COLOR-AND-STYLE-VISION.md for exact values

### **For Other Pages (Later):**
1. Pick relevant components from this library
2. Follow suggested page structures
3. Copy/paste settings from components
4. Adjust content (text, images) as needed

### **Customization Rules:**
- ✅ Change text content freely
- ✅ Change images (keep sizes)
- ✅ Adjust spacing slightly (±10px)
- ❌ Don't change colors (use Global Colors)
- ❌ Don't change border radius standards
- ❌ Don't change shadow values

---

## 🎯 WORKFLOW FOR NEW PAGES

1. **Read this document** (choose components)
2. **Read page structure** (from Page Templates section)
3. **Build section by section** (copy component settings)
4. **Test responsive** (desktop, tablet, mobile)
5. **Verify colors** (all using Global Colors)
6. **Check spacing** (matches standards)

---

**Status**: ✅ READY FOR USE
**Pages to Build**: Homepage (now), About, Programs, Contact, FAQ, Blog (later)
**All settings tested**: Yes (based on V4 mockup)

---

**Version**: 1.0
**Last Updated**: 2025-11-30
**Maintained By**: Claude Code Main Coordinator
