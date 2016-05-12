__author__ = 'rcarbone'
import pytest
from contacts import contacts

def test_directions():
   assert_equal(lexicon.scan("north"), [('direction', 'north')])
   result = lexicon.scan("north south east")
   assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])