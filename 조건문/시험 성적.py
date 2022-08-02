# 문제) 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# 입력) 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 출력) 시험 성적을 출력한다.

test_score = input()

test_score = int(test_score)

if test_score <= 100 and test_score >= 90 :
    print("A")
elif test_score <= 89 and test_score >= 80 :
    print("B")
elif test_score <= 79 and test_score >= 70 :
    print("C")
elif test_score <= 69 and test_score >= 60 :
    print("D")
else:
    print("F")