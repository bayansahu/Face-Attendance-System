import cv2
def generate_dataset(id):
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    url = 'http://192.168.206.197:8080/video'
    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        if faces is ():
            return None
        for (x, y, w, h) in faces:
            cropped_face = img[y:y + h, x:x + w]
        return cropped_face

    cap = cv2.VideoCapture(url)
    img_id = 0

    while True:
        ret, frame = cap.read()
        if face_cropped(frame) is not None:
            img_id += 1
            face = cv2.resize(face_cropped(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
            cv2.imwrite(file_name_path, face)
            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("Cropped face", face)

        if cv2.waitKey(1) == 13 or int(img_id) == 200:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("collecting samples is completed............")
