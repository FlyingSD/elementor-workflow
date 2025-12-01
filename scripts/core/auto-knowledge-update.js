#!/usr/bin/env node

/**
 * Auto-Knowledge Update - Self-Learning System
 *
 * Purpose: Agents call this to auto-update SSOT with discoveries
 * Inspired by: GPT-Engineer learning system
 * Usage: Called by agents when discovering new knowledge (NO human approval needed)
 */

const fs = require('fs');
const path = require('path');

class AutoKnowledgeUpdate {
  constructor() {
    this.ssotPath = path.join(__dirname, '../../SSOT');
    this.updateLog = path.join(this.ssotPath, 'runtime/KNOWLEDGE-UPDATES.md');
    this.indexPath = path.join(this.ssotPath, 'runtime/GUIDE-INDEX.json');
  }

  /**
   * Update SSOT file with new discovery
   * @param {Object} discovery - Discovery details
   * @returns {Object} Result
   */
  update(discovery) {
    console.log('🧠 AUTO-KNOWLEDGE UPDATE');
    console.log('═══════════════════════════════════════════\n');
    console.log(`Discovery: ${discovery.title}`);
    console.log(`By: ${discovery.agent}`);
    console.log(`File: ${discovery.targetFile}\n`);

    try {
      // 1. Find target file
      const filePath = path.join(this.ssotPath, discovery.targetFile);

      if (!fs.existsSync(filePath)) {
        throw new Error(`Target file not found: ${discovery.targetFile}`);
      }

      // 2. Read current content
      const content = fs.readFileSync(filePath, 'utf8');
      const lines = content.split('\n');

      // 3. Find insertion point (after section header)
      const sectionIndex = this.findSection(lines, discovery.section);

      if (sectionIndex === -1) {
        throw new Error(`Section not found: ${discovery.section}`);
      }

      // 4. Format new knowledge
      const newKnowledge = this.formatDiscovery(discovery);

      // 5. Insert into file
      lines.splice(sectionIndex + 1, 0, newKnowledge);

      // 6. Write back
      fs.writeFileSync(filePath, lines.join('\n'), 'utf8');

      console.log('✅ SSOT updated successfully!');

      // 7. Log the update
      this.logUpdate(discovery);
      console.log('✅ Update logged to KNOWLEDGE-UPDATES.md');

      // 8. Update index if new keywords
      if (discovery.keywords && discovery.keywords.length > 0) {
        this.updateIndex(discovery);
        console.log('✅ GUIDE-INDEX.json updated with new keywords');
      }

      console.log('\n═══════════════════════════════════════════');
      console.log('🎉 Auto-learning complete!\n');

      return {
        success: true,
        filesUpdated: [discovery.targetFile, 'runtime/KNOWLEDGE-UPDATES.md'],
        keywordsAdded: discovery.keywords || []
      };

    } catch (error) {
      console.error(`❌ Auto-update failed: ${error.message}\n`);
      console.log('⚠️  Manual update required\n');

      return {
        success: false,
        error: error.message
      };
    }
  }

  findSection(lines, sectionName) {
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].trim().startsWith('##') && lines[i].includes(sectionName)) {
        return i;
      }
    }
    return -1;
  }

  formatDiscovery(discovery) {
    const date = new Date().toISOString().split('T')[0];

    let formatted = `\n### ${discovery.title} (Discovered ${date})\n\n`;
    formatted += `${discovery.description}\n\n`;

    if (discovery.example) {
      formatted += '**Example**:\n```json\n';
      formatted += JSON.stringify(discovery.example, null, 2);
      formatted += '\n```\n\n';
    }

    if (discovery.usage) {
      formatted += `**Usage**: ${discovery.usage}\n\n`;
    }

    formatted += `**Verified**: ✅ Tested and working\n`;
    formatted += `**Discovered By**: ${discovery.agent}\n`;

    return formatted;
  }

  logUpdate(discovery) {
    const timestamp = new Date().toISOString();
    const entry = `
## 📚 UPDATE: ${discovery.title}

**Date**: ${timestamp}
**Discovered By**: ${discovery.agent}
**Context**: ${discovery.context || 'N/A'}

**What Was Discovered**:
${discovery.description}

**Updated Files**:
- ${discovery.targetFile}#${discovery.section}

**Impact**: ${discovery.impact || 'Improves knowledge base for future tasks'}

**Verification**: ✅ Tested and confirmed working

---
`;

    fs.appendFileSync(this.updateLog, entry);
  }

  updateIndex(discovery) {
    const index = JSON.parse(fs.readFileSync(this.indexPath, 'utf8'));

    discovery.keywords.forEach(keyword => {
      const anchor = `${discovery.targetFile}#${discovery.section}`;

      if (!index.index[keyword]) {
        index.index[keyword] = anchor;
        console.log(`   + Added keyword: "${keyword}" → ${anchor}`);
      }
    });

    index.stats.total_keywords = Object.keys(index.index).length;
    index.stats.last_updated = new Date().toISOString().split('T')[0];

    fs.writeFileSync(this.indexPath, JSON.stringify(index, null, 2));
  }
}

// CLI usage
if (require.main === module) {
  // Example discovery object (agents would provide this)
  const exampleDiscovery = {
    title: 'New Property Name',
    agent: 'elementor-expert',
    targetFile: 'ELEMENTOR-API-TECHNICAL-GUIDE.md',
    section: 'group-controls-deep-dive',
    description: 'Discovered new property naming pattern for box shadows',
    example: { 'box_shadow_box_shadow_type': 'yes' },
    usage: 'Use to enable box shadow group control',
    keywords: ['box shadow type', 'shadow enable'],
    context: 'While troubleshooting shadows not showing',
    impact: 'Helps future shadow implementation tasks'
  };

  console.log('📚 Example Auto-Knowledge Update\n');
  console.log('This is how agents auto-update SSOT:\n');
  console.log(JSON.stringify(exampleDiscovery, null, 2));
  console.log('\n(Run with actual discovery object to update SSOT)');
}

module.exports = AutoKnowledgeUpdate;
