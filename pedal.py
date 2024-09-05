#!/usr/bin/python3
import os
import sys

import pedalboard as pd


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


def get_arg_as_number(arr, index, default=0):
	try:
		return float(arr[index])
	except Exception as e:
		return default


def effect_log(message):
	print(f"\t=> {bcolors.OKGREEN}EFFECT: {bcolors.WARNING}{message}{bcolors.ENDC}")


def get_effect(option):
	if not "=" in option: return None

	parts = option.split("=")
	effect_name = parts[0]
	args = parts[1].split(",")
	match effect_name:
		case 'Chorus' | 'ch':
			effect_log(f"Chorus effect!")
			return pd.Chorus()
		case 'Clipping' | 'cl':
			threshold_db = get_arg_as_number(args, 0, default=-6.0)
			effect_log(f"Clipping effect with {threshold_db=}!")
			return pd.Clipping(threshold_db=threshold_db)
		case 'Compressor' | 'cp':
			threshold_db = get_arg_as_number(args, 0, default=-25)
			ratio = get_arg_as_number(args, 1, default=4)
			effect_log(f"Compressor effect with {threshold_db=} and {ratio=}!")
			return pd.Compressor(threshold_db=threshold_db, ratio=ratio)
		case 'Delay' | 'd':
			delay_seconds = get_arg_as_number(args, 0, default=0.5)
			feedback = get_arg_as_number(args, 1, default=0.0)
			mix = get_arg_as_number(args, 2, default=0.5)
			effect_log(f"Delay effect with {delay_seconds=}, {feedback=} and {mix=}!")
			return pd.Delay(delay_seconds=delay_seconds, feedback=feedback, mix=mix)
		case 'Distortion' | 'di':
			drive_db = get_arg_as_number(args, 0, default=5)
			effect_log(f"Distortion effect with {drive_db=}!")
			return pd.Distortion(drive_db=drive_db)
		case 'Gain' | 'g':
			gain_db = get_arg_as_number(args, 0, default=5)
			effect_log(f"Gain effect with {gain_db=}!")
			return pd.Gain(gain_db=gain_db)
		case 'HighpassFilter' | 'hpf':
			cutoff_frequency_hz = get_arg_as_number(args, 0, default=900)
			effect_log(f"HighpassFilter effect with {cutoff_frequency_hz=}!")
			return pd.HighpassFilter(cutoff_frequency_hz=cutoff_frequency_hz)
		case 'HighShelfFilter' | 'hsf':
			cutoff_frequency_hz = get_arg_as_number(args, 0, default=440)
			gain_db = get_arg_as_number(args, 1, default=0.0)
			q = get_arg_as_number(args, 2, default=0.7071067690849304)
			effect_log(f"HighShelfFilter effect with {cutoff_frequency_hz=}, {gain_db=} and {q=}!")
			return pd.HighShelfFilter(cutoff_frequency_hz=cutoff_frequency_hz, gain_db=gain_db, q=q)
		case 'LadderFilter' | 'lf':
			cutoff_hz = get_arg_as_number(args, 0, default=900)
			effect_log(f"LadderFilter effect with {cutoff_hz=}!")
			return pd.LadderFilter(mode=pd.LadderFilter.Mode.HPF12, cutoff_hz=cutoff_hz)
		case 'Limiter' | 'l':
			threshold_db = get_arg_as_number(args, 0, default=-10.0)
			release_ms = get_arg_as_number(args, 0, default=100.0)
			effect_log(f"Limiter effect with {threshold_db=} and {release_ms=}!")
			return pd.Limiter(threshold_db=threshold_db, release_ms=release_ms)
		case 'LowpassFilter' | 'lpf':
			cutoff_frequency_hz = get_arg_as_number(args, 0, default=900)
			effect_log(f"LowpassFilter effect with {cutoff_frequency_hz=}!")
			return pd.LowpassFilter(cutoff_frequency_hz=cutoff_frequency_hz)
		case 'LowShelfFilter' | 'lsf':
			cutoff_frequency_hz = get_arg_as_number(args, 0, default=440)
			gain_db = get_arg_as_number(args, 1, default=0.0)
			q = get_arg_as_number(args, 2, default=0.7071067690849304)
			effect_log(f"LowShelfFilter effect with {cutoff_frequency_hz=}, {gain_db=} and {q=}!")
			return pd.LowShelfFilter(cutoff_frequency_hz=cutoff_frequency_hz, gain_db=gain_db, q=q)
		case 'NoiseGate' | 'ng':
			threshold_db = get_arg_as_number(args, 0, default=-100.0)
			ratio = get_arg_as_number(args, 1, default=10)
			attack_ms = get_arg_as_number(args, 2, default=1.0)
			release_ms = get_arg_as_number(args, 3, default=100.0)
			effect_log(f"NoiseGate effect with {threshold_db=}, {ratio=}, {attack_ms=} and {release_ms=}!")
			return pd.NoiseGate(threshold_db=threshold_db, ratio=ratio, attack_ms=attack_ms, release_ms=release_ms)
		case 'Phaser' | 'p':
			effect_log(f"Phaser effect!")
			return pd.Phaser()
		case 'PitchShift' | 'ps':
			semitones = get_arg_as_number(args, 0, default=5)
			effect_log(f"PitchShift effect with {semitones=}!")
			return pd.PitchShift(semitones=semitones)
		case 'Reverb' | 'r':
			room_size = get_arg_as_number(args, 0, default=0.25)
			damping = get_arg_as_number(args, 1, default=0.5)
			effect_log(f"Reverb effect with {room_size=} and {damping=}!")
			return pd.Reverb(room_size=room_size, damping=damping)
		case _:
			return None


def pedal_me_this(input_filepath, output_filepath, options):
	effects = []

	for option in options:
		effect = get_effect(option)
		if effect:
			effects += [ effect ]
		else:
			print(f"Unknown effect: '{option}'")

	board = pd.Pedalboard(effects)

	with pd.io.AudioFile(input_filepath) as f:
		with pd.io.AudioFile(output_filepath, 'w', f.samplerate, f.num_channels) as o:
			# Read one second of audio at a time, until the file is empty:
			while f.tell() < f.frames:
				chunk = f.read(f.samplerate)

				# Run the audio through our pedalboard:
				effected = board(chunk, f.samplerate, reset=False)

				# Write the output to our output file:
				o.write(effected)


def main():
	args = sys.argv[1:]
	if len(args) < 2:
		print(f"Usage:\n\tpython3 peddle.py INPUT OUTPUT ARGS")
		return

	input_filepath = args[0]
	output_filepath = args[1]
	options = args[2:]

	if not os.path.isfile(input_filepath):
		print(f"Input file not found: '{input_filepath}'")
		return

	if os.path.isfile(output_filepath):
		print(f"Output file exists: '{output_filepath}'")
		response = input(f"Overwrite? (y/n) ")
		if response != 'y':
			return

	pedal_me_this(input_filepath, output_filepath, options)


if __name__ == '__main__':
	main()
