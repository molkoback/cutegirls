from datetime import datetime, timedelta

def boorutime(date_str):
	""" date_str eg. Sun Oct 22 06:10:05 +0200 2017 """
	return datetime.strptime(date_str[4:], "%b %d %H:%M:%S %z %Y")
