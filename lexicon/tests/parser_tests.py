from nose.tools import *
from ex48 import parser

def test_subject():
   assert_equal(parser.peek([('verb', 'run'), ('direction', 'north')]), 'verb')
   assert_equal(parser.peek([]), None)

def test_match():
    assert_equal(parser.match([('verb', 'run'), ('direction', 'north') ], 'verb'), ('verb', 'run'))
    assert_equal(parser.match([('verb', 'run')], 'noun'), None)
    assert_equal(parser.match([], 'verb'), None)

def test_skip():
    assert_equal(parser.skip([('verb', 'stop')], 'stop'), None)

def test_parse_verbs():
    result = parser.parse_verb([('verb', 'kill'), ('stop', 'the'), ('noun', 'princess')])
    assert_equal(result, ('verb', 'kill'))
    assert_raises(parser.ParserError, parser.parse_verb, [('noun', 'princess')])

def test_parse_object():
    result = parser.parse_object([('noun', 'princess')])
    assert_equal(result, ('noun', 'princess'), 'noun')
    result2 = parser.parse_object([('direction', 'north')])
    assert_equal(result2, ('direction', 'north'))
    assert_raises(parser.ParserError, parser.parse_object, [('verb', 'go')])

def test_parse_subject():
    result = parser.parse_subject([('noun', 'princess')])
    assert_equal(result, ('noun', 'princess'), 'noun')
    result2 = parser.parse_subject([('verb', 'go')])
    assert_equal(result2, ('noun', 'player'))
    assert_raises(parser.ParserError, parser.parse_subject, [('direction', 'south')])

def test_parse_sentence():
    result = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
    assert_equal(result.subject, 'bear')
    assert_equal(result.verb, 'eat')
    assert_equal(result.object, 'honey')
