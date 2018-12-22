A command line game for guessing the day of the week for any given day/month/year (right now coded for 1950-2050, but easily changed). The game automatically stores the time to make the guess and the result (1 for correct, 0 for incorrect), and can give you quick stats on your improvement with the appropriate kwarg. For instructions on how to play, please see: https://en.wikipedia.org/wiki/Doomsday_rule (the guesses, as suggested in the article, are Sunday (0-day), Monday (1-day), Tuesday (2-day) ... etc.).

    $ python doomsday.py stats
    last 10: 90.0% vs. all: 92.0%
    last 10: 14.3s vs. all: 17.5s

    $ python doomsday.py
    23 may 2035
    your guess: 3
    correct! wednesday (17.84066605567932 seconds)

    $ python doomsday.py stats
    last 10: 90.0% vs. all: 93.0%
    last 10: 14.5s vs. all: 17.5s
