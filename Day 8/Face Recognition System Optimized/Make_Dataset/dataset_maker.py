import os
import cv2 as cv
import numpy as np
import pandas as pd

def preprocess_images_for_dataset(input_dir):
    face_samples = []  
    labels = []        
    person_names = []  

    person_id = 1 

    for person_name in os.listdir(input_dir):
        person_dir = os.path.join(input_dir, person_name)

        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_name)

            image = cv.imread(image_path)

            gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

            resized_image = cv.resize(gray_image, (100, 100))

            flattened_image = np.array(resized_image).flatten()

            face_samples.append(flattened_image)

            labels.append(person_id)

        person_names.extend([person_name] * len(os.listdir(person_dir)))

        person_id += 1

    face_samples = np.array(face_samples)
    labels = np.array(labels)

    return face_samples, labels, person_names

def main():
    input_dir = 'Capture_Sample/sample_images' 

    face_samples, labels, person_names = preprocess_images_for_dataset(input_dir)

    df = pd.DataFrame(face_samples)

    df['label'] = labels

    df['person_name'] = person_names

    df.to_csv('Make_Dataset/face_dataset.csv', index=False)

if __name__ == "__main__":
    main()