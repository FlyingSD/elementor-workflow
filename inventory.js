const fs = require('fs');
const path = require('path');

const baseDir = process.cwd();
const inventory = {
  rootFiles: [],
  claude: [],
  ssot: [],
  scripts: [],
  templates: [],
  screenshots: [],
  backups: [],
  comparison: [],
  other: []
};

// Ignore patterns
const ignorePatterns = [
  'node_modules',
  '.git',
  'app/public/wp-admin',
  'app/public/wp-includes',
  'app/public/wp-content/plugins',
  'app/public/wp-content/themes/twenty',
  'app/sql',
  'logs',
  'conf'
];

function shouldIgnore(filePath) {
  return ignorePatterns.some(pattern => filePath.includes(pattern));
}

function getFileInfo(filePath) {
  const stats = fs.statSync(filePath);
  const relativePath = path.relative(baseDir, filePath);
  const ext = path.extname(filePath);

  return {
    path: relativePath,
    size: stats.size,
    sizeKB: (stats.size / 1024).toFixed(2),
    ext: ext,
    modified: stats.mtime.toISOString().split('T')[0]
  };
}

function scanDirectory(dir, category = null) {
  const items = fs.readdirSync(dir);

  items.forEach(item => {
    const fullPath = path.join(dir, item);

    if (shouldIgnore(fullPath)) return;

    const stats = fs.statSync(fullPath);

    if (stats.isDirectory()) {
      scanDirectory(fullPath, category);
    } else {
      const fileInfo = getFileInfo(fullPath);
      const relativePath = fileInfo.path;

      // Categorize
      if (relativePath.startsWith('.claude')) {
        inventory.claude.push(fileInfo);
      } else if (relativePath.startsWith('SSOT')) {
        inventory.ssot.push(fileInfo);
      } else if (fileInfo.ext === '.py') {
        inventory.scripts.push(fileInfo);
      } else if (fileInfo.ext === '.json' && relativePath.includes('template')) {
        inventory.templates.push(fileInfo);
      } else if (['.png', '.jpg', '.jpeg'].includes(fileInfo.ext)) {
        inventory.screenshots.push(fileInfo);
      } else if (relativePath.startsWith('backups')) {
        inventory.backups.push(fileInfo);
      } else if (relativePath.startsWith('2025-11-26-comparison') || relativePath.startsWith('comparison')) {
        inventory.comparison.push(fileInfo);
      } else if (relativePath.startsWith('2025-11-26-current-state')) {
        inventory.screenshots.push(fileInfo);
      } else if (!relativePath.startsWith('app/')) {
        if (fileInfo.ext === '.md' || fileInfo.ext === '.txt' || fileInfo.ext === '.json') {
          inventory.rootFiles.push(fileInfo);
        } else {
          inventory.other.push(fileInfo);
        }
      }
    }
  });
}

function printInventory() {
  console.log('='.repeat(70));
  console.log('PROJECT INVENTORY - Elementor Workflow');
  console.log('='.repeat(70));

  Object.entries(inventory).forEach(([category, files]) => {
    if (files.length === 0) return;

    const totalSize = files.reduce((sum, f) => sum + parseFloat(f.sizeKB), 0);

    console.log(`\n## ${category.toUpperCase()} (${files.length} files, ${totalSize.toFixed(2)} KB)`);
    console.log('-'.repeat(70));

    files.forEach(file => {
      const sizeStr = file.sizeKB.padStart(8) + ' KB';
      console.log(`${sizeStr}  ${file.path}`);
    });
  });

  console.log('\n' + '='.repeat(70));
  const allFiles = Object.values(inventory).flat();
  const totalFiles = allFiles.length;
  const totalSize = allFiles.reduce((sum, f) => sum + parseFloat(f.sizeKB), 0);
  console.log(`TOTAL: ${totalFiles} files, ${totalSize.toFixed(2)} KB (${(totalSize/1024).toFixed(2)} MB)`);
  console.log('='.repeat(70));
}

// Run scan
scanDirectory(baseDir);
printInventory();
