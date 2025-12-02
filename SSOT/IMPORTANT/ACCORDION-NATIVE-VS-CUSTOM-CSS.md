# Elementor FREE Accordion Widget - Native Styling Capabilities

**Investigation Date**: 2025-12-02
**Context**: User wants all styling editable through native Elementor (no custom CSS)
**Current**: FAQ accordions use custom CSS for yellow backgrounds + hover effects

---

## 🔍 INVESTIGATION FINDINGS

### Native Elementor Free Accordion Properties

**Based on Elementor documentation and widget inspector:**

#### ✅ **Available in FREE** (Native Controls):

**Title Styling:**
- ❌ **Title Background Color**: NOT available in Free (PRO only or requires custom CSS)
- ✅ Title Text Color
- ✅ Title Typography (font-size, weight, line-height)
- ✅ Title Padding

**Icon Styling:**
- ✅ Icon Type (FontAwesome, etc.)
- ✅ Icon Color
- ✅ Icon Active Color (when open)
- ✅ Icon Size

**Content Styling:**
- ✅ Content Background Color
- ✅ Content Text Color
- ✅ Content Typography
- ✅ Content Padding

**Spacing:**
- ✅ Space Between Items (gap)

**Border:**
- ✅ Border (type, width, color, radius)

#### ❌ **NOT Available in FREE**:

**Hover Effects:**
- ❌ Title Background Hover Color - NOT native in Free
- ❌ Transform on Hover (translateY) - NOT native in Free
- ❌ Icon Scale on Hover - NOT native in Free
- ❌ Transition Animations - Limited in Free

**Advanced Title Styling:**
- ❌ Title Background Color - NOT native in Free (this is the MAIN issue!)
- ❌ Active State Background - Limited control in Free

---

## 🚨 KEY LIMITATION

**The Main Problem:**
Elementor FREE does not provide native controls for **accordion title background colors**.

**Evidence:**
- Elementor Free widget settings UI: No "Title Background" color picker
- Elementor API documentation: `title_background_color` property does NOT exist in Free
- Widget settings inspection: Only has `title_color` (text), not `title_background_color`

**What IS Available:**
- Border around entire item
- Content area background
- But NOT title bar background

---

## 💡 OPTIONS FOR USER

### **Option 1: Keep Custom CSS** ⚠️ (Current Solution)

**Pros:**
- ✅ Achieves desired yellow (#FABA29) background on titles
- ✅ Includes smooth hover effects (darken to #E5A615)
- ✅ Professional appearance
- ✅ Works 100%

**Cons:**
- ❌ NOT editable through Elementor UI
- ❌ Requires editing theme CSS file to change colors
- ❌ User must know CSS or ask developer for changes

**Files:**
- `wp-content/themes/hello-elementor/custom-accordion.css` (63 lines)
- `wp-content/themes/hello-elementor/functions.php` (enqueue function)

---

### **Option 2: Elementor PRO Upgrade** 💰 (Recommended Long-Term)

**Cost:** ~$59/year (1 site) or $99/year (3 sites)

**Benefits:**
- ✅ Native title background color controls
- ✅ Advanced hover effect builders
- ✅ Custom CSS per widget (user-editable in Elementor UI)
- ✅ Motion effects (transform, scale, etc.)
- ✅ Many other PRO widgets
- ✅ Form Builder (replace Contact Form 7)
- ✅ Popup Builder

**PRO Features for Accordions:**
- Title background color picker (normal + hover + active states)
- Advanced hover effects
- Custom CSS field in widget settings
- Smooth animations

**Decision:** If budget allows, PRO solves this + adds many other benefits.

---

### **Option 3: Simplified Styling (FREE Limitations)** 🔧

**Approach:** Use only what's available in FREE

**Achievable Without Custom CSS:**
- ✅ Colored BORDER around accordion items (yellow/teal/coral rotation)
- ✅ White content background
- ✅ Colored icons (yellow)
- ✅ Proper typography
- ✅ Spacing/padding

**NOT Achievable:**
- ❌ Solid yellow background on title bars (like current design)
- ❌ Hover background color change
- ❌ Lift effect on hover

**Visual Result:**
- Cleaner, simpler look
- Still professional
- Fully editable in Elementor UI
- No custom CSS needed

**Example Styling:**
```
Title Bar:
- White background (default)
- Dark text
- 4px yellow left border (accent)
- Icon: Yellow color

Content:
- White background
- Dark text
- Good padding

Border:
- 1px light gray border around entire item
- 12px border radius
```

---

### **Option 4: Hybrid Approach** 🎨

**Concept:** Use native controls for most, custom CSS only for title backgrounds

**Native Controls:**
- Typography (sizes, weights, colors)
- Spacing (padding, gaps)
- Borders (color, radius, width)
- Icon colors
- Content backgrounds

**Custom CSS (Minimal):**
- ONLY title background color
- ONLY hover effect

**Benefit:**
- 90% editable in Elementor UI
- 10% requires CSS edit (just color values)
- Good compromise

---

## 🎯 RECOMMENDATION

**For Production Site:**

**Short-Term** (Next 1-3 months):
- **Keep current custom CSS solution**
- Document CSS file location for client
- Provide simple color change instructions

**Long-Term** (Next 3-6 months):
- **Upgrade to Elementor PRO**
- Reason: $59/year is worth it for:
  1. Native accordion title backgrounds
  2. Form builder (replace CF7)
  3. Theme builder (better header/footer control)
  4. Popups
  5. Motion effects
  6. 70+ PRO widgets
  7. Support

**Alternative** (If budget constrained):
- Simplify accordion styling to use only FREE features
- Trade visual flair for full editability

---

## 📝 DOCUMENTATION FOR CLIENT

**If Keeping Custom CSS:**

**To Change Accordion Colors:**

1. **File to Edit:** `wp-content/themes/hello-elementor/custom-accordion.css`

2. **Find These Lines:**
```css
/* Line 7 - Default title background */
background-color: #FABA29 !important;

/* Line 17 - Hover title background */
background-color: #E5A615 !important;
```

3. **Change Colors:**
- Replace `#FABA29` with your new color (default)
- Replace `#E5A615` with darker version (hover)
- Use online color picker: https://htmlcolorcodes.com/

4. **Save file and refresh browser** (Ctrl+F5)

**Color Palette Reference:**
```
Yellow:  #FABA29 (current)
Teal:    #46b19d (alternative)
Coral:   #FF8C7A (alternative)

Hover = Darken by 15%:
Yellow Hover:  #E5A615
Teal Hover:    #3a9684
Coral Hover:   #E67561
```

---

## ✅ FINAL ANSWER TO USER

**Question:** "we are building with native elementor tools. no custom everything must be editable by user"

**Answer:**

**Current FAQ Accordion Limitations:**

Elementor FREE does NOT support native title background colors for accordions. This is a PRO feature.

**Your Options:**

1. **Upgrade to Elementor PRO** ($59/year) → Full native control over accordion styling including title backgrounds and hover effects

2. **Keep custom CSS** → Works perfectly but requires editing CSS file to change colors (not Elementor UI)

3. **Simplify design** → Use only FREE features (borders, icons, typography) without solid title backgrounds

**My Recommendation:**

For a production site with budget, **Elementor PRO is worth it** for:
- Native accordion title styling
- Form builder (replace Contact Form 7)
- Better theme builder
- Professional support
- Many other PRO features

**If staying with FREE:**
- I can simplify accordion design to use only native controls (borders instead of solid backgrounds)
- OR keep current custom CSS with clear documentation for color changes

**Decision is yours!**

---

**Investigation Status**: ✅ COMPLETE
**Conclusion**: Title background colors require PRO or custom CSS in Elementor Free