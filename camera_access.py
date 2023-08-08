import cv2

def capture_and_save_image():
    # Open the default camera (usually camera index 0)
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Camera not accessible.")
        return

    # Capture a frame from the camera
    ret, frame = camera.read()

    if not ret:
        print("Unable to capture a frame.")
        camera.release()
        return

    # Release the camera
    camera.release()

    # Ask for the user's name
    user_name = input("Enter your name: ")

    # Save the captured image with the provided name
    image_filename = f"{user_name}.jpg"
    cv2.imwrite(image_filename, frame)
    print(f"Image captured and saved as {image_filename}")

if __name__ == "__main__":
    capture_and_save_image()
