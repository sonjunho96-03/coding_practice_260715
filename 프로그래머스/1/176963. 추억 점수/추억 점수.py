def solution(name, yearning, photo):
    answer = []

    # 사진 한 장씩 확인
    for one_photo in photo:
        photo_score = 0

        # 사진 속 사람 한 명씩 확인
        for person in one_photo:

            # 점수가 있는 사람이면 점수 더하기
            if person in name:
                pos = name.index(person)
                photo_score += yearning[pos]

        # 사진 한 장의 최종 점수 저장
        answer.append(photo_score)

    return answer
