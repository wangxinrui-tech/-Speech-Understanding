import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    '''
    Chop a waveform into overlapping frames.
    '''
    N = len(waveform)
    num_frames = 1 + (N - frame_length) // step
    frames = np.zeros((frame_length, num_frames))
    
    for t in range(num_frames):
        start = t * step
        end = start + frame_length
        frames[:, t] = waveform[start:end]
    
    return frames

def frames_to_stft(frames):
    '''
    Take the FFT of every column of the frames matrix.
    '''
    stft = np.fft.fft(frames, axis=0)  # FFT along each column (frame)
    return stft

def stft_to_spectrogram(stft):
    '''
    Convert STFT to decibel-scaled spectrogram with normalization and clipping.
    '''
    spectrogram = 20 * np.log10(np.abs(stft) + 1e-10)  # add epsilon to avoid log(0)
    spectrogram -= np.max(spectrogram)  # normalize so max is 0 dB
    spectrogram = np.maximum(spectrogram, -60)  # clip to -60 dB minimum
    return spectrogram
