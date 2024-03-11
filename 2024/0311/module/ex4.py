import sys

sys.path.append('../../0306/ch03')
import custom_lambda # 이곳에 코드를 작성하세요.


rides = '''와일드 윙: 110cm 이상
드림보트: 120cm 이상
자이안트 루프: 120cm 이상
툼 오브 호러: -
플라이벤처: 140cm~195cm
회전목마: 100cm 이상
매직 붕붕카: 110cm~140cm'''


def allowedrides(height):
    assert type(height) == int

    result = []

    for ride in rides.splitlines():
        ride_name, cm_min, cm_max = custom_lambda.read_rider(ride)
        if (not cm_min and not cm_max) or (cm_min <= height and not cm_max) or (cm_min <= height <= cm_max):
            result.append(ride_name)

    return result


if __name__ == "__main__":
    height = int(input())
    # 이곳에 코드를 작성하세요.
    result = allowedrides(height)

    for r in result:
        print(r)
