def remove_html_markup(s):
    tag = False
    out = ""

    for c in s:
        if c == '<':
            tag = True
        elif c == '>':
            tag = False
        elif not tag:
            out = out + c

    return out