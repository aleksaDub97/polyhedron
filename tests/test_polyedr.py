from pytest import approx
from shadow.polyedr import Polyedr
from math import sqrt


class TestPolyedr:

    def test_polyedr_1(self):
        f = Polyedr('data/test_1.geom')
        return f.get_edge_sum() == 2

    def test_polyedr_2(self):
        f = Polyedr('data/test_2.geom')
        return f.get_edge_sum() == 2

    def test_polyedr_3(self):
        f = Polyedr('data/test_3.geom')
        return f.get_edge_sum() == 0

    def test_polyedr_4(self):
        f = Polyedr('data/test_4.geom')
        return f.get_edge_sum() == 2

    # python3 -B -m pytest -p no:cacheprovider tests/test_polyedr.py
