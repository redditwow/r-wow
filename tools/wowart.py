import csv
from random import choice

users = []

with open('entries.csv', 'rb') as csvfile:
    entries = csv.reader(csvfile)
    for row in entries:
        users.append(row)

winners = []

while len(winners) < 10:
    username = choice(users)
    try:
        winner = r.get_redditor(username[0])
        winners.append(winner)
        print username[0]
    except:
        print 'BROKEN'
        print username[0]
