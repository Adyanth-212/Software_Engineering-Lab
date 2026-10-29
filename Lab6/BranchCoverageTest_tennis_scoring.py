import pytest
from tennis_scoring import game_score, set_winner, match_status


# Example test cases
def test_game_start():
    assert game_score(0, 0) == "0-0"


def test_set_undecided():
    assert set_winner(3, 2) is None


# --- game_score: both outcomes of every decision ---
def test_game_negative_a():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_game_negative_b():
    with pytest.raises(ValueError):
        game_score(0, -1)


@pytest.mark.parametrize("a,b,expected", [
    (3, 3, "deuce"),
    (4, 4, "deuce"),
    (5, 3, "game A"),
    (3, 5, "game B"),
    (4, 3, "advantage A"),
    (3, 4, "advantage B"),
    (4, 1, "game A"),
    (2, 4, "game B"),
    (3, 0, "40-0"),
    (0, 3, "0-40"),
    (3, 2, "40-30"),
    (2, 3, "30-40"),
    (1, 2, "15-30"),
    (4, 0, "game A"),
    (0, 4, "game B"),
])
def test_game_score_table(a, b, expected):
    assert game_score(a, b) == expected


# --- set_winner ---
@pytest.mark.parametrize("a,b,expected", [
    (6, 4, "A"),
    (6, 0, "A"),
    (4, 6, "B"),
    (0, 6, "B"),
    (7, 5, "A"),
    (5, 7, "B"),
    (7, 6, "A"),
    (6, 7, "B"),
    (6, 5, None),
    (5, 6, None),
    (6, 6, None),
    (3, 2, None),
])
def test_set_winner_table(a, b, expected):
    assert set_winner(a, b) == expected


# --- match_status ---
@pytest.mark.parametrize("sa,sb,bo,expected", [
    (2, 0, 3, "A wins"),
    (2, 1, 3, "A wins"),
    (0, 2, 3, "B wins"),
    (1, 2, 3, "B wins"),
    (1, 1, 3, "decider"),
    (2, 2, 5, "decider"),
    (1, 0, 3, "in progress"),
    (0, 1, 3, "in progress"),
    (0, 0, 3, "in progress"),
    (1, 2, 5, "in progress"),
])
def test_match_status_table(sa, sb, bo, expected):
    assert match_status(sa, sb, bo) == expected
