import pytest
from DOCUMENTAIRE import Documentaire

def test_documentaire_instantiation():
    doc = Documentaire("001", "Inception", "2010-07-16")
    assert doc.getcode() == "001"
