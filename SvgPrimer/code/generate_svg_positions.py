def generate_svg_positions(chord_code, chord_name=""):
    """
    Convert 6-char chord string to SVG elements with a top label.
    chord_code = string 6 to string 1: 'X02220'
    chord_name = optional label shown above the diagram.
    """
    svg = ['<!-- inject:positions -->', '<!-- START positions -->']
    string_spacing = 30
    fret_spacing = 40

    # Add chord name label
    if chord_name:
        svg.append(f'<text class="fret-label" x="85" y="-2">{chord_name}</text>')

    for i, fret in enumerate(chord_code):
        x = 10 + i * string_spacing  # left to right: string 6 → string 1
        if fret.upper() == 'X':
            svg.append(f'<text class="string-muted" x="{x}" y="5">X</text>')
        elif fret == '0':
            svg.append(f'<text class="fret-label" x="{x}" y="5">0</text>')
        elif fret.isdigit():
            y = int(fret) * fret_spacing
            svg.append(f'<circle class="dot-active" cx="{x}" cy="{y}" r="6" />')
            # No fret label for fretted notes
        else:
            svg.append(f'<!-- Invalid input on string {6 - i}: {fret} -->')

    svg.append('<!-- END positions -->')
    return '\n'.join(svg)


def main():
    chord_code = "X02220"; chord_name = "A Major" 
    chord_code = "X32010"; chord_name = "C Major"  
    svg_output = generate_svg_positions(chord_code, chord_name)
    print(svg_output)


if __name__ == "__main__":
    main()