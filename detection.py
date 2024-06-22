from attendance import present_marked
import cv2
import pandas as pd

def detector():
    def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
            id, pred = clf.predict(gray_image[y:y+h, x:x+w])
            confidence = int(100 * (1 - pred/300))

            attendance_df = pd.read_excel('attendance.xlsx')

            if confidence > 80:
                for index, row in attendance_df.iterrows():
                    d = row['ID']
                    name = row['Name']

                    if id == d:
                        cv2.putText(img, name, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
                        present_marked(id)
                        return name

            else:
                cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

    def recognize(img, clf, faceCascade):
        name = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
        return name, img

    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, img = video_capture.read()
        name, img = recognize(img, clf, faceCascade)
        cv2.imshow("Face detection", img)

        if cv2.waitKey(1) == 13:
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return name


