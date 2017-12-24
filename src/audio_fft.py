import pyaudio
import wave
import numpy as np
from matplotlib import pyplot as plot
import time

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 8192
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

if __name__=="__main__":
    audio = pyaudio.PyAudio()







    plot.show()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)
    print "recording..."
    frames = []



    for iter in range(1000):
        data = stream.read(CHUNK, exception_on_overflow=False)
        # Plot fft of signal
        # Obtaining FFT

        numArray = np.fromstring(data, '<i2')
        freq_list = np.fft.fft(numArray)
        p = 20 * np.log10(np.abs(freq_list.real))
        f = np.linspace(0, RATE / 2, len(p)/2)
        pHalf = p[1:len(p)/2 + 1]
        plot.plot(f, pHalf)
        plot.draw()
        plot.pause(0.05)
        plot.clf()



    stream.stop_stream()
    # stop Recording
    stream.close()
    audio.terminate()


    '''
    # Save audio to file
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    '''