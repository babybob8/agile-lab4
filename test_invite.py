import pytest
from invite import ALPHABET, generate_invite_code, join_trip


def make_trip(members=None, max_members=10):
    return {
        "code": "AB12CD",
        "members": members or ["anna"],
        "max_members": max_members,
    }


# AC1
def test_code_default_length():
    assert len(generate_invite_code()) == 6


def test_code_alphabet():
    assert all(ch in ALPHABET for ch in generate_invite_code())


def test_code_invalid_length():
    with pytest.raises(ValueError):
        generate_invite_code(2)


# AC2
def test_codes_are_unique():
    codes = {generate_invite_code() for _ in range(50)}
    assert len(codes) == 50


# AC3
def test_join_success():
    assert join_trip(make_trip(), "AB12CD", "boris") == ["anna", "boris"]


def test_join_lowercase_code():
    assert join_trip(make_trip(), " ab12cd ", "boris") == ["anna", "boris"]


# AC4
def test_join_wrong_code():
    with pytest.raises(ValueError):
        join_trip(make_trip(), "ZZZZZZ", "boris")


@pytest.mark.parametrize("bad", ["", "AB12", "AB12CD99", "AB 2CD", None, 123456])
def test_join_invalid_format(bad):
    with pytest.raises(ValueError):
        join_trip(make_trip(), bad, "boris")


# AC5
def test_join_already_member():
    with pytest.raises(ValueError):
        join_trip(make_trip(), "AB12CD", "anna")


def test_join_trip_full():
    trip = make_trip(members=["anna", "boris"], max_members=2)
    with pytest.raises(ValueError):
        join_trip(trip, "AB12CD", "clara")
