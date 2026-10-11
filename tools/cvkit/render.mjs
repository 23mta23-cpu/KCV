// Renders HTML files to A4 PDFs with headless Chromium.
// Usage: node render.mjs <in.html> <out.pdf> [<in2.html> <out2.pdf> ...]
// Pfade per Umgebungsvariable anpassbar; Standardwerte passen zur Claude-Code-Cloud-Umgebung.
const PW = process.env.CVKIT_PLAYWRIGHT || '/home/user/paperclip/node_modules/@playwright/test/index.mjs';
const { chromium } = await import(PW);
import { pathToFileURL } from 'node:url';

const args = process.argv.slice(2);
if (args.length < 2 || args.length % 2) {
  console.error('usage: node render.mjs <in.html> <out.pdf> [...]');
  process.exit(1);
}
const browser = await chromium.launch(process.env.CVKIT_CHROMIUM ? { executablePath: process.env.CVKIT_CHROMIUM } : {});
const page = await browser.newPage();
for (let i = 0; i < args.length; i += 2) {
  await page.goto(pathToFileURL(args[i]).href, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  // Fail loudly if content overflows the A4 page.
  const overflow = await page.evaluate(() => {
    const p = document.querySelector('.page');
    return p ? p.scrollHeight - p.clientHeight : 0;
  });
  if (overflow > 1) console.warn(`WARN ${args[i]}: content overflows page by ${overflow}px`);
  await page.pdf({ path: args[i + 1], format: 'A4', printBackground: true, preferCSSPageSize: true, tagged: true });
  console.log('pdf', args[i + 1]);
}
await browser.close();
