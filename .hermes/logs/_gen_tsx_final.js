const fs = require('fs');
const p = require('path');
const D = '/mnt/f/aitoptools/.hermes/logs';
const data = JSON.parse(fs.readFileSync(p.join(D, '2026-07-03-新工具入库.json')));
const tools = data.tools.slice(0, 5);
tools.forEach(t => {
  const name = t.name || t.slug.replace('-review','').replace(/-/g,' ');
  const slug = t.slug;
  const tsx = 'import Link from "next/link"' + '\n' +
    'export default function ReviewPage() {' + '\n' +
    '  return (' + '\n' +
    '    <div className="container">' + '\n' +
    '      <h1>' + t.slug.charAt(0).toUpperCase() + t.slug.slice(1).replace(/-/g,' ') + '</h1>' + '\n' +
    '      <p>' + (t.description || '') + '</p>' + '\n' +
    '    </div>' + '\n' +
    '  )}' + '\n';
  const fname = '2026-07-03-长尾-' + slug + '.tsx';
  fs.writeFileSync(p.join(D, fname), tsx);
  console.log('Created:', fname);
});
console.log('Done');

