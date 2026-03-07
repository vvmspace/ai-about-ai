const fs = require('fs');
const path = require('path');
const MarkdownIt = require('markdown-it');
const epub = require('epub-gen');
const cheerio = require('cheerio');
const frontMatter = require('front-matter');
const hljs = require('highlight.js');

const BOOKS_DIR = path.resolve(__dirname, '../../books');
const BUILDS_DIR = path.resolve(__dirname, '../../builds');
const GITHUB_BASE_URL = 'https://github.com/vvmspace/ai-about-ai/tree/main/books';

const md = new MarkdownIt({
    html: true,
    linkify: true,
    typographer: true,
    highlight: function (str, lang) {
        if (lang && hljs.getLanguage(lang)) {
            try {
                return '<pre class="hljs"><code>' +
                    hljs.highlight(str, { language: lang, ignoreIllegals: true }).value +
                    '</code></pre>';
            } catch (__) { }
        }
        return '<pre class="hljs"><code>' + md.utils.escapeHtml(str) + '</code></pre>';
    }
});

if (!fs.existsSync(BUILDS_DIR)) {
    fs.mkdirSync(BUILDS_DIR, { recursive: true });
}

async function getBooks() {
    return fs.readdirSync(BOOKS_DIR).filter(file => {
        return fs.statSync(path.join(BOOKS_DIR, file)).isDirectory();
    });
}

function getChapters(bookDir) {
    const files = fs.readdirSync(bookDir).filter(file => file.endsWith('.md'));
    // Sort alphanumerically
    return files.sort((a, b) => a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' }));
}

function processContent(content, bookName, fileName) {
    const fm = frontMatter(content);
    let html = md.render(fm.body);
    const $ = cheerio.load(html);

    // Link replacement logic
    $('a').each((i, link) => {
        const href = $(link).attr('href');
        if (href && href.startsWith('../')) {
            // It's a relative link to another book or parent directory
            // Resolved path from the perspective of the current file
            // Note: input is ../other_book/file.md
            // We want https://github.com/vvmspace/ai-about-ai/tree/main/books/other_book/file.md

            // Remove the leading ../
            const relativePath = href.replace(/^\.\.\//, '');
            const absoluteUrl = `${GITHUB_BASE_URL}/${relativePath}`;

            $(link).attr('href', absoluteUrl);
        } else if (href && !href.startsWith('http') && !href.startsWith('#')) {
            // Local link within the same book (e.g., ./chapter.md or just chapter.md)
            // These might need handling if epub readers don't support file-relative links well,
            // but standard relative links in epub often point to internal content.
            // However, standard epubs expect internal links to point to content IDs or filenames in the manifest.
            // epub-gen might handle this if we pass strict file paths, but often it relies on 'title' or order.
            // For now, we mainly focus on the cross-book requirement. 
            // If it's a link to another MD file in the SAME book, we ideally want it to link to that chapter.
            // This is complex in epub-gen without knowing the final internal structure.
            // We will leave local links alone for now unless they break, or convert them to absolute if requested.
            // The requirement specifically targeted "relative links to other books".
        }
    });

    // Extract title
    let title = fileName.replace('.md', '');
    const h1 = $('h1').first();
    if (h1.length > 0) {
        title = h1.text();
        h1.remove(); // Remove duplicate title if it's going to be the chapter header
    } else if (fm.attributes.title) {
        title = fm.attributes.title;
    }

    return {
        title: title,
        data: $.html()
    };
}

async function buildBook(bookName) {
    console.log(`Building EPUB for: ${bookName}`);
    const bookDir = path.join(BOOKS_DIR, bookName);
    const chaptersFiles = getChapters(bookDir);

    if (chaptersFiles.length === 0) {
        console.log(`No chapters found for ${bookName}, skipping.`);
        return;
    }

    const content = [];

    for (const file of chaptersFiles) {
        const filePath = path.join(bookDir, file);
        const rawContext = fs.readFileSync(filePath, 'utf-8');
        const processed = processContent(rawContext, bookName, file);
        content.push(processed);
    }

    const options = {
        title: bookName.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase()),
        author: "AI",
        output: path.join(BUILDS_DIR, `${bookName}.epub`),
        css: fs.readFileSync(require.resolve('highlight.js/styles/github.css'), 'utf-8') + '\n.hljs { padding: 10px; border-radius: 5px; background: #f6f8fa; }',
        content: content
    };

    const coverPng = path.join(bookDir, 'cover.png');
    const coverJpg = path.join(bookDir, 'cover.jpg');
    if (fs.existsSync(coverPng)) {
        options.cover = coverPng;
    } else if (fs.existsSync(coverJpg)) {
        options.cover = coverJpg;
    }

    try {
        await new epub(options).promise;
        console.log(`Successfully created ${options.output}`);
    } catch (err) {
        console.error(`Failed to generate ${bookName}.epub`, err);
    }
}

async function main() {
    const books = await getBooks();
    for (const book of books) {
        await buildBook(book);
    }
}

main();
