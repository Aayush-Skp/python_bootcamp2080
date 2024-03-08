import cv2 as cv
import os

def capture_images_from_folder(output_dir):
    input_folder = input("Select the directory containing colored sample images: ")
    person_name = input("Enter the name of the person: ")

    if not os.path.exists(input_folder):
        print("Error: Input folder does not exist.")
        return

    os.makedirs(output_dir, exist_ok=True)

    person_dir = os.path.join(output_dir, person_name)
    os.makedirs(person_dir, exist_ok=True)

    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

    samples_count = 0

    for filename in os.listdir(input_folder):
        img_path = os.path.join(input_folder, filename)
        img = cv.imread(img_path)

        gray_frame = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            samples_count += 1

            face_image_filename = os.path.join(person_dir, f'{samples_count}.jpg')
            cv.imwrite(face_image_filename, gray_frame[y:y+h, x:x+w])

            print(f'Sample {samples_count} saved as {face_image_filename}')

    print("Face capture from folder completed.")
