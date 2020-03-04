from server.sudoku_check import check_shape_contents,\
                                check_segment,\
                                preprocess,\
                                stack_squares,\
                                sudoku_check
from json import load
import numpy as np

pass_row = np.array([1,3,4,2,5,7,6,9,8])
fail_row = np.array([1,1,2,5,4,6,2,3,6])

pass_data = [\
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

fail_shape = [\
        '912468753',
        '867135492',
        '435279168',
        '784952631',
        '629317845',
        '153684279',
        '598726314',
        '271543986']

fail_shape_2 = [\
    '912468753',
    '867135492',
    '435279168',
    '784952631',
    '629317845',
    '15368429',
    '598726314',
    '346891527',
    '271543986']

fail_contents = [\
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
    fail_data = load(fl_in)

def test_check_shape_contents():
    for errortype in fail_data:
        for test in fail_data[errortype]:
            assert check_shape_contents(fail_data[errortype][test])
    
    assert not check_shape_contents(fail_shape)
    assert not check_shape_contents(fail_shape_2)
    assert not check_shape_contents(fail_contents)

def test_preprocess():
    result=preprocess(pass_data)
    assert type(result).__module__ == np.__name__
    assert result.shape == (9,9)

def test_stack_squares():
    result = preprocess(pass_data)
    result_squares = preprocess(pass_data_squares)
    result=stack_squares(result)
    np.testing.assert_array_equal(result, result_squares)

def test_check_segment():
    assert check_segment(pass_row)
    assert not check_segment(fail_row)

def test_sudoku_check():
    for errortype in fail_data:
        for test in fail_data[errortype]:
            assert not sudoku_check(fail_data[errortype][test])

    assert not sudoku_check(fail_contents)
    
    assert sudoku_check(pass_data)
