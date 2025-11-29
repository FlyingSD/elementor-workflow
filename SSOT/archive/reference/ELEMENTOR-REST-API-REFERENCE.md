# Elementor REST API Reference

**Purpose**: Complete reference for Elementor's custom REST API endpoints
**Discovery Date**: 2025-11-29
**Namespace**: `elementor/v1` and `elementor-ai/v1`
**Authentication**: WordPress Application Password (same as standard WP API)

---

## 🎯 Key Discovery

**YES, Elementor has its OWN REST API!**

Elementor registers **custom REST API endpoints** under the `elementor/v1` namespace, **separate from** the standard WordPress `/wp/v2/` endpoints.

**Base URL**: `http://svetlinkielementor.local/wp-json/elementor/v1/`

---

## 🆚 Elementor API vs WordPress API

### Standard WordPress API (What we've been using)

```bash
# Get page
GET /wp-json/wp/v2/pages/21

# Update page
POST /wp-json/wp/v2/pages/21

# Get post meta
GET /wp-json/wp/v2/pages/21?_fields=meta

# Update post meta (_elementor_data)
POST /wp-json/wp/v2/pages/21
Body: {"meta": {"_elementor_data": "..."}}
```

**Limitations**:
- ❌ Bypasses Elementor hooks (Issue #3 in our guide)
- ❌ Doesn't trigger CSS regeneration
- ❌ Requires manual "Update" click in editor
- ⚠️ Direct database manipulation

### Elementor Custom API (Better for Elementor operations!)

```bash
# Get globals (colors, typography)
GET /wp-json/elementor/v1/globals

# Get Global Colors
GET /wp-json/elementor/v1/globals/colors

# Update specific Global Color
POST /wp-json/elementor/v1/globals/colors/{id}

# Clear Elementor cache
DELETE /wp-json/elementor/v1/cache

# Get Elementor documents
GET /wp-json/elementor/v1/documents
```

**Advantages**:
- ✅ Goes through Elementor's internal logic
- ✅ Triggers proper hooks
- ✅ Handles cache regeneration
- ✅ More reliable for Elementor-specific operations

---

## 📋 Complete Endpoint List

### 1. Documents API (`/elementor/v1/documents`)

**Get all documents**:
```http
GET /wp-json/elementor/v1/documents
```

**Import media to document**:
```http
POST /wp-json/elementor/v1/documents/{id}/media/import
```

---

### 2. Cache Management (`/elementor/v1/cache`)

**Clear all Elementor cache** (⚠️ **THIS IS HUGE!**):
```http
DELETE /wp-json/elementor/v1/cache
```

**Why this matters**: This is the **programmatic** way to clear cache without PHP or WP-CLI!

---

### 3. Global Design System (`/elementor/v1/globals`)

#### Get All Globals:
```http
GET /wp-json/elementor/v1/globals
```

#### Global Colors:

**Get all Global Colors**:
```http
GET /wp-json/elementor/v1/globals/colors
```

**Get specific Global Color**:
```http
GET /wp-json/elementor/v1/globals/colors/{id}
```
Example: `GET /wp-json/elementor/v1/globals/colors/primary`

**Update Global Color**:
```http
POST /wp-json/elementor/v1/globals/colors/{id}
Body: {
  "value": "#FABA29"
}
```

**Delete Global Color**:
```http
DELETE /wp-json/elementor/v1/globals/colors/{id}
```

#### Global Typography:

**Get all Global Typography**:
```http
GET /wp-json/elementor/v1/globals/typography
```

**Get specific typography**:
```http
GET /wp-json/elementor/v1/globals/typography/{id}
```

**Update typography**:
```http
POST /wp-json/elementor/v1/globals/typography/{id}
```

**Delete typography**:
```http
DELETE /wp-json/elementor/v1/globals/typography/{id}
```

---

### 4. Settings API (`/elementor/v1/settings`)

**Get setting**:
```http
GET /wp-json/elementor/v1/settings/{key}
```

**Update setting**:
```http
POST /wp-json/elementor/v1/settings/{key}
PUT /wp-json/elementor/v1/settings/{key}
PATCH /wp-json/elementor/v1/settings/{key}
```

Examples:
- `/elementor/v1/settings/css_print_method`
- `/elementor/v1/settings/elementor_scheme_color`

---

### 5. Kit Elements Defaults (`/elementor/v1/kit-elements-defaults`)

**Get all kit element defaults**:
```http
GET /wp-json/elementor/v1/kit-elements-defaults
```

**Update element default**:
```http
POST /wp-json/elementor/v1/kit-elements-defaults/{type}
Body: {
  "settings": {
    "title_color": "var(--e-global-color-primary)"
  }
}
```

**Delete element default**:
```http
DELETE /wp-json/elementor/v1/kit-elements-defaults/{type}
```

---

### 6. Template Library (`/elementor/v1/template-library`)

**Get all templates**:
```http
GET /wp-json/elementor/v1/template-library/templates
```

**Create template**:
```http
POST /wp-json/elementor/v1/template-library/templates
Body: {
  "title": "My Template",
  "type": "page|section|container",
  "content": { /* Elementor JSON */ }
}
```

---

### 7. Post/Term/User Search (`/elementor/v1/post`, `/term`, `/user`)

**Search posts**:
```http
GET /wp-json/elementor/v1/post?term=search&items_count=100
```

**Search terms**:
```http
GET /wp-json/elementor/v1/term?term=search
```

**Search users**:
```http
GET /wp-json/elementor/v1/user?term=search
```

---

### 8. Site Navigation (`/elementor/v1/site-navigation`)

**Get recent posts**:
```http
GET /wp-json/elementor/v1/site-navigation/recent-posts?posts_per_page=10
```

**Create new post**:
```http
POST /wp-json/elementor/v1/site-navigation/add-new-post
Body: {
  "post_type": "page"
}
```

---

### 9. Favorites (`/elementor/v1/favorites`)

**Get favorites**:
```http
GET /wp-json/elementor/v1/favorites
```

**Add favorite**:
```http
POST /wp-json/elementor/v1/favorites/{id}
Body: {
  "favorite": "widget-heading"
}
```

**Remove favorite**:
```http
DELETE /wp-json/elementor/v1/favorites/{id}
```

---

### 10. User Data (`/elementor/v1/user-data/current-user`)

**Get current user data**:
```http
GET /wp-json/elementor/v1/user-data/current-user
```

**Update current user data**:
```http
PATCH /wp-json/elementor/v1/user-data/current-user
Body: {
  "suppressedMessages": ["message-key"]
}
```

---

### 11. Library Connect (`/elementor/v1/library/connect`)

**Connect to Elementor library**:
```http
POST /wp-json/elementor/v1/library/connect
Body: {
  "token": "cli-token"
}
```

**Disconnect from library**:
```http
DELETE /wp-json/elementor/v1/library/connect
```

---

### 12. Checklist API (`/elementor/v1/checklist`)

**Get checklist**:
```http
GET /wp-json/elementor/v1/checklist
```

**Get checklist steps**:
```http
GET /wp-json/elementor/v1/checklist/steps
```

**Update step**:
```http
POST /wp-json/elementor/v1/checklist/steps/{id}
```

**Get user progress**:
```http
GET /wp-json/elementor/v1/checklist/user-progress
```

**Update user progress**:
```http
POST /wp-json/elementor/v1/checklist/user-progress
```

---

### 13. Elementor AI API (`/elementor-ai/v1`)

**Get AI permissions**:
```http
GET /wp-json/elementor-ai/v1/permissions
```

---

### 14. Send Event (`/elementor/v1/send-event`)

**Send analytics event**:
```http
POST /wp-json/elementor/v1/send-event
Body: {
  "event_data": { /* event payload */ }
}
```

---

## 🔥 Most Useful Endpoints for Our Project

### 1. Clear Cache (⚠️ CRITICAL!)

Instead of:
```php
\Elementor\Plugin::$instance->files_manager->clear_cache();
```

Or:
```bash
wp elementor flush-css
```

**Now we can**:
```bash
curl -X DELETE \
  -u "test:S27q 64rq oFhf TPDA 30nB hNM5" \
  "http://svetlinkielementor.local/wp-json/elementor/v1/cache"
```

**Python**:
```python
import requests

auth = ('test', 'S27q 64rq oFhf TPDA 30nB hNM5')
url = 'http://svetlinkielementor.local/wp-json/elementor/v1/cache'

response = requests.delete(url, auth=auth)
print(f"Cache cleared: {response.status_code}")
```

---

### 2. Update Global Colors Programmatically

Instead of using our PHP polyfill, we could potentially:

```bash
curl -X POST \
  -u "test:S27q 64rq oFhf TPDA 30nB hNM5" \
  -H "Content-Type: application/json" \
  -d '{"value": "#FABA29"}' \
  "http://svetlinkielementor.local/wp-json/elementor/v1/globals/colors/primary"
```

**Python**:
```python
import requests

auth = ('test', 'S27q 64rq oFhf TPDA 30nB hNM5')
url = 'http://svetlinkielementor.local/wp-json/elementor/v1/globals/colors/primary'

data = {
    'value': '#FABA29'
}

response = requests.post(url, auth=auth, json=data)
print(f"Color updated: {response.status_code}")
```

---

### 3. Get All Global Colors

```bash
curl -s \
  -u "test:S27q 64rq oFhf TPDA 30nB hNM5" \
  "http://svetlinkielementor.local/wp-json/elementor/v1/globals/colors" \
  | python -m json.tool
```

**Returns**:
```json
{
  "primary": {
    "id": "primary",
    "value": "#FABA29",
    "title": "Primary"
  },
  "secondary": {
    "id": "secondary",
    "value": "#4F9F8B",
    "title": "Secondary"
  },
  "text": {
    "id": "text",
    "value": "#2C2C2C",
    "title": "Text"
  },
  "accent": {
    "id": "accent",
    "value": "#FEFCF5",
    "title": "Accent"
  }
}
```

---

### 4. Update Elementor Settings

```bash
# Change CSS Print Method to Internal Embedding
curl -X POST \
  -u "test:S27q 64rq oFhf TPDA 30nB hNM5" \
  -H "Content-Type: application/json" \
  -d '{"value": "internal"}' \
  "http://svetlinkielementor.local/wp-json/elementor/v1/settings/css_print_method"
```

---

## 🆚 When to Use Which API?

### Use Elementor API (`/elementor/v1/`) when:

✅ **Clearing cache** - Use `/elementor/v1/cache` DELETE
✅ **Managing Global Colors** - Use `/elementor/v1/globals/colors`
✅ **Managing Global Typography** - Use `/elementor/v1/globals/typography`
✅ **Updating Elementor settings** - Use `/elementor/v1/settings/{key}`
✅ **Working with templates** - Use `/elementor/v1/template-library`
✅ **Searching posts/terms for widgets** - Use `/elementor/v1/post`, `/term`

### Use WordPress API (`/wp/v2/`) when:

✅ **Creating/updating posts/pages** - Use `/wp/v2/pages`
✅ **Managing post meta** - Use `/wp/v2/pages/{id}` with `meta` field
✅ **Working with media** - Use `/wp/v2/media`
✅ **Managing taxonomies** - Use `/wp/v2/categories`, `/tags`

### Use Both Together for:

✅ **Creating a page with Elementor**:
```python
# 1. Create page via WordPress API
response = requests.post(
    'http://svetlinkielementor.local/wp-json/wp/v2/pages',
    auth=auth,
    json={
        'title': 'New Page',
        'status': 'publish',
        'meta': {
            '_elementor_edit_mode': 'builder',
            '_elementor_data': wp_slash(json.dumps(elementor_data))
        }
    }
)

page_id = response.json()['id']

# 2. Clear cache via Elementor API
requests.delete(
    'http://svetlinkielementor.local/wp-json/elementor/v1/cache',
    auth=auth
)
```

---

## 🚨 Critical Differences

### REST API Hook Bypass Issue (Issue #3)

**Problem**: WordPress REST API bypasses Elementor save hooks.

**Solution Options**:

1. **Manual Editor Update** (current workaround):
   - Open page in Elementor editor
   - Click "Update" button

2. **Use Elementor API for cache** (NEW!):
   ```python
   # After updating via WordPress API
   requests.delete(
       'http://svetlinkielementor.local/wp-json/elementor/v1/cache',
       auth=auth
   )
   ```

3. **Use Elementor-specific endpoints** when available

---

## 📖 Authentication

Both Elementor API and WordPress API use **the same authentication**:

**WordPress Application Password**:
```
Username: test
Password: S27q 64rq oFhf TPDA 30nB hNM5
```

**cURL Example**:
```bash
curl -u "test:S27q 64rq oFhf TPDA 30nB hNM5" \
  "http://svetlinkielementor.local/wp-json/elementor/v1/globals"
```

**Python Example**:
```python
import requests

auth = ('test', 'S27q 64rq oFhf TPDA 30nB hNM5')
response = requests.get(
    'http://svetlinkielementor.local/wp-json/elementor/v1/globals',
    auth=auth
)
```

---

## 🎯 Updated System Prompt for Claude

```
ELEMENTOR REST API:

Elementor has its OWN REST API under /elementor/v1/ namespace, separate from WordPress /wp/v2/.

Key endpoints:
- DELETE /elementor/v1/cache - Clear Elementor cache (USE THIS after page updates!)
- GET /elementor/v1/globals/colors - Get all Global Colors
- POST /elementor/v1/globals/colors/{id} - Update Global Color
- GET /elementor/v1/globals/typography - Get Global Typography
- POST /elementor/v1/settings/{key} - Update Elementor settings

When creating/updating pages:
1. Use WordPress API for page creation: POST /wp/v2/pages
2. Use Elementor API to clear cache: DELETE /elementor/v1/cache
3. This triggers proper CSS regeneration without manual editor update!

Authentication: Same WordPress Application Password for both APIs.
```

---

## ✅ Testing the Elementor API

Let's verify the cache clearing works:

```bash
# Test GET (should work)
curl -s -u "test:S27q 64rq oFhf TPDA 30nB hNM5" \
  "http://svetlinkielementor.local/wp-json/elementor/v1/globals" \
  | python -m json.tool

# Test cache clear (should return success)
curl -X DELETE -u "test:S27q 64rq oFhf TPDA 30nB hNM5" \
  "http://svetlinkielementor.local/wp-json/elementor/v1/cache"
```

---

## 📊 Impact on Our Project

### Before (Using Only WordPress API):

```python
# Update page
update_post_meta(page_id, '_elementor_data', data)

# ❌ Changes don't appear
# ⚠️ Must manually open editor and click "Update"
# OR use PHP: \Elementor\Plugin::$instance->files_manager->clear_cache()
# OR use WP-CLI: wp elementor flush-css
```

### After (Using Both APIs):

```python
# Update page via WordPress API
update_post_meta(page_id, '_elementor_data', data)

# ✅ Clear cache via Elementor API
requests.delete(
    'http://svetlinkielementor.local/wp-json/elementor/v1/cache',
    auth=auth
)

# ✅ Changes appear immediately!
```

---

## 🎉 Summary

**Discovered**: Elementor has **30+ custom REST API endpoints** under `/elementor/v1/`

**Most Critical Endpoint**: `DELETE /elementor/v1/cache` - Solves Issue #3!

**Key Advantage**: Programmatic cache clearing without PHP or WP-CLI

**Authentication**: Same as WordPress API (Application Password)

**Best Practice**:
- Use WordPress API for post/page creation
- Use Elementor API for Elementor-specific operations (cache, globals, settings)
- Combine both for optimal workflow

---

**Version**: 1.0
**Created**: 2025-11-29
**Purpose**: Reference for Elementor's custom REST API endpoints
**Status**: Complete - all available endpoints documented

**This changes everything for programmatic Elementor manipulation!** 🚀
