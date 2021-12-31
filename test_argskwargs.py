import argskwargs as ak


def test_function():
    assert ak.func('red', 'blue', 'yellow',
                   'chartreuse') == "red, blue, yellow, chartreuse"
    assert ak.func(link_color='red', back_color='blue') == "red, blue"
    assert ak.func('purple', link_color='red',
                   back_color='blue') == "purple, red, blue"
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert ak.func(*regular, **links) == "red, blue, chartreuse"
