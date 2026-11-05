POINTS = {'0': 0, '15': 1, '30': 2, '40': 3}


def parse_score(text):
    """Parse 'A-B' into (a, b). Return None for any invalid input."""
    if not isinstance(text, str):
        return None
    parts = text.split('-')
    if len(parts) != 2:
        return None
    try:
        return int(parts[0]), int(parts[1])
    except ValueError:
        return None


def game_lead(text):
    """Return A's lead in points for a score like '40-30'. None if invalid."""
    if not isinstance(text, str):
        return None
    parts = text.split('-')
    if len(parts) != 2 or parts[0] not in POINTS or parts[1] not in POINTS:
        return None
    return POINTS[parts[0]] - POINTS[parts[1]]


def set_spread(games_csv):
    """Return max - min of comma-separated game counts. None if invalid."""
    if not isinstance(games_csv, str):
        return None
    try:
        games = [int(g) for g in games_csv.split(',')]
    except ValueError:
        return None
    return max(games) - min(games)


def main():
    print("==== Running parse_score ====")
    user_input = input("Enter points won as A-B (e.g. 3-2): ")
    result = parse_score(user_input)
    if result is None:
        print("Invalid input: expected two integers like 3-2")
    else:
        print("Points A and B:", result)

    print("\n==== Running game_lead ====")
    user_input = input("Enter a game score (e.g. 40-30): ")
    result = game_lead(user_input)
    if result is None:
        print("Invalid input: use 0, 15, 30 or 40 on each side, e.g. 40-30")
    else:
        print("Lead in Points:", result)

    print("\n==== Running set_spread ====")
    user_input = input("Enter games won per set as CSV (e.g. 6,4,7): ")
    result = set_spread(user_input)
    if result is None:
        print("Invalid input: expected comma-separated integers like 6,4,7")
    else:
        print("Spread:", result)


if __name__ == "__main__":
    main()
