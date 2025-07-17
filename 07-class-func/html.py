def tag(name, *content, class_=None, **attrs):
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {name}=\'{value}\'' for name, value in attrs.items())
    attr_str = ''.join(attr_pairs)
    if content is not None and len(content) > 0:
        elements = []
        for c in content:
            if isinstance(c, list):
                for e in c:
                    if e is not None:
                        elements.append(f'<{name}{attr_str}>{e}</{name}>')
                    else:
                        elements.append(f'<{name}{attr_str}/>')
                continue
            if c is not None:
                elements.append(f'<{name}{attr_str}>{c}</{name}>')
            else:
                elements.append(f'<{name}{attr_str}/>')
        return '\n'.join(elements)
    return f'<{name}{attr_str}/>'


def tag2(*, name, content, class_=None, **attrs):
    return tag(name, content, class_=class_, **attrs)


print(tag('br'))
print(tag('div', 'hello'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', class_='sidebar'))
print(tag(content='testing', name="img"))

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class': 'framed'}
print(tag(**my_tag))
print('-' * 20)

print(tag2(name='br', content=''))
print(tag2(name='div', content='hello'))
print(tag2(name='p', content='hello', id=33))
print(tag2(name='p', content=['hello', "world"], class_='sidebar'))
print(tag2(content='testing', name="img"))
