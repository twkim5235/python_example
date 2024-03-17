from datetime import datetime, timedelta

str_time = input("날짜를 입력하세요: ")
today = datetime.strptime(str_time, "%Y %m %d")
tomorrow_date = today + timedelta(days=1)
tomorrow_date = tomorrow_date.strftime("%m/%d/%Y")

print(today.strftime("%m/%d/%Y"))
print(tomorrow_date)
