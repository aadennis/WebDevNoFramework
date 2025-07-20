import re

def generate_svg_positions(chord_code, chord_name=""):
    """
    Generates SVG elements from a 6-char chord code.
    chord_code: string 6 to 1 (low E → high e), e.g. 'X32010'
    chord_name: label above the diagram
    """
    svg = []
    string_spacing = 30
    fret_spacing = 40

    if chord_name:
        svg.append(f'    <text class="fret-label" x="85" y="-2">{chord_name}</text>')

    for i, fret in enumerate(chord_code):
        x = 10 + i * string_spacing

        if fret.upper() == 'X':
            svg.append(f'    <text class="string-muted" x="{x}" y="5">X</text>')
        elif fret == '0':
            svg.append(f'    <text class="fret-label" x="{x}" y="5">0</text>')
        elif fret.isdigit():
            y = int(fret) * fret_spacing
            svg.append(f'    <circle class="dot-active" cx="{x}" cy="{y}" r="6" />')
        else:
            svg.append(f'<!-- Invalid input on string {6 - i}: {fret} -->')

    return '\n'.join(svg)


def generate_full_html(chord_code, chord_name=""):
    """
    Returns full HTML document with embedded SVG chord diagram.
    """
    svg_positions = generate_svg_positions(chord_code, chord_name)
    fret_lines = generate_fret_lines()


    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{chord_name} – Fretboard Diagram</title>
  <link rel="stylesheet" href="fretboard.css">
</head>
<body>
  <svg xmlns="http://www.w3.org/2000/svg"
       width="200" height="200"
       viewBox="-10 -20 220 220"
       preserveAspectRatio="xMidYMid meet"
       class="fretboard">

    <!-- Strings -->
    <line class="string-line" x1="10" y1="10" x2="10" y2="190" />
    <line class="string-line" x1="40" y1="10" x2="40" y2="190" />
    <line class="string-line" x1="70" y1="10" x2="70" y2="190" />
    <line class="string-line" x1="100" y1="10" x2="100" y2="190" />
    <line class="string-line" x1="130" y1="10" x2="130" y2="190" />
    <line class="string-line" x1="160" y1="10" x2="160" y2="190" />

    <!-- inject:frets -->
    <!-- START frets -->
{fret_lines}
    <!-- END frets -->

    <!-- inject:positions -->
    <!-- START positions -->
{svg_positions}
    <!-- END positions -->
  </svg>
</body>
</html>"""


def sanitize_filename(chord_name):
    # Replace spaces and special chars with hyphens, force lowercase
    name = re.sub(r'\s+', '-', chord_name.strip())
    name = re.sub(r'[^\w\-]', '', name)  # Remove non-filename-safe chars
    return f"chord-{name.lower()}.html"

def generate_fret_lines(y_fret_start=10, y_fret_increment=40, num_frets=5):
    """
    Dynamically generates SVG <line> elements for fret bars.
    """
    lines = []
    for i in range(num_frets):
        y = y_fret_start + i * y_fret_increment
        x1 = 10 if i != 0 else 8
        x2 = 160 if i != 0 else 162
        lines.append(f'    <line class="fret-bar" x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" />')

    return '\n'.join(lines)


def main():
    chord_code = "X32010"
    chord_name = "C Major"
    html_output = generate_full_html(chord_code, chord_name)

    filename = sanitize_filename(chord_name)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_output)

    print(f"✅ Generated: {filename}")


if __name__ == "__main__":
    main()