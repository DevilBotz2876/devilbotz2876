from datetime import datetime
parsedDate = datetime.strptime('Thu, 16 Dec 2010 12:14:05', '%a, %d %b %Y %H:%M:%S')
date = parsedDate.strftime('%Y-%m-%d')
category = parsedDate.strftime('%Y')
print(date)
print(category)