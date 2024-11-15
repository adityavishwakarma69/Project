import pyaudio
import pygame
from pygame.locals import *
import numpy as np

# Constants
FORMAT = pyaudio.paInt16  # Sample format
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sampling rate in Hz
CHUNK = 1024  # Number of frames per buffer

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Listening...")


screen = pygame.display.set_mode((500, 500))

follow = 0

try:
    while True:
        # Read chunk of audio data from the stream
        data = stream.read(CHUNK)

        numpy_data = np.frombuffer(data, dtype=np.int16)
        
        average_amplitude = np.mean(np.abs(numpy_data))

        follow += (average_amplitude - follow)//5

        for event in pygame.event.get():
            if event.type == QUIT:
                stream.stop_stream()
                stream.close()
                audio.terminate()
                pygame.quit()
                exit()

        screen.fill((0, 0, 0))

        for i in range(5, 10):
            pygame.draw.circle(screen, (255, 0, 0), (250, 250), (follow//5) - i *10, 2)


        pygame.display.flip()
        
        # Process audio data here
        # For example, you can perform real-time audio analysis or apply audio effects
        
except KeyboardInterrupt:
    # Stop stream
    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("Stream stopped")

