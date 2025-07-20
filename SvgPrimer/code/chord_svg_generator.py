def generate_full_svg(chord):
    """
    chord: dict with keys 'name' and 'fingering'
    Returns a complete <svg> block with title and chord markers
    """
    chord_name = chord['name']
    string_map = chord['fingering']

    string_labels = ['E', 'A', 'D', 'G', 'B', 'e']
    x_positions = [20, 60, 100, 140, 180, 220]
    y_nut = 10
    y_fret_1 = 30
    fret_spacing = 40
    marker_radius = 6

    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="250" viewBox="0 0 240 250">',
        f'  <title>{chord_name} Chord Diagram</title>',
        f'  <desc>',
        f'    Chord: {chord_name}'
    ]
    for label, value in zip(string_labels, string_map):
        lines.append(f'    {label} - {value}')
    lines.append('  </desc>\n')

    # Nut markers (above strings)
    for i, value in enumerate(string_map):
        x = x_positions[i]
        if value == 'X':
            marker = 'X'
        elif value == 0:
            marker = 'O'
        elif isinstance(value, int) and value > 0:
            marker = '●'
        else:
            continue
        lines.append(f'  <text x="{x}" y="{y_nut}" font-size="12" fill="white" text-anchor="middle">{marker}</text>')

    # Finger dots
    for i, value in enumerate(string_map):
        if isinstance(value, int) and value > 0:
            x = x_positions[i]
            y = y_fret_1 + (value - 1) * fret_spacing + (fret_spacing // 2)
            lines.append(f'  <circle cx="{x}" cy="{y}" r="{marker_radius}" fill="red" />')

    lines.append('</svg>')
    return '\n'.join(lines)


def main():
    chord = {
        'name': 'A Major',
        'fingering': ['X', 0, 2, 2, 2, 0]
    }
    svg_content = generate_full_svg(chord)
    print(svg_content)


if __name__ == "__main__":
    main()