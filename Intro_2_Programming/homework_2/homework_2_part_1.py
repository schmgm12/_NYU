

def make_tags(tag_type, text):

    print('<{}>{}</{}>'.format(tag_type, text, tag_type))


make_tags('i', 'Yay')
make_tags('i', 'Hello')
make_tags('cite', 'Yay')
