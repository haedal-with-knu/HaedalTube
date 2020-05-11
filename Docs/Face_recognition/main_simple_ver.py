import cv2

# 모델 데이터까지의 경로
frontalface_trained_xmlFile = "venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml"
# 얼굴 검출기 생성
face_detector = cv2.CascadeClassifier(frontalface_trained_xmlFile)

# 비디오 캡처 카메라 선택
# 저는 놋북 카메라가 하나라서 기본인 0으로 인자를 전달합니다.
video = cv2.VideoCapture(0)

while True:  # 무한 반복
    ret, frame = video.read()  # 화면 캡처, ret에는 캡처 성공 여부, frame에는 캡처한 결과가 담긴다.

    # 앞서 생성해둔 얼굴검출기로 얼굴을 찾아 faces 변수에 담는다.
    # 비올라 존스 알고리즘은 명암 영상을 바탕으로 작동하므로 컬러 영상을 흑백으로 바꾼다.
    # -> cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # scaleFactor와 minNeightbors 는 알고리즘과 관련된 수치. 수정하면 성능에 변화가 생긴다. 자세한 설명은 생략
    faces = face_detector.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), scaleFactor=1.08, minNeighbors=4)

    # 찾은 얼굴 각각의 좌표를 이용해 사각형으로 표시 -> cv2.rectangle
    # 표시된 곳 위에 텍스트를 써서 찾아낸 얼굴임을 표시 -> cv2.putText
    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Face', (x, y - 5), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    # 합성한 이미지를 송출
    cv2.imshow('Your Face', frame)

    # 만약 키보드로부터 입력이 있다면 반복문을 벗어난다.
    if cv2.waitKey(1) > 0:
        break

video.release()  # 비디오 캡처 객체 해제
cv2.destroyAllWindows()  # 창 닫기