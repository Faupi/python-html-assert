import re


class ElementDef(object):
    """ An element we want to match, specifying the name, content, attributes and children we want to assert. """

    def __init__(self, name_regex, *children, **attrs):
        self.name_regex = name_regex
        self.name_matcher = re.compile(name_regex)
        self.r_name = attrs.pop('r_name', None)
        self.parent = None
        self.children = [child for child in children if child]
        self.attrs = attrs
        self.content = self._keyword_attr('content')

        self._init_child_parents()
        self._handle_escaped_attrs()

    def _keyword_attr(self, attr_name):
        if attr_name in self.attrs:
            attr_value = self.attrs[attr_name]
            del self.attrs[attr_name]
        else:
            attr_value = None
        return attr_value

    def _init_child_parents(self):
        for child in self.children:
            child.parent = self

    def _handle_escaped_attrs(self):
        new_attrs={}
        for key, value in self.attrs.items():
            if key.endswith('_'):
                new_attrs[key.replace('_', '')] = value
            else:
                new_attrs[key] = value
        self.attrs = new_attrs

    def __repr__(self):
        return 'ElementMatcher[name_regex={0},content={1},attrs={2}]'.format(self.name_regex, self.content, self.attrs)

    def __str__(self):
        name = self.name_regex[1:-1]
        elem_def = '<{0}'.format(name)
        for key, value in self.attrs.items():
            elem_def += ' {0}="{1}"'.format(key, value)
        if self.content:
            elem_def += '>{0}</{1}>'.format(self.content, name)
        else:
            elem_def += '/>'

        return elem_def


def elem(name: str, *children, **attrs):
    elem_regex = r'^{0}$'.format(name)
    return ElementDef(elem_regex, *children, **attrs)


def html(*children, **attrs):
    return ElementDef(r'^html$', *children, **attrs)


def heading(heading_text: str, *children, **attrs):
    attrs['content'] = heading_text
    return ElementDef(r'^(h1|h2|h3|h4|h5|h6)$', *children, **attrs)


def text(text_content: str, *children, **attrs):
    attrs['content'] = text_content.replace("\n", "\\n")
    return ElementDef(r'^.*$', *children, **attrs)


def a(href=None, link_text=None, *children, **attrs):
    if href:
        attrs['href'] = href
    if link_text:
        attrs['content'] = link_text
    return ElementDef(r'^a$', *children, **attrs)


def accordion(*children, **attrs):
    attrs['class_'] = 'accordion'
    return div(*children, **attrs)


def acc_group(*children, **attrs):
    attrs['class_'] = 'accordion-group'
    return div(*children, **attrs)


def acc_heading(*children, **attrs):
    attrs['class_'] = 'accordion-heading'
    return div(*children, **attrs)


def acc_body(*children, **attrs):
    attrs['class_'] = 'accordion-body'
    return div(*children, **attrs)


def div(*children, **attrs):
    return ElementDef(r'^div$', *children, **attrs)


def input(id, value=None, *children, **attrs):
    attrs['id'] = id
    if value:
        attrs['value'] = value
    return ElementDef(r'^input$', *children, **attrs)


def select(id, *children, **attrs):
    attrs['id'] = id
    return ElementDef(r'^select$', *children, **attrs)


def option(value, content=None, selected=False, *children, **attrs):
    attrs['value'] = value
    if content:
        attrs['content'] = content
    if selected:
        attrs['selected'] = ''
    return ElementDef(r'^option$', *children, **attrs)


def option_xhtml(value, content=None, selected=False, *children, **attrs):
    attrs['value'] = value
    if content:
        attrs['content'] = content
    if selected:
        attrs['selected'] = 'selected'
    return ElementDef(r'^option$', *children, **attrs)


def img(src, *children, **attrs):
    attrs['src'] = src
    return ElementDef(r'^img$', *children, **attrs)
