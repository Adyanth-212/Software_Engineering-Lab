from hypothesis import given, strategies as st
from tennis_scoring import parse_score, game_lead, set_spread


@given(st.text() | st.none())
def test_parse_score_no_crash(s):
    try:
        parse_score(s)
    except Exception as e:
        assert False, f"parse_score crashed with: {e!r}"


@given(st.text() | st.none())
def test_game_lead_no_crash(s):
    try:
        game_lead(s)
    except Exception as e:
        assert False, f"game_lead crashed with: {e!r}"


@given(st.text() | st.none())
def test_set_spread_no_crash(s):
    try:
        set_spread(s)
    except Exception as e:
        assert False, f"set_spread crashed with: {e!r}"


# Extra properties: valid inputs must give correct results
@given(st.integers(min_value=0), st.integers(min_value=0))
def test_parse_score_valid(a, b):
    assert parse_score(f"{a}-{b}") == (a, b)


@given(st.sampled_from(["0", "15", "30", "40"]), st.sampled_from(["0", "15", "30", "40"]))
def test_game_lead_valid(x, y):
    order = ["0", "15", "30", "40"]
    assert game_lead(f"{x}-{y}") == order.index(x) - order.index(y)


@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_set_spread_valid(games):
    csv = ",".join(str(g) for g in games)
    assert set_spread(csv) == max(games) - min(games)
