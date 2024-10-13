# Fourier Transform (FFT) and Signal Analysis
This project demonstrates the application of the Fast Fourier Transform (FFT) to analyze and decompose complex signals into their sinusoidal components. The project showcases how to:
- Decompose combined sinusoidal signals (e.g., 50 Hz and 120 Hz) using FFT.
- Analyze motion data from video files and extract their frequency components.
- Visualize original signals, individual sinusoidal waves, and the corresponding frequency spectra.

## Key Features:
- **FFT on Synthetic Signals**: Decomposes a complex signal consisting of multiple sine waves into its individual components.
- **Video Motion Analysis**: Extracts motion data from a video file and applies FFT to understand its frequency behavior.
- **Visualization**: Plots the original signals, their decomposed components, and FFT frequency spectrum using `matplotlib`.

### Important Notes:
Threshold and Gaussian Blur Adjustments: Depending on the characteristics of the video file (e.g., resolution, noise level), the threshold value and Gaussian Blur kernel size may need to be adjusted. Lower thresholds are more sensitive to small movements, while larger blur kernel sizes can help smooth out noise in high-resolution videos.
These values can be modified in the code, specifically in the sections dealing with motion detection and preprocessing.
Install the required libraries (NumPy, Matplotlib, OpenCV)

### Functions Overview:
Example func_1: f(t)=3⋅sin(2π⋅50⋅t)+5⋅sin(2π⋅120⋅t)
This function combines a 50 Hz and a 120 Hz sinusoidal signal.

Example func_2: f(t)=2⋅sin(2π⋅30⋅t)+1.5⋅sin(2π⋅60⋅t)+1.0⋅sin(2π⋅90⋅t)+0.5⋅sin(2π⋅150⋅t)+0.8⋅sin(2π⋅200⋅t)
This function combines five sinusoidal signals with varying frequencies and amplitudes.

#### Steps:
Step 1: Run func_1.py and check the result.
Step 2: Run func_2.py and review the result.
Step 3: Run fft_motion_analysis.py, make adjustments to threshold and blur, then check the final results.
Step 4: View example motion and FFT analysis plots from the provided sample videos.

Note: Sorry for some Turkish words.
