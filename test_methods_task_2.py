import pytest
from lesson14_task_2 import Tree

tree = Tree(10)

def test_add_nodes_from_lst_T():
    tree.add_nodes_from_lst([10, 4, 18, 2, 31])
    assert tree.check_node(10) and tree.check_node(4) and tree.check_node(18) and tree.check_node(2)\
           and tree.check_node(31) is True

def test_min_value_node_T():
    assert tree.min_value_node() == 2

def test_min_value_node():
    assert tree.min_value_node() != 1

def test_max_value_node_T():
    assert tree.max_value_node() == 31

def test_max_value_node():
    assert tree.max_value_node() != 30

def test_del_node():
    tree.delete_node(4)
    assert tree.check_node(4) is False

def test_insert():
    tree.insert(30)
    assert tree.check_node(30) is True


