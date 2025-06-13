import homework7, importlib
importlib.reload(homework7)
import matplotlib.pyplot as plt

Fs = 8000
F0 = 110
F1 = {'a': 800, 'i': 300, 'u': 350, 'e': 500, 'o': 400}
F2 = {'a': 1150, 'i': 2200, 'u': 600, 'e': 1700, 'o': 800}

# Test voiced_excitation
excitation = homework7.voiced_excitation(8000, F0, Fs)
plt.figure(figsize=(14,4))
plt.stem(excitation[:300])
plt.title('First 300 samples of voiced excitation')
plt.show()

# Test resonator
resonance = homework7.resonator(excitation, 500, 100, Fs)
plt.figure(figsize=(14,4))
plt.plot(resonance[:300])
plt.title('500 Hz resonator output')
plt.show()

# Test synthesize_vowel
fig = plt.figure(figsize=(14,15), layout='tight')
subfig = fig.subplots(5,1)
for idx, phoneme in enumerate('aiueo'):
    speech = homework7.synthesize_vowel(8000, F0, F1[phoneme], F2[phoneme], 2500, 3500, 100, 200, 300, 400, Fs)
    subfig[idx].plot(speech[:300])
    subfig[idx].set_title(f'Artificial /{phoneme}/')
plt.show()
