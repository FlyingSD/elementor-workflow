# DESIGN TRACKING - Homepage Redesign

**Дата**: 2025-11-29
**Статус**: 🟡 ПЛАНИРАНЕ
**Цел**: Подобряване на дизайна следвайки UI/UX критики - БЕЗ промяна на съдържание

---

## 🚨 СТРОГИ ПРАВИЛА (MANDATORY)

### ❌ ЗАБРАНЕНО:
- ❌ **NO hardcode** - никакви hex цветове (#FABA29)
- ❌ **NO !important CSS** - никога
- ❌ **NO inline CSS** - никакъв style="" атрибут
- ❌ **NO HTML widgets** - само native Elementor widgets
- ❌ **NO custom code** - нищо в Code/Custom CSS полета
- ❌ **NO content changes** - цени, текстове остават същите

### ✅ РАЗРЕШЕНО:
- ✅ **Global Colors ONLY** - `var(--e-global-color-primary)`, `var(--e-global-color-secondary)`, etc.
- ✅ **Native Elementor widgets** - Heading, Icon Box, Button, Container, Grid, etc.
- ✅ **Container/Flexbox/Grid** - modern layouts (Container е FREE!)
- ✅ **Hover effects** - button_background_hover_color, icon_hover_color
- ✅ **Everything editable** - потребителят може да променя всичко
- ✅ **MCP tools** - create_elementor_container, add_widget_to_section, update_elementor_widget

---

## 📚 РЕСУРСИ (От Archive)

### MCP Tools (32 available - Standard Mode):
- `create_elementor_container` - Flexbox/Grid containers
- `add_widget_to_section` - Add widgets
- `update_elementor_widget` - Modify settings
- `get_elementor_data` - Get current structure
- `clear_elementor_cache_by_page` - Clear cache

### JSON Templates:
- `SSOT/archive/deprecated-docs/hero_container_structure.json` - Container example with Flexbox
- `SSOT/archive/merged-sources/JSON-GENERATION-TOOLS-GUIDE.md` - Templates
- `SSOT/archive/merged-sources/MCP-PAGE-CREATION-CHECKLIST.md` - Workflow

### Design Guidelines:
- `SSOT/REFFERENCE-BY-UI-UX-EXPERT.md` - UI/UX критики
- `SSOT/Blog/` - 17 blog posts за тон и стил
- `SSOT/archive/deprecated-docs/DESIGNER-BLOG-ANALYSIS.md` - Brand voice

---

## 🎯 ПЛАН ЗА ПРОМЕНИ (Based on UI/UX Feedback)

### **Текуща Структура (6 Sections):**
1. **Hero** - H1, Text, 2x Counter (fake), Button
2. **Benefits** - Heading + 3x Icon Box @33%
3. **Programs** - Heading + 5x Text Editor @20%
4. **Pricing CTA** - Heading + Text + Button
5. **Testimonials** - 2x Testimonial widgets
6. **Contact** - Address + CF7 form

---

## 📋 TASK LIST

### **Phase 1: Hero Section** (Критика 1.3)
**Проблем**: Fake counters (500+, 8+), малки числа, липсва контекст
**Решение**:
- [ ] **Task 1.1** - Премахни 2x Counter widgets (fake data)
- [ ] **Task 1.2** - Запази H1, Text, Button
- [ ] **Task 1.3** - Подреди в Container (Flexbox column)

**MCP Tools**: `get_elementor_data`, `update_elementor_data`, `clear_elementor_cache_by_page`

**Widget Changes**:
- **Remove**: Counter widget ID `fa7f699` (ученици 0+)
- **Remove**: Counter widget ID `3ff2063` (години опит 0+)
- **Keep**: Heading, Text Editor, Button

**Expected Result**:
```
Hero Section (Container):
  ├── Heading (H1)
  ├── Text Editor (subtitle)
  └── Button (CTA)
```

---

### **Phase 2: Benefits Section** (Критика 1.4 partial)
**Проблем**: 3 карти @33% width - cramped, липсват hover effects
**Решение**:
- [ ] **Task 2.1** - Convert Section → Container (Flexbox row)
- [ ] **Task 2.2** - Keep 3x Icon Box widgets
- [ ] **Task 2.3** - Add gap: 40px between cards
- [ ] **Task 2.4** - Add hover effects:
  - icon_hover_color: `var(--e-global-color-primary)`
  - icon_hover_animation: "grow"

**MCP Tools**: `create_elementor_container`, `update_elementor_widget`

**Widget IDs**:
- Icon Box 1: `609e1d6` (По-добра Концентрация)
- Icon Box 2: `4e5ac70` (Логическо Мислене)
- Icon Box 3: `21b9328` (Отлична Памет)

**Expected Result**:
```
Benefits Container (Flexbox row, gap 40px):
  ├── Icon Box 1 (По-добра Концентрация) + hover
  ├── Icon Box 2 (Логическо Мислене) + hover
  └── Icon Box 3 (Отлична Памет) + hover
```

---

### **Phase 3: Programs Section** (Критика 1.4)
**Проблем**: 5 карти @20% width - too narrow, визуално неравномерно
**Решение**: Bento Box Layout (2-2-1)
- [ ] **Task 3.1** - Convert от 5 columns → Grid Container
- [ ] **Task 3.2** - Row 1: Grid 2 columns (Ниво 1, Ниво 2)
- [ ] **Task 3.3** - Row 2: Grid 2 columns (Ниво 3, Ниво 4)
- [ ] **Task 3.4** - Row 3: Single centered (Ниво 5)
- [ ] **Task 3.5** - Convert Text Editor → Icon Box widgets (за consistency)
- [ ] **Task 3.6** - Add hover: translateY(-8px) + shadow

**MCP Tools**: `create_elementor_container`, `add_widget_to_section`

**Current Widget IDs**:
- Text 1: `7e2c905` (Ниво 1: Начална Група)
- Text 2: `ff698da` (Ниво 2: Средна Група)
- Text 3: `f4cde45` (Ниво 3: Напреднала Група)
- Text 4: `501c414` (Ниво 4: Майсторска Група)
- Text 5: `b0024fe` (Ниво 5: Състезателна Група)

**Expected Result**:
```
Programs Section:
  ├── Heading (Нашата 5-степенна програма)
  ├── Container Row 1 (Grid 2 cols):
  │     ├── Icon Box (Ниво 1)
  │     └── Icon Box (Ниво 2)
  ├── Container Row 2 (Grid 2 cols):
  │     ├── Icon Box (Ниво 3)
  │     └── Icon Box (Ниво 4)
  └── Container Row 3 (Single centered):
        └── Icon Box (Ниво 5)
```

---

### **Phase 4: Pricing CTA Section** (Критика 1.5)
**Проблем**: Голям жълт box, дълъг текст
**Решение**:
- [ ] **Task 4.1** - Reduce section padding (80px → 60px)
- [ ] **Task 4.2** - Make button larger (size: lg)
- [ ] **Task 4.3** - Add button hover effect
- [ ] **Task 4.4** - Convert to Container (cleaner layout)

**MCP Tools**: `update_elementor_section`, `update_elementor_widget`

**Widget IDs**:
- Heading: `7f6f3b3` (Нека поговорим за цените)
- Text: `fdd9444` (Знаем, че това е важен въпрос...)
- Button: `b06e66a` (Разгледайте нашите цени)

**Expected Result**:
```
Pricing CTA Container:
  ├── Heading (same text)
  ├── Text (same text)
  └── Button (larger, hover glow)
```

---

### **Phase 5: Button Hover Effects** (All CTAs)
**Проблем**: Липсват hover effects
**Решение**: Add hover to ALL buttons
- [ ] **Task 5.1** - Hero button: hover glow
- [ ] **Task 5.2** - Pricing button: hover glow
- [ ] **Task 5.3** - Contact button (if exists): hover glow

**Settings**:
```json
{
  "button_background_hover_color": "var(--e-global-color-secondary)",
  "hover_color": "#FFFFFF",
  "button_box_shadow_box_shadow_type": "yes",
  "button_box_shadow_box_shadow": {
    "horizontal": 0,
    "vertical": 4,
    "blur": 12,
    "spread": 0,
    "color": "rgba(250, 186, 41, 0.3)"
  }
}
```

**Button IDs**:
- Hero: `396cc0f` (ЗАПАЗИ СЕ СЕГА)
- Pricing: `b06e66a` (Разгледайте нашите цени)

---

### **Phase 6: Contact Page Layout** (Критика 6.4, 6.5)
**Страница**: Contact (ID 27)
**Проблем**: Vertical layout, червен submit button
**Решение**:
- [ ] **Task 6.1** - Convert to side-by-side (Container Flexbox row)
- [ ] **Task 6.2** - Left 40%: Contact info
- [ ] **Task 6.3** - Right 60%: Form
- [ ] **Task 6.4** - Change submit button color: red → yellow

**MCP Tools**: `get_elementor_data`, `update_elementor_data` (page 27)

---

## 📊 BUDGET TRACKING

**Widget Budget**: <30 widgets per page ✅

**Current Homepage**:
- Hero: 4 widgets → 2 widgets (remove 2 counters) ✅
- Benefits: 3 widgets → 3 widgets (same) ✅
- Programs: 5 widgets → 5 widgets (convert to Icon Box) ✅
- Pricing: 3 widgets → 3 widgets (same) ✅
- Testimonials: 2 widgets (same) ✅
- Contact: 2 widgets (same) ✅
- **TOTAL**: 19 widgets → 17 widgets ✅ (Under budget!)

---

## ✅ PRE-FLIGHT CHECKLIST

Преди всяка промяна:

- [ ] Backup current page: `python backup-before-update.py --page-id 21 --task "design-improvements"`
- [ ] Read current structure: `get_elementor_data({page_id: 21})`
- [ ] Validate Global Colors: All colors use `var(--e-global-color-*)`
- [ ] No hardcode: No hex values (#FABA29)
- [ ] No HTML widgets: Only native Elementor widgets
- [ ] Everything editable: User can modify in Elementor editor

---

## 🚀 POST-UPDATE CHECKLIST

След всяка промяна:

- [ ] Clear cache: `clear_elementor_cache_by_page({page_id: 21})`
- [ ] Test in browser: http://svetlinkielementor.local/
- [ ] Screenshot: Desktop, Tablet, Mobile
- [ ] Verify editability: Open in Elementor editor, confirm all editable
- [ ] Update this file: Mark task as complete
- [ ] Git commit: Push changes
- [ ] Update SSOT: Document changes in ACTIVE_STATE.md

---

## 📝 CHANGE LOG

### 2025-11-29 - Planning Phase
- Created DESIGN-TRACKING.md
- Analyzed UI/UX feedback
- Mapped current structure (6 sections, 19 widgets)
- Defined strict rules (no hardcode, no !important, etc.)
- Created task breakdown (6 phases)

**Status**: 🟡 Awaiting approval to start

---

## 🎯 WORKFLOW

1. **PLAN** ✅ (този файл)
2. **APPROVE** ⏳ (чакам "давай")
3. **EXECUTE** ⏳ (правя промените)
4. **TEST** ⏳ (screenshots, verification)
5. **GIT PUSH** ⏳ (commit changes)
6. **UPDATE DOCS** ⏳ (SSOT, .claude/)
7. **DONE** ⏳

---

**Next Step**: Чакам потвърждение "давай" за да започна Phase 1 🚀
