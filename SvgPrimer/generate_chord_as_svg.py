import re

# --- Constants ---
NOTE_NAMES = ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#"]
STRING_ROOTS = ["E", "A", "D", "G", "B", "E"]  # Strings 6 to 1

NOTE_MAP = {note: i for i, note in enumerate(NOTE_NAMES)}

# --- Utilities ---
def note_at(string_index, fret_number):
    """Return the note name for the given string and fret."""
    root_note = STRING_ROOTS[string_index]
    root_index = NOTE_MAP[root_note]
    return NOTE_NAMES[(root_index + fret_number) % 12]

def sanitize_filename(chord_name):
    name = re.sub(r'\s+', '-', chord_name.strip())
    name = re.sub(r'[^\w\-]', '', name)
    return f"chord-{name.lower()}.html"

# --- Diagram Generators ---
def generate_fret_lines(y_fret_start=30, y_fret_increment=40, num_frets=6):
    lines = []
    for i in range(num_frets):
        y = y_fret_start + i * y_fret_increment
        x1 = 10 if i != 0 else 8
        x2 = 160 if i != 0 else 162
        lines.append(f'<line class="fret-bar" x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" />')
    return '\n'.join(lines)

def generate_string_lines(x_start=10, string_spacing=30, y_string_start=30, string_length=220, num_strings=6):
    lines = []
    for i in range(num_strings):
        x = x_start + i * string_spacing
        y1 = y_string_start
        y2 = y_string_start + string_length
        lines.append(f'<line class="string-line" x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" />')
    return '\n'.join(lines)

def generate_svg_positions(
    chord_code,
    chord_name="",
    x_start=10,
    string_spacing=30,
    fret_spacing=40,
    y_marker_top=25,
    y_chord_label=-2,
    dot_radius=6
):
    svg = []

    if chord_name:
        svg.append(f'<text class="fret-label" x="85" y="{y_chord_label}">{chord_name}</text>')

    for i, fret in enumerate(chord_code):
        string_index = i
        x = x_start + i * string_spacing

        if fret.upper() == "X":
            svg.append(f'<text class="string-muted" x="{x}" y="{y_marker_top}">X</text>')
        elif fret == "0":
            note = note_at(string_index, 0)
            svg.append(f'<rect class="note-box" x="{x - 8}" y="{y_marker_top - 12}" width="16" height="16" rx="2" />')
            svg.append(f'<text class="open-note" x="{x}" y="{y_marker_top}">{note}</text>')
        elif fret.isdigit():
            fret_number = int(fret)
            note = note_at(string_index, fret_number)
            y = fret_number * fret_spacing + y_marker_top - dot_radius
            svg.append(f'<circle class="dot-active" cx="{x}" cy="{y}" r="{dot_radius}" />')
            svg.append(f'<rect class="note-box" x="{x - 8}" y="{y - 22}" width="16" height="16" rx="2" />')
            svg.append(f'<text class="note-label" x="{x}" y="{y - 10}">{note}</text>')
        elif fret.isdigit():
            fret_number = int(fret)
            note = note_at(string_index, fret_number)
            y = fret_number * fret_spacing + y_marker_top - dot_radius
            svg.append(f'<circle class="dot-active" cx="{x}" cy="{y}" r="{dot_radius}" />')
            svg.append(f'<text class="note-label" x="{x}" y="{y - 10}">{note}</text>')
        else:
            svg.append(f'<!-- Invalid input on string {6 - i}: {fret} -->')

    return '\n'.join(svg)

# --- HTML Generator ---
def generate_full_html(chord_code, chord_name=""):
    svg_positions = generate_svg_positions(chord_code, chord_name)
    fret_lines = generate_fret_lines()
    string_lines = generate_string_lines()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{chord_name} – Fretboard Diagram</title>
  <link rel="stylesheet" href="fretboard.css">
</head>
<body>
  <svg xmlns="http://www.w3.org/2000/svg"
       width="200" height="280"
       viewBox="-10 -20 220 300"
       preserveAspectRatio="xMidYMid meet"
       class="fretboard">

    <!-- inject:strings -->
{string_lines}
    <!-- END strings -->

    <!-- inject:frets -->
{fret_lines}
    <!-- END frets -->

    <!-- inject:positions -->
{svg_positions}
    <!-- END positions -->
  </svg>
</body>
</html>"""

# --- Execution Stub ---
def main():
    # Example chord codes and names
    chord_code = "X02220"; chord_name = "A Major" 
    chord_code = "X32010"; chord_name = "C Major"  
    chord_code = "XX3213"; chord_name = "Fadd9"
    chord_code = "XX0232"; chord_name = "D Major" 
    chord_code = "022000"; chord_name = "E minor" 
    chord_code = "353533"; chord_name = "G7 sus4" 
    chord_code = "X5453X"; chord_name = "D7 version 2"
    chord_code = "X24432"; chord_name = "B minor" 
    chord_code = "X32030"; chord_name = "C add9"
    chord_code = "XX3211"; chord_name = "F*"
    chord_code = "020000"; chord_name = "Em7 version 1"
    chord_code = "022030"; chord_name = "Em7 version 2"
    chord_code = "X21202"; chord_name = "B7"
    chord_code = "X02223"; chord_name = "A7 version 2"
    chord_code = "X35555"; chord_name = "C6"
    chord_code = "X57777"; chord_name = "D6"
    chord_code = "XX5443"; chord_name = "G aug"
    chord_code = "X022XX"; chord_name = "A5"
    
    
    
    html_output = generate_full_html(chord_code, chord_name)
    filename = sanitize_filename(chord_name)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_output)

    print(f"✅ Generated: {filename}")

if __name__ == "__main__":
    main()
    