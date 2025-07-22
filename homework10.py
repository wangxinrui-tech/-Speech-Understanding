import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    '''
    Chop a waveform into overlapping frames.
    
    @params:
    waveform (np.ndarray(N)) - the waveform
    frame_length (scalar) - length of the frame, in samples
    step (scalar) - step size, in samples
    
    @returns:
    frames (np.ndarray((frame_length, num_frames))) - waveform chopped into frames
    
    num_frames should be at least int((len(speech)-frame_length)/step); it may be longer.
    For every n and t such that 0 <= t*step+n <= N-1, it should be the case that 
       frames[n,t] = waveform[t*step+n]
    '''
    N = len(waveform)
    num_frames = int(np.ceil((N - frame_length) / step)) + 1
    frames = np.zeros((frame_length, num_frames))
    
    for t in range(num_frames):
        start = t * step
        end = start + frame_length
        if end > N:
            # Pad with zeros if we go past the end of the waveform
            pad_length = end - N
            frames[:, t] = np.pad(waveform[start:N], (0, pad_length), 'constant')
        else:
            frames[:, t] = waveform[start:end]
    
    return frames

def frames_to_stft(frames):
    '''
    Take the FFT of every column of the frames matrix.
    
    @params:
    frames (np.ndarray((frame_length, num_frames))) - the speech samples (real-valued)
    
    @returns:
    stft (np.ndarray((frame_length,num_frames))) - the STFT (complex-valued)
    '''
    return np.fft.fft(frames, axis=0)

def stft_to_spectrogram(stft):
    '''
    Calculate the level, in decibels, of each complex-valued sample of the STFT,
    normalized so the highest value is 0dB, 
    and clipped so that the lowest value is -60dB.
    
    @params:
    stft (np.ndarray((frame_length,num_frames))) - STFT (complex-valued)
    
    @returns:
    spectrogram (np.ndarray((frame_length,num_frames)) - spectrogram (real-valued)
    
    The spectrogram should be expressed in decibels (20*log10(abs(stft)).
    np.amax(spectrogram) should be 0dB.
    np.amin(spectrogram) should be no smaller than -60dB.
    '''
    magnitude = np.abs(stft)
    # Avoid log of zero by replacing zeros with a very small number
    magnitude[magnitude == 0] = np.finfo(float).eps
    spectrogram = 20 * np.log10(magnitude)
    
    # Normalize so max is 0dB
    max_val = np.amax(spectrogram)
    spectrogram = spectrogram - max_val
    
    # Clip to -60dB
    spectrogram = np.clip(spectrogram, -60, None)
    
    return spectrogram
