from datetime import datetime, timedelta

months = {
	"Jan": 1,
	"Feb": 2,
	"Mar": 3,
	"Apr": 4,
	"May": 5,
	"Jun": 6,
	"Jul": 7,
	"Aug": 8,
	"Sep": 9,
	"Oct": 10,
	"Nov": 11,
	"Dec": 12
}

def boorutime(date_str):
	""" date_str eg. Sun Oct 22 06:10:05 +0200 2017 """
	dl = date_str.split()
	tl = dl[3].split(":")
	
	dt = datetime(
		int(dl[5]), months[dl[1]], int(dl[2]),
		int(tl[0]), int(tl[1]), int(tl[2])
	)
	
	# Timezone
	sign = dl[4][0]
	hours = int(dl[4][1:3])
	mins = int(dl[4][3:5])
	delta = timedelta(hours=hours, minutes=mins)
	return dt-delta if sign=="+" else dt+delta
