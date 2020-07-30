import pytest


@pytest.fixture
def IncDecFixture():
    import kata.dummy as dummy
    return dummy.IncDec()


def test_increment(IncDecFixture):
    assert IncDecFixture.increment(3) == 3


def test_decrement(IncDecFixture):
    assert IncDecFixture.decrement(3) == -3
