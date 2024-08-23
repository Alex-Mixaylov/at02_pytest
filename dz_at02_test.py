import pytest
from dz_at02 import count_vowels

def test_vowels_only():
    """
    Тест проверяет, что функция корректно считает гласные в строке, содержащей только гласные.
    """
    assert count_vowels("aeiouyAEIOU") == 11  # В строке 10 гласных

def test_no_vowels():
    """
    Тест проверяет, что функция возвращает 0 для строки, не содержащей гласных.
    """
    assert count_vowels("bcdfghjklmnpqrstvwxz") == 0  # В строке нет гласных

def test_mixed_string():
    """
    Тест проверяет, что функция корректно считает гласные в смешанной строке,
    включая прописные и строчные буквы.
    """
    assert count_vowels("My name is Alex") == 6  # В строке 'My name is Alex' 6 гласных

def test_empty_string():
    """
    Тест проверяет, что функция возвращает 0 для пустой строки.
    """
    assert count_vowels("") == 0  # Пустая строка содержит 0 гласных

def test_vowels_with_special_characters():
    """
    Тест проверяет, что функция корректно считает гласные в строке, содержащей спецсимволы.
    """
    assert count_vowels("a@ei#ou!") == 5  # Спецсимволы не должны мешать подсчету гласных

