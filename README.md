
# Pedal

`Pedal` is a command-line utility built on top of the [Awesome Pedalboard Library](https://github.com/spotify/pedalboard).
I use it to apply Pedalboard Effects on Audio without having to write a new `Python` script every time.

I am using [`readmix`](https://github.com/iaseth/readmix) for generating this README.
You can view the source file [here](https://github.com/iaseth/pedal/blob/master/README.md.rx).


## Usage

```
python3 pedal.py input.mp3 output.mp3 Chorus=
```


## Supported Effects

| | Effect | Shortcut | Arguments |
| ---- | ---- | ---- | ---- |
|  1 | `Chorus`          | `ch`  | `None` |
|  2 | `Clipping`        | `cl`  | `threshold_db` |
|  3 | `Compressor`      | `cp`  | `threshold_db`<br>`ratio` |
|  4 | `Delay`           | `d`   | `delay_seconds`<br>`feedback`<br>`mix` |
|  5 | `Distortion`      | `di`  | `drive_db` |
|  6 | `Gain`            | `g`   | `gain_db` |
|  7 | `HighpassFilter`  | `hpf` | `cutoff_frequency_hz` |
|  8 | `HighShelfFilter` | `hsf` | `cutoff_frequency_hz`<br>`gain_db`<br>`q` |
|  9 | `LadderFilter`    | `lf`  | `cutoff_hz` |
| 10 | `Limiter`         | `l`   | `threshold_db`<br>`release_ms` |
| 11 | `LowpassFilter`   | `lpf` | `cutoff_frequency_hz` |
| 12 | `LowShelfFilter`  | `lsf` | `cutoff_frequency_hz`<br>`gain_db`<br>`q` |
| 13 | `NoiseGate`       | `ng`  | `threshold_db`<br>`ratio`<br>`attack_ms`<br>`release_ms` |
| 14 | `Phaser`          | `p`   | `None` |
| 15 | `PitchShift`      | `ps`  | `semitones` |
| 16 | `Reverb`          | `r`   | `room_size`<br>`damping` |


## License
MIT License

Copyright (c) Ankur Seth.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Credit

This file was generated using [`readmix`](https://github.com/iaseth/readmix).

