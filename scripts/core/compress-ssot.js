#!/usr/bin/env node

/**
 * SSOT Markdown Compressor
 *
 * Purpose: Intelligently compress verbose SSOT files while preserving critical structure
 * Algorithm:
 * 1. Parse markdown by ## headers (ANCHORS - must preserve!)
 * 2. Compress content between headers:
 *    - Remove verbose explanations (keep core info)
 *    - Reduce redundant examples (max 1 per concept)
 *    - Convert paragraphs → bullet lists
 *    - Remove ASCII decorations
 *    - Keep code blocks intact (critical!)
 * 3. Preserve all ## headers (anchor links depend on them)
 * 4. Auto-backup originals before overwriting
 *
 * Usage:
 *   node scripts/core/compress-ssot.js --file SSOT/STATIC_RULES.md --dry-run
 *   node scripts/core/compress-ssot.js --file SSOT/STATIC_RULES.md
 *   node scripts/core/compress-ssot.js --all
 */

const fs = require('fs');
const path = require('path');

// Configuration
const TARGET_FILES = [
  'SSOT/STATIC_RULES.md',
  'SSOT/ELEMENTOR-STRUCTURE-AND-ALIGNMENT-GUIDE.md',
  'SSOT/CORE-WEBSITE-BUILDING-RULES.md',
  'SSOT/ELEMENTOR-API-TECHNICAL-GUIDE.md'
];

const COMPRESSION_RULES = {
  // Remove verbose connectors
  verbosePhrases: [
    /This is important because/gi,
    /It's worth noting that/gi,
    /Keep in mind that/gi,
    /One thing to remember is/gi,
    /As mentioned (earlier|above|previously)/gi,
    /For example, if you/gi,
    /Let's take a look at/gi,
    /In other words/gi
  ],

  // ASCII decorations to remove
  asciiDecorations: [
    /^[━─═]+$/gm,        // Horizontal lines
    /^[│┃║]\s*/gm,       // Vertical bars at start
    /[│┃║]\s*$/gm,       // Vertical bars at end
    /^[┌┐└┘├┤┬┴┼╔╗╚╝╠╣╦╩╬]+$/gm,  // Box drawing
    /^[\*\-_]{3,}$/gm    // Markdown horizontal rules (keep one \n---)
  ],

  // Multiple blank lines → single blank line
  multipleBlankLines: /\n\n\n+/g,

  // Preserve these patterns
  preservePatterns: {
    codeBlocks: /```[\s\S]*?```/g,
    inlineCode: /`[^`]+`/g,
    links: /\[([^\]]+)\]\(([^)]+)\)/g,
    anchors: /<a name="[^"]+"><\/a>/g,
    headers: /^#{1,6}\s+.+$/gm,
    tables: /^\|.+\|$/gm
  }
};

// Parse command line arguments
const args = process.argv.slice(2);
const dryRun = args.includes('--dry-run');
const allFiles = args.includes('--all');
const fileIndex = args.indexOf('--file');
const targetFile = fileIndex !== -1 ? args[fileIndex + 1] : null;

/**
 * Main compression logic
 */
function compressMarkdown(content, filePath) {
  const originalLines = content.split('\n').length;

  // Step 1: Protect critical content (code blocks, links, etc.)
  const protected = {};
  let protectedIndex = 0;

  // Protect code blocks
  content = content.replace(COMPRESSION_RULES.preservePatterns.codeBlocks, (match) => {
    const key = `__PROTECTED_${protectedIndex++}__`;
    protected[key] = match;
    return key;
  });

  // Step 2: Split by ## headers (ANCHORS!)
  const sections = [];
  const headerRegex = /^## .+$/gm;
  let lastIndex = 0;
  let match;

  while ((match = headerRegex.exec(content)) !== null) {
    // Add content before this header
    if (match.index > lastIndex) {
      const beforeContent = content.substring(lastIndex, match.index);
      if (beforeContent.trim()) {
        sections.push({ type: 'content', text: beforeContent });
      }
    }

    // Add the header itself
    sections.push({ type: 'header', text: match[0] });
    lastIndex = match.index + match[0].length;
  }

  // Add remaining content
  if (lastIndex < content.length) {
    const remaining = content.substring(lastIndex);
    if (remaining.trim()) {
      sections.push({ type: 'content', text: remaining });
    }
  }

  // Step 3: Compress content sections (NOT headers!)
  const compressed = sections.map(section => {
    if (section.type === 'header') {
      return section.text; // NEVER compress headers (anchors!)
    }

    let text = section.text;

    // Remove verbose phrases
    COMPRESSION_RULES.verbosePhrases.forEach(pattern => {
      text = text.replace(pattern, '');
    });

    // Remove ASCII decorations
    COMPRESSION_RULES.asciiDecorations.forEach(pattern => {
      text = text.replace(pattern, '');
    });

    // Remove redundant whitespace
    text = text.replace(/ {2,}/g, ' '); // Multiple spaces → single space
    text = text.replace(/\t/g, '  ');   // Tabs → 2 spaces

    // Compress repetitive examples
    text = compressExamples(text);

    // Remove "Note:", "Remember:", etc. (keep content after)
    text = text.replace(/^(Note|Remember|Keep in mind|Important):\s*/gim, '');

    // Shorten emoji-heavy lines (remove excessive decoration)
    text = text.replace(/^([✅❌⭐🔥💡📊🎯]{2,})\s*/gm, '');

    // Convert verbose paragraphs to bullets
    text = paragraphsToBullets(text);

    // Remove multiple blank lines
    text = text.replace(COMPRESSION_RULES.multipleBlankLines, '\n\n');

    // Remove trailing whitespace
    text = text.split('\n').map(line => line.trimEnd()).join('\n');

    return text;
  }).join('\n');

  // Step 4: Restore protected content
  let final = compressed;
  Object.keys(protected).forEach(key => {
    final = final.replace(key, protected[key]);
  });

  // Step 5: Final cleanup
  final = final.replace(COMPRESSION_RULES.multipleBlankLines, '\n\n');
  final = final.trim() + '\n'; // Single newline at EOF

  const compressedLines = final.split('\n').length;
  const savings = ((originalLines - compressedLines) / originalLines * 100).toFixed(1);

  return {
    content: final,
    stats: {
      originalLines,
      compressedLines,
      savings: `${savings}%`,
      file: path.basename(filePath)
    }
  };
}

/**
 * Compress redundant examples
 */
function compressExamples(text) {
  // Look for "Example 1:", "Example 2:", etc.
  const exampleSections = text.match(/Example \d+:[\s\S]*?(?=Example \d+:|$)/gi);

  if (exampleSections && exampleSections.length > 2) {
    // Keep first example, remove others
    const firstExample = exampleSections[0];
    const otherExamples = exampleSections.slice(1);

    otherExamples.forEach(example => {
      text = text.replace(example, '');
    });

    // Add note about removed examples
    text = text.replace(firstExample, firstExample + '\n\n*(Additional examples removed for brevity)*\n');
  }

  return text;
}

/**
 * Convert verbose paragraphs to bullet lists (aggressive compression)
 */
function paragraphsToBullets(text) {
  // Look for paragraphs with multiple sentences
  const paragraphs = text.split('\n\n');

  const converted = paragraphs.map(para => {
    // Skip if already bullets, code, headers, tables, or has emojis (likely formatted)
    if (para.match(/^[\-\*\+]\s/m) ||
        para.match(/^```/) ||
        para.match(/^#{1,6}\s/) ||
        para.match(/^\|/m) ||
        para.match(/[✅❌⭐🔥💡📊🎯]/u) ||
        para.includes('__PROTECTED_') ||
        para.startsWith('**') ||  // Skip if starts with bold (likely list header)
        para.length < 150) {      // Skip short paragraphs
      return para;
    }

    // Check if paragraph has multiple sentences (4+) and is verbose
    const sentences = para.split(/\.\s+/).filter(s => s.trim().length > 20);

    if (sentences.length >= 4 && para.length > 300) {
      // Convert to bullets (more aggressive)
      return sentences
        .slice(0, 3)  // Keep only first 3 sentences
        .map(s => `- ${s.trim()}${s.endsWith('.') ? '' : '.'}`)
        .join('\n');
    }

    return para;
  });

  return converted.join('\n\n');
}

/**
 * Verify all anchors preserved
 */
function verifyAnchors(original, compressed) {
  const originalHeaders = (original.match(/^## .+$/gm) || []);
  const compressedHeaders = (compressed.match(/^## .+$/gm) || []);

  if (originalHeaders.length !== compressedHeaders.length) {
    return {
      valid: false,
      message: `Header count mismatch! Original: ${originalHeaders.length}, Compressed: ${compressedHeaders.length}`
    };
  }

  for (let i = 0; i < originalHeaders.length; i++) {
    if (originalHeaders[i] !== compressedHeaders[i]) {
      return {
        valid: false,
        message: `Header mismatch at index ${i}!\nOriginal: ${originalHeaders[i]}\nCompressed: ${compressedHeaders[i]}`
      };
    }
  }

  return { valid: true, message: 'All anchors preserved ✓' };
}

/**
 * Backup original file
 */
function backupFile(filePath) {
  const backupPath = filePath + '.backup';
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-').split('T')[0];
  const datedBackupPath = filePath.replace('.md', `-backup-${timestamp}.md`);

  // Create both .backup (latest) and dated backup
  fs.copyFileSync(filePath, backupPath);
  fs.copyFileSync(filePath, datedBackupPath);

  return { backupPath, datedBackupPath };
}

/**
 * Process a single file
 */
function processFile(filePath, options = {}) {
  const fullPath = path.join(__dirname, '../../', filePath);

  if (!fs.existsSync(fullPath)) {
    console.error(`❌ File not found: ${filePath}`);
    return null;
  }

  console.log(`\n📄 Processing: ${filePath}`);
  console.log('━'.repeat(60));

  // Read original
  const original = fs.readFileSync(fullPath, 'utf8');

  // Compress
  const result = compressMarkdown(original, filePath);

  // Verify anchors
  const anchorCheck = verifyAnchors(original, result.content);

  console.log(`📊 Original: ${result.stats.originalLines} lines`);
  console.log(`📊 Compressed: ${result.stats.compressedLines} lines`);
  console.log(`💾 Savings: ${result.stats.savings}`);
  console.log(`🔗 Anchors: ${anchorCheck.message}`);

  if (!anchorCheck.valid) {
    console.error(`\n⚠️  WARNING: ${anchorCheck.message}`);
    console.error('❌ Compression aborted - anchors would be broken!');
    return null;
  }

  if (options.dryRun) {
    console.log('\n🔍 DRY RUN - No files modified');

    // Show preview (first 500 chars)
    console.log('\n📝 Preview (first 500 chars):');
    console.log('─'.repeat(60));
    console.log(result.content.substring(0, 500) + '...');
    console.log('─'.repeat(60));
  } else {
    // Backup original
    const backups = backupFile(fullPath);
    console.log(`\n💾 Backup created: ${path.basename(backups.backupPath)}`);
    console.log(`💾 Dated backup: ${path.basename(backups.datedBackupPath)}`);

    // Write compressed version
    fs.writeFileSync(fullPath, result.content, 'utf8');
    console.log(`✅ Compressed file written!`);
  }

  return result.stats;
}

/**
 * Main execution
 */
function main() {
  console.log('🗜️  SSOT Markdown Compressor');
  console.log('═'.repeat(60));

  if (args.includes('--help') || args.length === 0) {
    console.log(`
Usage:
  node scripts/core/compress-ssot.js --file <path> [--dry-run]
  node scripts/core/compress-ssot.js --all [--dry-run]

Options:
  --file <path>   Compress specific file (e.g., SSOT/STATIC_RULES.md)
  --all           Compress all target files
  --dry-run       Preview without modifying files
  --help          Show this help

Target Files:
${TARGET_FILES.map(f => `  - ${f}`).join('\n')}

Examples:
  # Preview compression
  node scripts/core/compress-ssot.js --file SSOT/STATIC_RULES.md --dry-run

  # Actually compress
  node scripts/core/compress-ssot.js --file SSOT/STATIC_RULES.md

  # Compress all SSOT files
  node scripts/core/compress-ssot.js --all
`);
    return;
  }

  const options = { dryRun };
  const allStats = [];

  if (allFiles) {
    console.log('\n📦 Processing all target files...\n');

    TARGET_FILES.forEach(file => {
      const stats = processFile(file, options);
      if (stats) allStats.push(stats);
    });
  } else if (targetFile) {
    const stats = processFile(targetFile, options);
    if (stats) allStats.push(stats);
  } else {
    console.error('\n❌ Error: Must specify --file or --all');
    console.log('Run with --help for usage information');
    process.exit(1);
  }

  // Summary
  if (allStats.length > 0) {
    console.log('\n' + '═'.repeat(60));
    console.log('📊 COMPRESSION SUMMARY');
    console.log('═'.repeat(60));

    const totalOriginal = allStats.reduce((sum, s) => sum + s.originalLines, 0);
    const totalCompressed = allStats.reduce((sum, s) => sum + s.compressedLines, 0);
    const totalSavings = ((totalOriginal - totalCompressed) / totalOriginal * 100).toFixed(1);

    allStats.forEach(stats => {
      console.log(`${stats.file}:`);
      console.log(`  ${stats.originalLines} → ${stats.compressedLines} lines (${stats.savings})`);
    });

    console.log('\n' + '─'.repeat(60));
    console.log(`Total: ${totalOriginal} → ${totalCompressed} lines (${totalSavings}% savings)`);
    console.log('═'.repeat(60));

    if (dryRun) {
      console.log('\n💡 Run without --dry-run to apply changes');
    } else {
      console.log('\n✅ Compression complete!');
      console.log('💾 Backups saved with .backup and -backup-YYYY-MM-DD.md extensions');
      console.log('🔗 All anchors verified and preserved');
    }
  }
}

// Execute
main();
