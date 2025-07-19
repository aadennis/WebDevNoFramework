def generate_svg_positions(chord_code):
    """
    Convert 6-char chord string to SVG elements.
    Each character = fret: 0–9 (open to fret), X (mute).
    Assumes string 6 (low E) to string 1 (high e), left to right.
    """
    svg = ['<!-- inject:positions -->', '<!-- START positions -->']
    string_spacing = 30
    fret_spacing = 40

    for i, fret in enumerate(chord_code):
        x = 10 + i * string_spacing  # string 6 (left) → string 1 (right)
        if fret.upper() == 'X':
            svg.append(f'<text class="string-muted" x="{x}" y="5">X</text>')
        elif fret == '0':
            svg.append(f'<text class="fret-label" x="{x}" y="5">0</text>')
        elif fret.isdigit():
            y = 10 + int(fret) * fret_spacing
            svg.append(f'<circle class="dot-active" cx="{x}" cy="{y}" r="6" />')
            svg.append(f'<text class="fret-label" x="{x}" y="{y - 5}">{fret}</text>')
        else:
            svg.append(f'<!-- Invalid input on string {6 - i}: {fret} -->')

    svg.append('<!-- END positions -->')
    return '\n'.join(svg)


def main():
    chord_code = "X02220"  # A major
    svg_output = generate_svg_positions(chord_code)
    print(svg_output)


if __name__ == "__main__":
    main()