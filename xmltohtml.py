#!/usr/bin/python3
import xml.etree.ElementTree as ET
from typing import Dict, NewType

class Tag():
  def __init__(self, _parent, _name: str = "div", _attr: Dict = dict()):
    self.indent = 0 if _parent == None else _parent.indent + 1
    self.name = _name
    self.attr = _attr

  def __enter__(self):
    print( '  ' * self.indent, end='' )
    print( f'<{self.name}', end='' )
    for attr in self.attr.keys():
      print( f' {attr}="{self.attr[ attr ]}"', end='' )
    print( '>' )
    return self

  def __exit__(self, type, value, traceback):
    print( '  ' * self.indent, end='' )
    print( f'</{self.name}>' )

  def content(self, contentText):
    print( '  ' * (self.indent + 1), end='' )
    print( contentText )

def basic_fmt_text( t ):
  return ' '.join( t.text.lstrip().rstrip().split() )

def main():
  root = ET.parse('answer.xml').getroot()
  with Tag( None, 'html', { 'lang': 'ru-RU' } ) as html:
    with Tag( html, 'head', {} ) as head:
      with Tag( head, 'title', {} ) as title:
        title.content( 'Компьютерные сети. Тест 2' )
    
    with Tag( html, 'body', {} ) as body:
      with Tag( body, 'div', {} ) as header:
        with Tag( header, 'h1', {} ) as header_h1:
          header_h1.content( 'Компьютерные сети. Тест 2' )

      for question in root.findall( 'test_question' ):
        with Tag( header, 'div', {} ) as q_div:
          with Tag( q_div, 'h2', {} ) as q_div_h2:
            text = basic_fmt_text( question.find( 'question' ) )
            q_div_h2.content( text )
          
          with Tag( q_div, 'div', {} ) as q_div_body:
            with Tag( q_div_body, 'ul', {} ) as q_list:
              for variant in question.findall( 'answer_variant' ):
                weightTag = variant.find( 'weight' )
                color = 'green' if basic_fmt_text( weightTag ) == '+1' else 'red' 
                with Tag( q_list, 'li', { 'style': f'color: {color}'} ) as q_list_item:
                  textTag = variant.find( 'text' )
                  q_list_item.content( basic_fmt_text( textTag ) )

if __name__ == '__main__':
  main()