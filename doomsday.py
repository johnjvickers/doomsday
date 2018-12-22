import random as rnd
import time
import datetime
import sys

def get_date():
    year = rnd.randint(1950, 2050)

    month = rnd.randint(1, 12)

    if month == 2:
        if year % 4 == 0:
            day = rnd.randint(1, 29)
        else:
            day = rnd.randint(1, 28)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        day = rnd.randint(1, 31)
    else:
        day = rnd.randint(1, 30)

    # print(str(day) + ' ' + month + str(year))
    return(year, month, day)

def run_game():
    read_months = [
        'buffer', 'january', 'february', 'march', 'april', 'may', 'june',
         'july', 'august', 'september', 'october', 'november', 'december'
    ]
    read_days = [
        'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday'
    ]

    date = get_date()

    print(str(date[2]) + ' ' + read_months[date[1]] + ' ' + str(date[0]))

    t0 = time.time()

    weekday = datetime.date(date[0], date[1], date[2]).weekday()+1
    if weekday == 7:
        weekday = 0
        
    guess = input('Your guess: ')

    t1 = time.time() - t0

    outfile = open('doomsday.csv', 'a')

    if int(guess) == weekday:
        print("correct! " + read_days[weekday] + ' (' + str(t1) + ' seconds)')
        outfile.write('1,'+str(t1)+'\n')
    else:
        print("incorrect! " + read_days[weekday] + ' (' + str(t1) + ' seconds)')
        outfile.write('0,'+str(t1)+'\n')

def run_stats():

    #try:
    corrs, times = [], []
    for line in open('doomsday.csv'):
        corrs.append(float(line.partition(',')[0]))
        times.append(float(line.partition(',')[2].partition('\n')[0]))

    if len(corrs) < 10:
        print('need more results for stats')
    else:
        per_all = round(float(sum(corrs)/len(corrs)), 2)*100
        tim_all = round(sum(times)/len(times), 1)
        corrs, times = corrs[-10:], times[-10:]
        per_cur = round(sum(corrs)/len(corrs), 2)*100
        tim_cur = round(sum(times)/len(times), 1)
        
    print('last 10: ' + str(per_cur) + '% vs. all: ' + str(per_all) + '%')
    print('last 10: ' + str(tim_cur) + 's vs. all: ' + str(tim_all) + 's')
            
            
    #except:
    #    print('no doomsday.csv to read')
        
if __name__ == '__main__':

    try:
        sys.argv[1] == 'stats'
        run_stats()
    except:
        run_game()

