'''
Checks functionality of all functions within sudoku_check.py
'''
from json import load
import numpy as np
from server.sudoku_check import check_shape_contents,\
                                check_segment,\
                                preprocess,\
                                stack_squares,\
                                sudoku_check

PASS_ROW = np.array([1, 3, 4, 2, 5, 7, 6, 9, 8])
FAIL_ROW = np.array([1, 1, 2, 5, 4, 6, 2, 3, 6])

PASS_DATA = [\
    '912468753',
    '867135492',
    '435279168',
    '784952631',
    '629317845',
    '153684279',
    '598726314',
    '346891527',
    '271543986']

pass_data_squares = [\
    '912867435',
    '468135279',
    '753492168',
    '784629153',
    '952317684',
    '631845279',
    '598346271',
    '726891543',
    '314527986']

FAIL_SHAPE = [\
        '912468753',
        '867135492',
        '435279168',
        '784952631',
        '629317845',
        '153684279',
        '598726314',
        '271543986']

FAIL_SHAPE_2 = [\
    '912468753',
    '867135492',
    '435279168',
    '784952631',
    '629317845',
    '15368429',
    '598726314',
    '346891527',
    '271543986']

FAIL_CONTENTS = [\
    '912468753',
    '867135492',
    '435279168',
    '78495a631',
    '629317845',
    '153684279',
    '598726314',
    '3e6891527',
    '271543986']

with open('testing/testdata.json', 'rt') as fl_in:
    FAIL_DATA = load(fl_in)

def test_check_shape_contents():
    '''
    Tests check_shape_contents by passing one too few rows,
    one too few items in a row, and invalide cell contents
    '''
    for errortype in FAIL_DATA:
        for test in FAIL_DATA[errortype]:
            assert check_shape_contents(FAIL_DATA[errortype][test])

    assert not check_shape_contents(FAIL_SHAPE)
    assert not check_shape_contents(FAIL_SHAPE_2)
    assert not check_shape_contents(FAIL_CONTENTS)

def test_preprocess():
    '''
    Tests to be sure that preprocess is returning a numpy array
    of shape (9, 9)
    '''
    result = preprocess(PASS_DATA)
    assert type(result).__module__ == np.__name__
    assert result.shape == (9, 9)

def test_stack_squares():
    '''
    Tests to see if the squares are being unfolded properly by
    comparing a known board to a manually unfolded board
    '''
    result = preprocess(PASS_DATA)
    result_squares = preprocess(pass_data_squares)
    result = stack_squares(result)
    np.testing.assert_array_equal(result, result_squares)

def test_check_segment():
    '''
    Tests the check_segment function by passing it good rows and bad rows
    '''
    assert check_segment(PASS_ROW)
    assert not check_segment(FAIL_ROW)

def test_sudoku_check():
    '''
    tests the concatenating function
    '''
    for errortype in FAIL_DATA:
        for test in FAIL_DATA[errortype]:
            assert not sudoku_check(FAIL_DATA[errortype][test])

    assert not sudoku_check(FAIL_CONTENTS)

    assert sudoku_check(PASS_DATA)
