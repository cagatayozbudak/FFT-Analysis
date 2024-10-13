# Fourier Transform (FFT) and Signal Analysis

This project focuses on the implementation of the Fast Fourier Transform (FFT) to analyze and decompose complex signals into their sinusoidal components. The project demonstrates how to:
- Decompose combined sinusoidal signals (e.g., 50 Hz and 120 Hz) using FFT.
- Analyze motion data from video files and extract its frequency components.
- Visualize the original signals, the individual sinusoidal waves, and their corresponding frequency spectra.

## Key Features:
- **FFT on Synthetic Signals**: Decomposes a complex signal consisting of multiple sine waves into its individual components.
- **Video Motion Analysis**: Extracts motion data from a video file and applies FFT to understand its frequency behavior.
- **Visualization**: Plots the original signals, their decomposed components, and FFT frequency spectrum using `matplotlib`.


Install the required libraries (NumPy, Matplotlib, OpenCV)

ex. func1 f(t)=3⋅sin(2π⋅50⋅t)+5⋅sin(2π⋅120⋅t)
Ex. func2 f(t)=2⋅sin(2π⋅30⋅t)+1.5⋅sin(2π⋅60⋅t)+1.0⋅sin(2π⋅90⋅t)+0.5⋅sin(2π⋅150⋅t)+0.8⋅sin(2π⋅200⋅t)
