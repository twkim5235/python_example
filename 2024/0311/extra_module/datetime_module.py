from datetime import datetime, timezone, timedelta

# specific_date = datetime(2024, 3, 17, 12, 30)
# print(specific_date)
#
# datetime1 = datetime(2024, 3, 1)
# datetime2 = datetime(2024, 3, 17)
#
# difference = datetime2 - datetime1
# print(difference)

# datetime 객체를 문자열로 변경
# current_datetime = datetime.now()
# formatted_date = current_datetime.strftime("%B %d, %Y")
# print(formatted_date)
#
# 문자열 객체를 datetime 객체로 변경
# date_string = "27 February, 2024"
# datetime_object = datetime.strptime(date_string, "%d %B, %Y")
# print(datetime_object)

import pytz
# timezone = pytz.timezone('Asia/Seoul')
# localized_datetime = datetime.now(timezone)
# print(localized_datetime)

# datetime_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(datetime_now)

# current_datetime = datetime.now()
# one_week_later = current_datetime + timedelta(days=7, minutes=30)
# print(one_week_later)
