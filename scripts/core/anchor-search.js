#!/usr/bin/env node

/**
 * Anchor Search - Targeted SSOT Section Retrieval
 *
 * Purpose: 80% context reduction by loading ONLY relevant sections
 * Usage: node scripts/core/anchor-search.js "card layout"
 * Output: File path + anchor link for targeted reading
 */

const fs = require('fs');
const path = require('path');

// Load index
const indexPath = path.join(__dirname, '../../SSOT/runtime/GUIDE-INDEX.json');
const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));

// Get query from command line
const query = process.argv.slice(2).join(' ').toLowerCase().trim();

if (!query) {
  console.error('Usage: node anchor-search.js "your query"');
  console.error('Example: node anchor-search.js "card layout"');
  process.exit(1);
}

// Search logic
function search(query) {
  // Tier 1: Exact match in index
  if (index.index[query]) {
    return {
      tier: 1,
      match: 'exact',
      query: query,
      result: index.index[query]
    };
  }

  // Tier 2: Alias lookup
  if (index.aliases[query]) {
    const canonical = index.aliases[query];
    return {
      tier: 2,
      match: 'alias',
      query: query,
      canonical: canonical,
      result: index.index[canonical]
    };
  }

  // Tier 3: Fuzzy keyword search
  for (const [keyword, target] of Object.entries(index.index)) {
    if (query.includes(keyword) || keyword.includes(query)) {
      return {
        tier: 3,
        match: 'fuzzy',
        query: query,
        matched_keyword: keyword,
        result: target
      };
    }
  }

  // No match found
  return {
    tier: 0,
    match: 'none',
    query: query,
    result: null,
    suggestion: 'Try broader keywords or check SSOT files directly'
  };
}

// Execute search
const result = search(query);

// Output results
console.log('═══════════════════════════════════════════');
console.log('         ANCHOR SEARCH RESULTS');
console.log('═══════════════════════════════════════════');
console.log('');
console.log(`Query: "${result.query}"`);
console.log(`Match Type: Tier ${result.tier} (${result.match})`);

if (result.canonical) {
  console.log(`Canonical: "${result.canonical}"`);
}

if (result.matched_keyword) {
  console.log(`Matched Keyword: "${result.matched_keyword}"`);
}

console.log('');

if (result.result) {
  console.log('✅ FOUND:');
  console.log(`   ${result.result}`);
  console.log('');
  console.log('📖 Read ONLY this section (targeted load):');
  console.log(`   Read file_path="${result.result.split('#')[0]}"`);
  console.log(`   Look for section: #${result.result.split('#')[1]}`);
  console.log('');
  console.log('💾 Context Saved: ~80% (section vs full file)');
} else {
  console.log('❌ NOT FOUND');
  console.log('');
  console.log('💡 Suggestions:');
  console.log('   - Try broader keywords: "card", "column", "section"');
  console.log('   - Check available keywords: cat SSOT/runtime/GUIDE-INDEX.json');
  console.log('   - Fallback: Read full guide (last resort)');
}

console.log('');
console.log('═══════════════════════════════════════════');

// Exit with status
process.exit(result.result ? 0 : 1);
