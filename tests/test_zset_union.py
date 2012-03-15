from tests import IntegerZSetTestCase


class TestIntegerZSet(IntegerZSetTestCase):
    def test_union(self):
        self.zset.add(1, 1)
        union = self.zset.union([(2, 2.0), (3, 3.0)])
        assert union == set([(1, 1.0), (2, 2.0), (3, 3.0)])

    def test_or_operator(self):
        self.zset.add(1, 1)
        union = self.zset | set([(2, 2.0), (3, 3.0)])
        assert union == set([(1, 1.0), (2, 2.0), (3, 3.0)])

    def test_update(self):
        self.zset.add(1, 1)
        self.zset.update(set([(2, 2.0), (3, 3.0)]))
        assert self.zset.data == [(1, 1.0), (2, 2.0), (3, 3.0)]

    def test_or_assignment_operator(self):
        self.zset.add(1, 1)
        self.zset |= set([(2, 2.0), (3, 3.0)])
        assert self.zset.data == [(1, 1.0), (2, 2.0), (3, 3.0)]
