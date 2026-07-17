def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        schedule = schedules[i]

        hour = schedule // 100
        minute = schedule % 100

        minute += 10

        if minute >= 60:
            hour += 1
            minute -= 60

        deadline = hour * 100 + minute

        is_late = False  # 지각 여부 정보 변수

        for day_index in range(7):
            day = startday + day_index

            if day > 7:
                day -=7

            if day != 6 and day != 7:
                if timelogs[i][day_index] > deadline:
                    is_late = True
                    break

        if is_late == False:
            answer += 1

    return answer
