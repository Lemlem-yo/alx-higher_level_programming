#!/usr/bin/python3
"""A mdoule for python matix multiplication"""


def matrix_mul(m_a, m_b):
    """Matrix multiplication function"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if any(not isinstance(x, list) for x in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(x, list) for x in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for _a in m_a:
        if any(not isinstance(x, int) for x in _a):
            raise TypeError("m_a should contain only integers or floats")
    for _b in m_b:
        if any(not isinstance(x, int) for x in _b):
            raise TypeError("m_b should contain only integers or floats")
    temp = len(m_a[0])
    if any(len(_a) != temp for _a in m_a):
        raise TypeError("each row of m_a must be of the same size")
    temp = len(m_b[0])
    if any(len(_b) != temp for _b in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    if any(len(a) != len(b) for a, b in zip(m_a, m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    m_b_ = [[row[i] for row in m_b] for i in range(len(m_b[0]))]
    new_matrix = [[a * b for a, b in zip(_a, _b)] for _a, _b in zip(m_a, m_b_)]
    _sum = 0
    for _mat in new_matrix:
        for i in _mat:
            _sum += i
    return _sum
