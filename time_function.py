from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

# start_dt = date(2015, 12, 20)
# end_dt = date(2019, 2, 9)


# for dt in list(daterange(start_dt, end_dt))[0::7]:
# 	eow = dt + timedelta(days=6)
# 	bow = dt.strftime("%Y-%m-%d")
# 	# print(bow, eow)


