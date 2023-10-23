# -*- coding: utf-8 -*-
"""Pruebas calculadora AVANZADA"""

import unittest
from unittest import mock
from src.proyecto.funciones import hello_world, super,  super_hello_world, super_super_hello_world, super_super_whatever, whatever


class TestFunciones(unittest.TestCase):
    """Test Ejemplo TDD"""
    def test_hello_world(self):
        """Test hello_world"""
        self.assertEqual(hello_world(), 'hello world')
    def test_super(self):
        """Test super"""
        self.assertEqual(super(), 'super ')


    @mock.patch("src.proyecto.funciones.hello_world")
    @mock.patch("src.proyecto.funciones.super")
    def test_super_hello_world(self, mock_super, mock_hello):
        """Test super_hello_world"""
        mock_super.return_value = "No Super "
        mock_hello.return_value = "Hello World"
        res_real = super_hello_world()
        self.assertEqual(res_real, 'super hello world')

    @mock.patch("src.proyecto.funciones.hello_world")
    @mock.patch("src.proyecto.funciones.super", side_effect=["super ", "no super "])
    def test_super_super_hello_world(self, _, mock_hello):
        """Test super_super_hello_world"""
        mock_hello.return_value = "Hello World"
        res_real = super_super_hello_world()
        self.assertEqual(res_real, 'super super hello world')

    @mock.patch("src.proyecto.funciones.whatever")
    @mock.patch("src.proyecto.funciones.super", side_effect=["super ", "no super "])
    def super_super_whatever(self, _, mock_whatever):
        """Test super_super_hello_world"""
        mock_whatever.return_value = "fail"
        res_real = super_super_hello_world()
        self.assertEqual(res_real, 'super super fail')


if __name__ == '__main__':
    unittest.main()
