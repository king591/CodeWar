def tp_bet_counting(bot_amount: int, players: int, pla_pos: int):
    chaal_limit = bot_amount * 128
    pot_limit = bot_amount * 1024
    print(bot_amount, chaal_limit, pot_limit, players)
    max_round = 10
    pot_players = [bot_amount] * players
    ante = bot_amount
    for r in range(1, max_round + 1):
        for p in range(players):
            if ante < chaal_limit:
                pot_players[p] = pot_players[p] + ante * 2
                ante = ante * 2
                if sum(pot_players) >= pot_limit:
                    return r, pot_players
            else:
                pot_players[p] = pot_players[p] + chaal_limit
                if sum(pot_players) >= pot_limit:
                    return r, p+1, pot_players, max(pot_players)


print(tp_bet_counting(1, 2, 1))
print(tp_bet_counting(1, 3, 1))
print(tp_bet_counting(1, 4, 1))
print(tp_bet_counting(1, 5, 1))
