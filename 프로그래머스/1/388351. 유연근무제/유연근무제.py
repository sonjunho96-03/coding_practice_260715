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

        success = True

        for j in range(7):
            day = (startday + j - 1) % 7 + 1

            if day != 6 and day != 7:
                if timelogs[i][j] > deadline:
                    success = False
                    break

        if success:
            answer += 1

    return answer