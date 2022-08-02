import sys
room = int(sys.stdin.readline())
pass_room = 1
a = 0
present_floor = 1
Next_floor = 1
if room == 1:
    print(f'{pass_room}')
else:
    while True:
        pass_room += 1
        a += 6
        Next_floor += a
        if present_floor < room and room <= Next_floor:
            print(f'{pass_room}')
            break
        present_floor = Next_floor
        

    # break는 while문을 빠저 나갑니다.
# print(f'{pass_room}')