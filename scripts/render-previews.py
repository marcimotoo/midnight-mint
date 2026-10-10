from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json

root = Path(__file__).resolve().parents[1]
package = root
theme = json.loads((package / 'themes/midnight-mint-color-theme.json').read_text(encoding='utf-8'))
colors = theme['colors']
tokens = theme['semanticTokenColors']
palette = {'text': colors['editor.foreground'], 'mint': tokens['keyword'], 'pink': tokens['function'],
           'orange': tokens['string'], 'gold': tokens['number'], 'blue': tokens['namespace'],
           'comment': tokens['comment']['foreground'], 'param': tokens['parameter']}
image = Image.new('RGB', (1800, 1080), '#101313')
draw = ImageDraw.Draw(image)
fonts = Path('C:/Windows/Fonts')
title = ImageFont.truetype(str(fonts / 'segoeuib.ttf'), 62)
label = ImageFont.truetype(str(fonts / 'segoeui.ttf'), 25)
small = ImageFont.truetype(str(fonts / 'segoeui.ttf'), 21)
mono = ImageFont.truetype(str(fonts / 'consola.ttf'), 21)
italic = ImageFont.truetype(str(fonts / 'consolai.ttf'), 21)
bold = ImageFont.truetype(str(fonts / 'consolab.ttf'), 21)
draw.rounded_rectangle((64, 58, 72, 126), 4, fill=palette['mint'])
draw.text((96, 49), 'Midnight Mint', font=title, fill='#f0f5f2')
draw.text((98, 130), 'Dark charcoal. Clear syntax. A quiet touch of neon.', font=label, fill='#a0aca4')

# Explicit token spans keep the code legible and use the theme's actual palette.
js = [
 [('comment', '// A little light after midnight')],
 [('mint', 'const'), ('text', ' theme = {')],
 [('text', '  name: '), ('orange', '"Midnight Mint"'), ('text', ',')],
 [('text', '  accent: '), ('orange', '"#00ff99"'), ('text', ',')],
 [('text', '  contrast: '), ('gold', '4.5')],
 [('text', '};')], [],
 [('mint', 'function'), ('pink', ' greet'), ('text', '('), ('param', 'name'), ('text', ') {')],
 [('mint', '  const'), ('text', ' message = '), ('orange', '`Hello, '), ('text', '${'), ('param', 'name'), ('text', '}'), ('orange', '`'), ('text', ';')],
 [('mint', '  return'), ('text', ' message;')],
 [('text', '}')], [],
 [('text', 'console.'), ('pink', 'log'), ('text', '('), ('pink', 'greet'), ('text', '('), ('orange', '"night owl"'), ('text', '));')],
]
html = [
 [('comment', '<!-- Keep the focus on content -->')],
 [('text', '<'), ('mint', 'main'), ('blue', ' class'), ('text', '='), ('orange', '"card"'), ('text', '>')],
 [('text', '  <'), ('mint', 'h1'), ('text', '>Midnight Mint</'), ('mint', 'h1'), ('text', '>')],
 [('text', '  <'), ('mint', 'p'), ('blue', ' class'), ('text', '='), ('orange', '"subtitle"'), ('text', '>')],
 [('text', '    Less noise. More focus.')],
 [('text', '  </'), ('mint', 'p'), ('text', '>')], [],
 [('text', '  <'), ('mint', 'button')],
 [('blue', '    type'), ('text', '='), ('orange', '"button"')],
 [('blue', '    aria-label'), ('text', '='), ('orange', '"Get started"'), ('text', '>')],
 [('text', '    Start creating')],
 [('text', '  </'), ('mint', 'button'), ('text', '>')],
 [('text', '</'), ('mint', 'main'), ('text', '>')],
]
css = [
 [('comment', '/* Quiet surfaces, bright accents */')],
 [('mint', '.card'), ('text', ' {')],
 [('pink', '  background'), ('text', ': '), ('gold', '#191d1c'), ('text', ';')],
 [('pink', '  color'), ('text', ': '), ('gold', '#d7dfd9'), ('text', ';')],
 [('pink', '  padding'), ('text', ': '), ('gold', '24px'), ('text', ';')],
 [('pink', '  border-radius'), ('text', ': '), ('gold', '12px'), ('text', ';')],
 [('text', '}')], [],
 [('mint', '.card button:hover'), ('text', ' {')],
 [('pink', '  color'), ('text', ': '), ('gold', '#00ff99'), ('text', ';')],
 [('pink', '  cursor'), ('text', ': '), ('orange', 'pointer'), ('text', ';')],
 [('pink', '  transition'), ('text', ': '), ('orange', 'color'), ('text', ' '), ('gold', '180ms'), ('text', ';')],
 [('text', '}')],
]
def render_cards(examples):
    for index, (filename, language, lines) in enumerate(examples):
        x = 64 + index * 572
        draw.rounded_rectangle((x, 215, x + 548, 831), 14, fill=colors['editor.background'], outline='#303a34', width=2)
        draw.rounded_rectangle((x + 1, 216, x + 547, 282), 13, fill='#202624')
        draw.rectangle((x + 1, 260, x + 547, 282), fill='#202624')
        draw.rectangle((x + 22, 280, x + 186, 282), fill=palette['mint'])
        draw.text((x + 24, 233), filename, font=small, fill='#e2ebe5')
        draw.text((x + 24, 776), language, font=small, fill='#a0aca4')
        for number, spans in enumerate(lines, 1):
            y = 309 + (number - 1) * 31
            draw.text((x + 18, y), str(number).rjust(2), font=mono, fill='#65746b')
            cursor = x + 62
            for token, content in spans:
                font = italic if token in ('comment', 'mdItalic') else bold if token in ('mdBold', 'mdHeading') else mono
                draw.text((cursor, y), content, font=font, fill=palette[token])
                cursor += draw.textlength(content, font=font)
            assert cursor < x + 536, f'Code exceeds card: {filename}, line {number}'

render_cards([('hello.js', 'JavaScript', js), ('index.html', 'HTML', html), ('theme.css', 'CSS', css)])

for index, (token, caption) in enumerate([('mint', 'Mint'), ('pink', 'Hot pink'), ('orange', 'Strings'), ('gold', 'Numbers'), ('blue', 'Attributes'), ('comment', 'Comments')]):
    x = 70 + index * 286
    draw.rounded_rectangle((x, 885, x + 20, 905), 5, fill=palette[token])
    draw.text((x + 33, 878), caption, font=label, fill='#d7dfd9')
draw.text((70, 964), 'Visual Studio Code theme  /  Midnight Mint', font=small, fill='#a0aca4')
draw.text((70, 1004), 'Illustrated preview using the theme palette. Token colors may vary by language extension.', font=small, fill='#82948a')
(package / 'images').mkdir(exist_ok=True)
image.save(package / 'images/midnight-mint-preview.png', optimize=True)

palette.update({'lavender': '#c2a4e8', 'link': '#83dbb8', 'raw': '#ce9178', 'mdBold': '#e8eee9', 'mdItalic': '#bfcec4', 'mdHeading': '#00ff99'})
python_lines = [
 [('comment', '# A little light after midnight')],
 [('mint', 'class '), ('mint', 'Palette'), ('text', ':')],
 [('mint', '    def '), ('pink', '__init__'), ('text', '('), ('param', 'self, accent'), ('text', '):')],
 [('text', '        self.'), ('text', 'accent = accent')], [],
 [('mint', '    def '), ('pink', 'describe'), ('text', '('), ('param', 'self, count'), ('text', '):')],
 [('mint', '        return '), ('orange', 'f"Mint: '), ('text', '{count}'), ('orange', '"')], [],
 [('text', 'palette = '), ('mint', 'Palette'), ('text', '('), ('orange', '"#00ff99"'), ('text', ')')],
 [('pink', 'print'), ('text', '(palette.'), ('pink', 'describe'), ('text', '('), ('gold', '3'), ('text', '))')],
]
json_lines = [
 [('text', '{')],
 [('blue', '  "name"'), ('text', ': '), ('orange', '"Midnight Mint"'), ('text', ',')],
 [('blue', '  "accent"'), ('text', ': '), ('orange', '"#00ff99"'), ('text', ',')],
 [('blue', '  "fontSize"'), ('text', ': '), ('gold', '14'), ('text', ',')],
 [('blue', '  "enabled"'), ('text', ': '), ('lavender', 'true'), ('text', ',')],
 [('blue', '  "fallback"'), ('text', ': '), ('lavender', 'null'), ('text', ',')],
 [('blue', '  "languages"'), ('text', ': [')],
 [('orange', '    "Python"'), ('text', ',')],
 [('orange', '    "JavaScript"'), ('text', ',')],
 [('orange', '    "CSS"')],
 [('text', '  ]')],
 [('text', '}')],
]
markdown_lines = [
 [('mdHeading', '# Midnight Mint')], [],
 [('text', 'Less noise. More focus.')], [],
 [('text', 'Write with '), ('mdBold', '**clarity**')],
 [('text', 'and '), ('mdItalic', '*a little color*'), ('text', '.')], [],
 [('text', '- Accent: '), ('raw', '`#00ff99`')],
 [('text', '- Mode: '), ('raw', '`dark`')], [],
 [('link', '[Explore](https://example.com)')], [],
 [('text', '> A quiet touch of neon.')],
]
draw.rectangle((60, 210, 1760, 835), fill='#101313')
draw.rectangle((95, 128, 1740, 170), fill='#101313')
draw.text((98, 130), 'Python, JSON & Markdown / The same palette, more languages.', font=label, fill='#a0aca4')
render_cards([('palette.py', 'Python', python_lines), ('settings.json', 'JSON', json_lines), ('notes.md', 'Markdown', markdown_lines)])
image.save(package / 'images/midnight-mint-languages.png', optimize=True)
