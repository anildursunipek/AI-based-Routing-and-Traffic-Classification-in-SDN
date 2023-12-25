import cv2
import numpy as np

def calculate_mse_and_psnr(original_video, compressed_video):
    # Open the video files
    original_cap = cv2.VideoCapture(original_video)
    compressed_cap = cv2.VideoCapture(compressed_video)

    # Read video frames
    _, original_frame = original_cap.read()
    _, compressed_frame = compressed_cap.read()

    mse_values = []
    psnr_values = []

    while original_frame is not None and compressed_frame is not None:
        # Scale pixel values between 0-255
        original_frame = original_frame.astype(float)
        compressed_frame = compressed_frame.astype(float)

        # Calculate difference between pixel values
        difference = original_frame - compressed_frame

        # Calculate square of difference
        squared_difference = difference ** 2

        # Calculate MSE(Mean Square Error)
        mse = np.mean(squared_difference)
        mse_values.append(mse)

        # Calculate PSNR
        if mse != 0: # Eğer MSE sıfırsa PSNR sonsuza yakındır
            max_pixel_value = 255.0
            psnr = 10 * np.log10((max_pixel_value ** 2) / mse)
            psnr_values.append(psnr)

        # Read next frames
        _, original_frame = original_cap.read()
        _, compressed_frame = compressed_cap.read()

    # Calculate avarage psnr and mse values
    average_mse = np.mean(mse_values)
    average_psnr = np.mean(psnr_values)
    if(len(psnr_values) == 0):
        average_psnr = float("inf")

    # Release the video files
    original_cap.release()
    compressed_cap.release()

    return average_mse, average_psnr

if __name__ == "__main__":
    original_video_path = 'original.mp4'
    compressed_video_path = 'original-rec.mp4'

    average_mse_value, average_psnr_value = calculate_mse_and_psnr(original_video_path, compressed_video_path)
    print(f"Avarage MSE: {average_mse_value}")
    print(f"Avarage PSNR: {average_psnr_value}")