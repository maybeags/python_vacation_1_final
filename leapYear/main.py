'''
주어진 해가 윤년인지 아닌지를 계산하는 프로그램을 작성하세요. 일반적으로 1년은 365일이고,
윤년은 366일로 2월에 하루가 더 있습니다.

다음은 특정 연도가 윤년인지 확인하는 방법입니다.

1. 4로 나누어 떨어지는 해는 윤년입니다.
2. 그러나, 100으로 나누어 떨어지는 해는 윤년이 아닙니다.
3. 그런데, 400으로 나누어 떨어지는 해는 윤년입니다.

ex)

2000 / 4 = 500 (윤년)
2000 / 100 = 20 (윤년 아님)
2000 / 400 = 5 (윤년)

따라서 2000년은 윤년입니다.

2100 / 4 = 525 (윤년)
2100 / 100 = 21 (윤년 아님)
2100 / 400 = 5.25 (윤년 아님)

따라서 2100년은 윤년이 아닙니다.
'''

def is_leap_year(year):
    if year % 400 == 0:
        return f"{year}년은 윤년입니다."
    elif year % 100 == 0:
        return f"{year}년은 윤년이 아닙니다."
    elif year % 4 == 0:
        return f"{year}년은 윤년입니다."

def is_leap_year2(year):
    if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
        return f"{year}는 윤년입니다."
    else:
        return f"{year}는 윤년이 아닙니다."

year = int(input("년도를 입력하세요 >>> "))
print(is_leap_year2(year))















