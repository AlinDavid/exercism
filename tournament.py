def tally(rows):
    result = ["Team                           | MP |  W |  D |  L |  P"]

    sc = {}

    for row in rows:
        team1, team2, res = row.split(";")

        if team1 not in sc:
            sc[team1] = {"w": 0, "d": 0, "l": 0, "p": 0}
        if team2 not in sc:
            sc[team2] = {"w": 0, "d": 0, "l": 0, "p": 0}

        if res == "win":
            sc[team1]["w"] += 1
            sc[team2]["l"] += 1
        elif res == "loss":
            sc[team1]["l"] += 1
            sc[team2]["w"] += 1
        elif res == "draw":
            sc[team1]["d"] += 1
            sc[team2]["d"] += 1

        sc[team1]["p"] += 1
        sc[team2]["p"] += 1

    for k in sorted(
            sc.keys(),
            key=lambda k_points: (-(sc[k_points]["w"] * 3 + sc[k_points]["d"] * 1), -sc[k_points]["p"], k_points)
    ):
        v = sc[k]
        result.append(
            f"{k: <30} | {v['p']: >2} | {v['w']: >2} | {v['d']: >2} | {v['l']: >2} | {v['w'] * 3 + v['d'] * 1: >2}"
        )

    return result



