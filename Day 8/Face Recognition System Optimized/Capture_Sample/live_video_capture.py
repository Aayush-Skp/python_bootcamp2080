import cv2 as cv
import os
import shutil

def capture_images_from_video(num_samples, output_dir):

    video_capture = cv.VideoCapture(0)

    samples_count = 0

    person_name = input("Enter the name of the person: ")

    person_dir = os.path.join(output_dir, person_name)
    if os.path.exists(person_dir):
        replace = input(f"A folder with the name '{person_name}' already exists. Do you want to replace its contents? (y/n): ")
        if replace.lower() == 'y':
            shutil.rmtree(person_dir)
        else:
            print("Exiting...")
            return

    os.makedirs(person_dir)

    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

    prev_time = 0

    while True:
        ret, frame = video_capture.read()
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if cv.waitKey(1) & 0xFF == ord(' ') and (cv.getTickCount() - prev_time) / cv.getTickFrequency() > 0.3:
                samples_count += 1
                face_image_filename = f'{person_dir}/{samples_count}.jpg'
                cv.imwrite(face_image_filename, gray_frame[y:y+h, x:x+w])  # Save only the face image

                print(f'Sample {samples_count}/{num_samples} saved as {face_image_filename}')

                prev_time = cv.getTickCount()

        cv.imshow('Capture Images - Press Space to Capture, ESC to Exit', frame)

        if samples_count >= num_samples:
            break
        if cv.waitKey(1) & 0xFF == 27:
            break
            
    video_capture.release()
    cv.destroyAllWindows()