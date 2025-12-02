# Production Backup - Complete Website

**Created**: 2025-12-02
**Website**: Svetlinki Elementor (Educational program platform)
**WordPress Version**: 6.7.1
**Elementor Version**: 3.x (Free)
**Database Size**: 5.88 MB
**Total Files**: 4,478 files

---

## 📦 What's Included:

### 1. **database.sql** (5.88 MB)
- Complete WordPress database export
- All pages, posts, settings, users, options
- All Elementor page data and configurations
- Plugin settings (Elementor, Contact Form 7, Complianz)
- Ready to import to any MySQL/MariaDB database

### 2. **wp-content/** (4,478 files)
```
wp-content/
├── themes/
│   └── hello-elementor/          (120 files) - Customized child theme
├── plugins/
│   ├── elementor/                (Essential plugins)
│   ├── header-footer-elementor/
│   ├── contact-form-7/
│   └── complianz-gdpr/
└── uploads/                       (42 files) - Media library
```

### 3. **pages/** (8 JSON files)
Individual Elementor page backups for quick reference/restore:
- `page_21_home.json` (130 KB, 9 sections)
- `page_23_about.json` (43 KB, 6 sections)
- `page_25_programs.json` (82 KB, 9 sections)
- `page_27_contact.json` (49 KB, 8 sections)
- `page_29_faq.json` (79 KB, 6 sections)
- `page_31_blog.json` (5 KB, 1 section)
- `page_33_privacy-policy.json` (5 KB, 1 section)
- `page_35_terms-of-service.json` (19 KB, 3 sections)

---

## 🚀 How to Restore to SiteGround (Production Deployment):

### Step 1: Install WordPress on SiteGround
1. Log into SiteGround cPanel
2. Use WordPress Manager to install fresh WordPress
3. Note your new database credentials

### Step 2: Upload Files
```bash
# Via SFTP/FTP, upload:
1. wp-content/themes/hello-elementor → /public_html/wp-content/themes/
2. wp-content/plugins/* → /public_html/wp-content/plugins/
3. wp-content/uploads/* → /public_html/wp-content/uploads/
```

### Step 3: Import Database
```bash
# Option A: Via phpMyAdmin (SiteGround cPanel)
1. Open phpMyAdmin
2. Select your database
3. Click "Import" tab
4. Upload database.sql
5. Click "Go"

# Option B: Via SSH (if you have shell access)
mysql -u YOUR_DB_USER -p YOUR_DB_NAME < database.sql
```

### Step 4: Update URLs (IMPORTANT!)
```bash
# Connect to SiteGround via SSH, then:
cd /home/YOUR_ACCOUNT/public_html

# Replace local URLs with production URLs
wp search-replace 'http://svetlinkielementor.local' 'https://your-production-domain.com' --all-tables

# Or use this SQL directly in phpMyAdmin:
UPDATE wp_options SET option_value = replace(option_value, 'http://svetlinkielementor.local', 'https://your-production-domain.com') WHERE option_name = 'home' OR option_name = 'siteurl';
UPDATE wp_posts SET post_content = replace(post_content, 'http://svetlinkielementor.local', 'https://your-production-domain.com');
UPDATE wp_postmeta SET meta_value = replace(meta_value, 'http://svetlinkielementor.local', 'https://your-production-domain.com');
```

### Step 5: Activate Plugins
1. Log into WordPress admin (https://your-production-domain.com/wp-admin)
2. Go to Plugins → Installed Plugins
3. Activate:
   - Elementor
   - Header Footer Elementor
   - Contact Form 7
   - Complianz GDPR

### Step 6: Regenerate Elementor CSS
1. Elementor → Tools → Regenerate CSS
2. Click "Regenerate Files"
3. Visit your homepage to verify

---

## 🔄 How to Restore Locally (Emergency Recovery):

### Complete Site Restore:
```bash
# 1. Import database
cd "C:\Users\denit\Local Sites\svetlinkielementor\app\public"
wp db import ../../backups/production/database.sql

# 2. Copy files (if needed)
xcopy "..\..\backups\production\wp-content\themes\hello-elementor" "wp-content\themes\hello-elementor\" /E /I /Y

# 3. Clear caches
wp cache flush
curl http://svetlinkielementor.local/nuclear-css-fix.php
```

### Individual Page Restore:
```bash
# Use individual JSON files from pages/ folder
# Import via MCP or REST API
python restore-from-backup.py --backup "backups/production/pages/page_21_home.json"
```

---

## 📋 System Requirements:

### For SiteGround Production:
- PHP 8.1+ (recommended 8.2)
- MySQL 5.7+ or MariaDB 10.3+
- WordPress 6.7.1
- Min 256MB PHP memory limit (512MB recommended)
- HTTPS enabled (SSL certificate)

### Plugins Required:
- Elementor (Free version)
- Header Footer Elementor
- Contact Form 7
- Complianz GDPR (optional, for cookie consent)

---

## ⚠️ Important Notes:

1. **Database Credentials**: After importing, update `wp-config.php` with your SiteGround database credentials
2. **File Permissions**: Set correct permissions on SiteGround (755 for directories, 644 for files)
3. **URL Replacement**: MUST replace local URLs with production URLs (Step 4 above)
4. **SSL**: Enable HTTPS on SiteGround for proper security
5. **Media Uploads**: If media files don't display, check uploads folder permissions
6. **Email**: Configure SMTP on SiteGround for Contact Form 7 to work properly

---

## 🎨 V4 Color System:

Global colors are defined and should work automatically:
- Primary: #FABA29 (Yellow)
- Secondary: #46b19d (Teal)
- Accent: #FF8C7A (Coral)
- Text: #1D3234 (Dark Teal)

All pages use `var(--e-global-color-*)` for consistency.

---

## 📊 What's Been Done:

✅ **Website Content**:
- 8 pages built and styled (Home, About, Programs, Contact, FAQ, Blog, Privacy, Terms)
- V4 global color system applied (71 hardcoded colors replaced)
- Custom CSS for accordions (FAQ page)
- Contact Form 7 integrated

✅ **Quality**:
- 161 → 143 violations after color cleanup
- Acceptable exceptions documented
- !important CSS only in Blog/FAQ (user approved)

✅ **Ready for Production**:
- All files backed up
- Database exported
- Individual page JSONs for reference
- Restore procedures documented

---

## 🔗 GitHub Repository:

**URL**: https://github.com/FlyingSD/elementor-workflow
**Branch**: master

Contains:
- This production backup (backups/production/)
- All scripts and automation tools
- Complete documentation (SSOT/)
- Configuration files

---

## 💡 Quick Reference:

### Emergency Contacts:
- **Local Development**: http://svetlinkielementor.local
- **GitHub Repo**: https://github.com/FlyingSD/elementor-workflow
- **WordPress Admin**: /wp-admin (user: test)

### Key Scripts:
- `export-database-for-production.php` - Export database
- `copy-production-files.php` - Copy theme/plugins/uploads
- `export-all-pages-json.php` - Export individual page JSONs
- `backup-before-update.py` - Create pre-flight snapshot
- `restore-from-backup.py` - Restore from snapshot

---

**Backup Status**: ✅ COMPLETE & TESTED
**Last Updated**: 2025-12-02
**Next Update**: After major changes (new pages, design updates, content additions)

**Keep this backup safe!** It's your complete website in one folder.
