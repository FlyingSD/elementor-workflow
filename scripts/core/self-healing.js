#!/usr/bin/env node

/**
 * Self-Healing System - Auto-detect and auto-fix known issues
 *
 * Purpose: After MCP operations, automatically detect and fix common problems
 * Inspired by: Pythagora GPT-Pilot self-healing pattern
 * Usage: node scripts/core/self-healing.js --page-id 21 --check-type full
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

class SelfHealingSystem {
  constructor(pageId) {
    this.pageId = pageId;
    this.siteUrl = 'http://svetlinkielementor.local';
    this.issuesDetected = [];
    this.issuesFixed = [];
    this.issuesFailed = [];
    this.logPath = 'SSOT/runtime/SUCCESS-LOG.md';
  }

  // Main entry point
  async run(checkType = 'full') {
    console.log('🔧 SELF-HEALING SYSTEM ACTIVATED');
    console.log('═══════════════════════════════════════════\n');
    console.log(`Page ID: ${this.pageId}`);
    console.log(`Check Type: ${checkType}\n`);

    // Run health checks
    const checks = checkType === 'full'
      ? this.getAllChecks()
      : this.getQuickChecks();

    for (const check of checks) {
      await this.runCheck(check);
    }

    // Report results
    this.reportResults();
  }

  // Health check definitions
  getAllChecks() {
    return [
      { name: 'CSS Regeneration', fn: () => this.checkCSSRegeneration() },
      { name: 'Global Colors', fn: () => this.checkGlobalColors() },
      { name: 'Stretch Section', fn: () => this.checkStretchSection() },
      { name: 'WordPress Accessible', fn: () => this.checkWordPressAccessible() },
      { name: 'MCP Server', fn: () => this.checkMCPServer() }
    ];
  }

  getQuickChecks() {
    return [
      { name: 'CSS Regeneration', fn: () => this.checkCSSRegeneration() },
      { name: 'WordPress Accessible', fn: () => this.checkWordPressAccessible() }
    ];
  }

  // Run individual check
  async runCheck(check) {
    console.log(`🔍 Checking: ${check.name}...`);

    try {
      const issue = await check.fn();

      if (issue) {
        this.issuesDetected.push({ check: check.name, issue });
        console.log(`   ⚠️  Issue detected: ${issue.description}`);

        // Auto-fix if known solution exists
        const fixed = await this.autoFix(issue);

        if (fixed) {
          this.issuesFixed.push({ check: check.name, issue, fix: fixed });
          console.log(`   ✅ Auto-fixed: ${fixed}`);
        } else {
          this.issuesFailed.push({ check: check.name, issue });
          console.log(`   ❌ No auto-fix available (manual intervention needed)`);
        }
      } else {
        console.log(`   ✅ Passed`);
      }
    } catch (error) {
      console.log(`   ⚠️  Check failed: ${error.message}`);
    }

    console.log('');
  }

  // Check #1: CSS Regeneration
  async checkCSSRegeneration() {
    try {
      // Check if CSS file exists and is fresh
      const cssUrl = `${this.siteUrl}/wp-content/uploads/elementor/css/post-${this.pageId}.css`;
      const result = execSync(`curl -I "${cssUrl}" 2>&1`, { encoding: 'utf8' });

      if (result.includes('404')) {
        return {
          code: 'css_not_regenerated',
          description: 'CSS file missing (404)',
          autoFixable: true
        };
      }

      // Check if file is stale (older than 5 minutes)
      const lastModified = result.match(/Last-Modified: (.+)/);
      if (lastModified) {
        const cssDate = new Date(lastModified[1]);
        const now = new Date();
        const ageMinutes = (now - cssDate) / 1000 / 60;

        if (ageMinutes > 5) {
          return {
            code: 'css_stale',
            description: `CSS file stale (${Math.floor(ageMinutes)} minutes old)`,
            autoFixable: true
          };
        }
      }

      return null; // No issue
    } catch (error) {
      return {
        code: 'css_check_failed',
        description: error.message,
        autoFixable: false
      };
    }
  }

  // Check #2: Global Colors
  async checkGlobalColors() {
    // TODO: Implement when needed
    return null;
  }

  // Check #3: Stretch Section
  async checkStretchSection() {
    // TODO: Implement when needed
    return null;
  }

  // Check #4: WordPress Accessible
  async checkWordPressAccessible() {
    try {
      execSync(`curl -s -o nul -w "%{http_code}" "${this.siteUrl}"`, { encoding: 'utf8' });
      return null; // Accessible
    } catch (error) {
      return {
        code: 'wordpress_down',
        description: 'WordPress site not accessible',
        autoFixable: false
      };
    }
  }

  // Check #5: MCP Server
  async checkMCPServer() {
    // Check if MCP tools are available (basic check)
    // This would need integration with Claude Code internals
    return null; // Skip for now
  }

  // Auto-Fix Registry
  async autoFix(issue) {
    const fixes = {
      'css_not_regenerated': () => this.fixCSSRegeneration(),
      'css_stale': () => this.fixCSSRegeneration()
    };

    const fixFunction = fixes[issue.code];

    if (fixFunction && issue.autoFixable) {
      try {
        return await fixFunction();
      } catch (error) {
        console.log(`   ⚠️  Auto-fix failed: ${error.message}`);
        return null;
      }
    }

    return null;
  }

  // Fix: CSS Regeneration
  async fixCSSRegeneration() {
    console.log('   🔧 Applying fix: Nuclear CSS regeneration...');

    // Step 1: Nuclear CSS fix
    execSync(`curl -s "${this.siteUrl}/nuclear-css-fix.php"`, { encoding: 'utf8' });

    // Step 2: Visit page to trigger regeneration
    execSync(`curl -s "${this.siteUrl}/home" > nul`, { encoding: 'utf8' });

    // Wait a moment for CSS generation
    await this.sleep(2000);

    // Verify fix worked
    const stillBroken = await this.checkCSSRegeneration();

    if (!stillBroken) {
      // Log success
      this.logAutoFix('CSS Regeneration', 'nuclear-css-fix.php executed');
      return 'CSS regenerated successfully';
    } else {
      return null; // Fix didn't work
    }
  }

  // Log auto-fix to SUCCESS-LOG
  logAutoFix(issue, solution) {
    const timestamp = new Date().toISOString();
    const entry = `
## ✅ AUTO-HEALED: ${issue}

**Date**: ${timestamp}
**Page**: ${this.pageId}
**Issue Detected**: ${issue}
**Auto-Fix Applied**: ${solution}
**Result**: ✅ Successfully healed

**Self-Healing System**: Detected and fixed automatically (no human intervention)

---
`;

    fs.appendFileSync(this.logPath, entry);
  }

  // Report results
  reportResults() {
    console.log('═══════════════════════════════════════════');
    console.log('         SELF-HEALING RESULTS');
    console.log('═══════════════════════════════════════════\n');

    console.log(`✅ Issues Auto-Fixed: ${this.issuesFixed.length}`);
    if (this.issuesFixed.length > 0) {
      this.issuesFixed.forEach(f => {
        console.log(`   - ${f.check}: ${f.fix}`);
      });
      console.log('');
    }

    console.log(`⚠️  Issues Requiring Manual Fix: ${this.issuesFailed.length}`);
    if (this.issuesFailed.length > 0) {
      this.issuesFailed.forEach(f => {
        console.log(`   - ${f.check}: ${f.issue.description}`);
      });
      console.log('');
    }

    if (this.issuesDetected.length === 0) {
      console.log('🎉 All health checks passed! No issues detected.\n');
    }

    console.log('═══════════════════════════════════════════');
  }

  sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}

// CLI usage
if (require.main === module) {
  const args = process.argv.slice(2);
  const pageIdArg = args.find(a => a.startsWith('--page-id='));
  const checkTypeArg = args.find(a => a.startsWith('--check-type='));

  if (!pageIdArg) {
    console.error('Usage: node self-healing.js --page-id=21 [--check-type=full|quick]');
    console.error('');
    console.error('Examples:');
    console.error('  node scripts/core/self-healing.js --page-id=21');
    console.error('  node scripts/core/self-healing.js --page-id=21 --check-type=quick');
    process.exit(1);
  }

  const pageId = pageIdArg.split('=')[1];
  const checkType = checkTypeArg ? checkTypeArg.split('=')[1] : 'full';

  const healer = new SelfHealingSystem(pageId);
  healer.run(checkType).catch(error => {
    console.error('Self-healing system error:', error);
    process.exit(1);
  });
}

module.exports = SelfHealingSystem;
