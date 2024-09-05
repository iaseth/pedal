#!/usr/bin/python3
import sounddevice as sd
import scipy



SAMPLE_RATE = 44100


def main():
	seconds = 20  # Duration of recording

	print(f"Recording audio for {seconds} seconds . . .")
	my_recording = sd.rec(int(seconds * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=2)
	sd.wait()  # Wait until recording is finished
	print(f"\tRecording complete.")

	output_filepath = 'output.wav'
	scipy.io.wavfile.write(output_filepath, SAMPLE_RATE, my_recording)
	print(f"\tSaved: '{output_filepath}'")


if __name__ == '__main__':
	main()
