from remove_html_markup import remove_html_markup

assert remove_html_markup("Here's some <strong>strong argument</strong>.") == \
    "Here's some strong argument."

assert remove_html_markup('<input type="text" value="<your name>">') == ""

assert remove_html_markup('<b>foo</b>') == 'foo'

assert remove_html_markup('<b>"foo"</b>') == '"foo"'

assert remove_html_markup('<"b">foo</"b">') == 'foo'


