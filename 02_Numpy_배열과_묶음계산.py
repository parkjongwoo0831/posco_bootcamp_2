import csv
import os
import numpy as np


def dp(name):
    """
    실행 위치가 어디든 data 폴더를 찾아주는 작은 도우미 함수

    "data/17_열처리.csv" 지금 있는 폴더 아래의 data를 뜻함.
    그래서 터미널이 어느 폴더에 서있느냐에 따라 같은 코드가 되기도 하고
    FileNotFoundError가 되기도 한다.
    폴더배치 posco_bootcamp_2/data 밑에 있음
    """
    here = os.path.dirname(os.path.abspath(__file__))
    for c in (
        os.path.join("data", name),
        os.path.join(here, "data", name),
        os.path.join(here, "..", "data", name),
    ):
        if os.path.exists(c):
            return c
    return os.path.join("data", name)


MCT = dp("10_mct_tool.csv")


# ==================================
# 0. 리스트로는 왜 안 되나 - 곱셈이 곱셈이 아닌 장면
# ==================================
# 상황) 온도 네 개를 재 뒀습니다. 전부 두배로 만들고 싶어요.

print("=" * 60)
print("[0] 리스트로 묶음 계산을 해 보면")
temps = [30, 30, 31, 29]
temps2 = [5, 6, 7, 8]

doubled = []
for t in temps:
    doubled.append(t * 2)
print(doubled)

# 같은 일을 배열로 해 봅니다.
print("[0-1] 같은 일을 배열로")
arr = np.array(temps)
arr2 = np.array(temps2)
print("배열:", arr)
print("arr*2:", arr * 2)
print("arr+5:", arr + 5)
print("화씨로 바꾸기:", arr * 1.8 + 32)
print("배열 곱 가능:", arr * arr2)

# 그럼 for로 하면 되는데 왜 Numpy 를 쓰냐?
# for 로 한 줄이 아니라 세 줄이 들었습니다.(빈 리스트 만들기 / for / append)
# 값 네 개라서 세줄이면 되는데, 40개여도 세 줄이고 400만개여도 세 줄입니다.
# 줄 수가 문제가 아닙니다. 문제는 두 가지입니다.
# 1) 하고 싶은 일(두 배로) 이 코드에 안 보입니다. 상 차리는 코드에 묻힙니다.
# 2) 느립니다. 400만개를 for로 돌리는 것과 Numpy로 하는 것은 속도가 수십배 차이 납니다.


# ==================================
# 1. 리스트와 배열은 무엇이 다른가 - 자료형이 하나로 통일됩니다.
# ==================================
