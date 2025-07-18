def generate_chord_svg_block(chord_id, chord_name, string_map):
    """
    chord_id: string, e.g. 'a-major'
    chord_name: string, e.g. 'A Major'
    string_map: list of 6 values from low E to high e, e.g. ['X', 0, 2, 2, 2, 0]
    """
    string_labels = ['E', 'A', 'D', 'G', 'B', 'e']
    x_positions = [20, 60, 100, 140, 180, 220]
    y_nut = 10
    y_fret_base = 70
    fret_spacing = 40
    marker_radius = 6

    lines = [f'<g id="{chord_id}">']
    lines.append(f'  <desc>\n    Chord: {chord_name}')

    # Add string labels to <desc>
    for label, value in zip(string_labels, string_map):
        lines.append(f'    {label} - {value}')
    lines.append('  </desc>\n')

    # Above nut markers
    for i, value in enumerate(string_map):
        x = x_positions[i]
        if value == 'X':
            marker = 'X'
        elif value == 0:
            marker = 'O'
        elif isinstance(value, int) and value > 0:
            marker = '●'
        else:
            continue  # skip invalid
        lines.append(f'  <text x="{x}" y="{y_nut}" font-size="12" fill="white" text-anchor="middle">{marker}</text>')

    # Finger markers
    for i, value in enumerate(string_map):
        if isinstance(value, int) and value > 0:
            x = x_positions[i]
            y = y_fret_base + (value - 1) * fret_spacing + fret_spacing // 2  # midpoint between frets
            lines.append(f'  <circle cx="{x}" cy="{y}" r="{marker_radius}" fill="red" />')

    lines.append('</g>')
    return '\n'.join(lines)