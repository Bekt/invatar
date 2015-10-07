
defaults = {
    'size': 100,
    'font_size': 60,
    'font_family': 'Arial',
    'bg': 'black',
    'color': 'white',
    'text': 'KB'
}


def make_svg(**options):
    """Builds a simple SVG text square with a centered text.

    options: size, font_size, font_family, bg, color, text

    :return (str)
    """
    if options is not None and not isinstance(options, dict):
        raise ValueError('options should be None or a type of dict.')

    if 'size' in options and 'font_size' not in options:
        options['font_size'] = int(options['size'] * 0.6)

    dc = defaults.copy()
    dc.update(options)
    options = dc

    svg = """
    <svg xmlns="http://www.w3.org/2000/svg"
         width="{size}px" height="{size}px">
      <g>
        <rect x="0" y="0" fill="{bg}" width="{size}px" height="{size}px">
        </rect>
        <text y="50%" x="50%" fill="{color}"
              text-anchor="middle" dominant-baseline="central"
              style="font-family: {font_family}; font-size: {font_size}px">
          {text}
        </text>
      </g>
    </svg>
    """.format(**options)

    return svg
