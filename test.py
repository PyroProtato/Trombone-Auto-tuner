import sounddevice as sd
import numpy as np
import aubio
import math
import sys

# --- Configuration ---
FS = 44100         # Sample rate in Hz
CHANNELS = 1       # Mono input
BLOCKSIZE = 1024   
HOP_SIZE = 512     

average = 0
total = 0
bigsamples = []
SAMPLES_SIZE = 10

smallavg = 0
smalltotal = 0
smallsamples = []
SMALL_SAMPLES_SIZE = 3


#Pitches
PITCH_FREQUENCIES = {
    'A0': 27.50,
    'A#0': 29.14,
    'B0': 30.87,
    'C1': 32.70,
    'C#1': 34.65,
    'D1': 36.71,
    'D#1': 38.89,
    'E1': 41.20,
    'F1': 43.65,
    'F#1': 46.25,
    'G1': 49.00,
    'G#1': 51.91,
    'A1': 55.00,
    'A#1': 58.27,
    'B1': 61.74,
    'C2': 65.41,
    'C#2': 69.30,
    'D2': 73.42,
    'D#2': 77.78,
    'E2': 82.41,
    'F2': 87.31,
    'F#2': 92.50,
    'G2': 98.00,
    'G#2': 103.83,
    'A2': 110.00,
    'A#2': 116.54,
    'B2': 123.47,
    'C3': 130.81,
    'C#3': 138.59,
    'D3': 146.83,
    'D#3': 155.56,
    'E3': 164.81,
    'F3': 174.61,
    'F#3': 185.00,
    'G3': 196.00,
    'G#3': 207.65,
    'A3': 220.00,
    'A#3': 233.08,
    'B3': 246.94,
    'C4': 261.63,  # Middle C
    'C#4': 277.18,
    'D4': 293.66,
    'D#4': 311.13,
    'E4': 329.63,
    'F4': 349.23,
    'F#4': 369.99,
    'G4': 392.00,
    'G#4': 415.30,
    'A4': 440.00,  # Concert Pitch Standard
    'A#4': 466.16,
    'B4': 493.88,
    'C5': 523.25,
    'C#5': 554.37,
    'D5': 587.33,
    'D#5': 622.25,
    'E5': 659.25,
    'F5': 698.46,
    'F#5': 739.99,
    'G5': 783.99,
    'G#5': 830.61,
    'A5': 880.00,
    'A#5': 932.33,
    'B5': 987.77,
    'C6': 1046.50,
    'C#6': 1108.73,
    'D6': 1174.66,
    'D#6': 1244.51,
    'E6': 1318.51,
    'F6': 1396.91,
    'F#6': 1479.98,
    'G6': 1567.98,
    'G#6': 1661.22,
    'A6': 1760.00,
    'A#6': 1864.66,
    'B6': 1975.53,
    'C7': 2093.00,
    'C#7': 2217.46,
    'D7': 2349.32,
    'D#7': 2489.02,
    'E7': 2637.02,
    'F7': 2793.83,
    'F#7': 2959.96,
    'G7': 3135.96,
    'G#7': 3322.44,
    'A7': 3520.00,
    'A#7': 3729.31,
    'B7': 3951.07,
    'C8': 4186.01
}



# --- Initialize aubio Pitch Detection with YIN algorithm ---
# YIN is generally more accurate for musical instruments with rich harmonics.
p = aubio.pitch("yin", BLOCKSIZE, HOP_SIZE, FS) 

# Set parameters for a more stable tuner experience:

# Use 'midi' unit for better understanding of note boundaries, we convert back to Hz for display
p.set_unit("Hz") 

# Tolerance: Lower tolerance makes it more strict (can drop out if noisy)
# Higher tolerance is more 'forgiving' but might jump notes. 0.8 is a good balance.
p.set_tolerance(0.75) 

# Silence Threshold: Below this dB value, no pitch is detected
p.set_silence(-45) # Set a lower threshold for brass instruments to prevent noise



def aubio_audio_callback(indata, frames, time, status):
    global average
    global total
    global bigsamples

    global smallavg
    global smalltotal
    global smallsamples
    
    assert frames == HOP_SIZE, f"Callback frames size mismatch: expected {HOP_SIZE}, got {frames}"
    
    if status:
        print(status, file=sys.stderr)
    
    samples = indata[:, 0].astype(aubio.float_type)

    pitch_hz = p(samples)[0] # Get the frequency value
    confidence = p.get_confidence() # Get the confidence value (float)

    #Volume
    volume_norm = np.sqrt(np.mean(samples**2)) * 1000 
    db_level = 20 * np.log10(volume_norm + 1e-10)


    #Detects if each pitch should be heard
    if pitch_hz > 0 and confidence > 0.3 and db_level > 55.0: # aubio returns 0 Hz if it detects silence/no confident pitch
        #print(f"Detected Frequency: {abs(pitch_hz):.2f} Hz (Confidence: {confidence:.2f}) Volume: {db_level}")

        total += pitch_hz
        bigsamples.append(pitch_hz)
        eliminate_outliers_percentile(bigsamples, 5, 95)
        
        if len(bigsamples) > SAMPLES_SIZE:
            total -= bigsamples[0]
            del bigsamples[0]
    
        average = total/len(bigsamples)

        target = PITCH_FREQUENCIES[pitch(average)]
        action = ""
        if average < target:
            action = "flat"
        else:
            action = "sharp"

        print(f"{pitch(average)} {action} {average-target}")




       


def eliminate_outliers_percentile(data_list, lower_p=5, upper_p=95):
    """
    Eliminates data points outside the specified percentile range.
    """
    data_arr = np.array(data_list)
    # Calculate the 5th and 95th percentiles
    lower_bound = np.percentile(data_arr, lower_p)
    upper_bound = np.percentile(data_arr, upper_p)
    
    # Filter the data to keep only values within the bounds
    cleaned_list = data_arr[(data_arr >= lower_bound) & (data_arr <= upper_bound)].tolist()
    return cleaned_list, lower_bound, upper_bound



def pitch(freq):
    # A4 (440 Hz) is 4.75 octaves above C0 in a 16 Hz based system
    A4 = 440
    C0 = A4 * math.pow(2, -4.75) 
    
    # Note names in an octave
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
    # Calculate the number of half steps 'h' from C0
    # The formula h = 12 * log2(P / C0) is used
    h = round(12 * math.log2(freq / C0))
    
    # Calculate the octave and the note name index
    octave = h // 12
    n = h % 12
    
    # Return the note name and octave as a combined string
    return name[n] + str(octave)
    


print("Starting Aubio YIN pitch stream... Press Ctrl+C to stop.")
try:
    with sd.InputStream(samplerate=FS, blocksize=HOP_SIZE, channels=CHANNELS, callback=aubio_audio_callback):
        while True:
            sd.sleep(1000) 
except KeyboardInterrupt:
    print("\nStream stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")






"""
holdover = 0
#Gets the average of the last 3 samples
smalltotal += pitch_hz
smallsamples.append(pitch_hz)
if len(smallsamples) > SMALL_SAMPLES_SIZE:
    smalltotal -= smallsamples[0]
    holdover = smallsamples[0]
    del smallsamples[0]
#Deletes outliers
if len(smallsamples) == SMALL_SAMPLES_SIZE and abs(smallsamples[1]-smallsamples[0]) > smallsamples[0] * 0.05 and abs(smallsamples[1]-smallsamples[2]) > smallsamples[2] * 0.05:
    smalltotal -= smallsamples[1]
    del smallsamples[1]
smallavg = smalltotal/len(smallsamples)

if abs(average-smallavg) > average*0.1:
    #Resets samples if detects a note change
    print("Note Change!")
    bigsamples = []
    total = 0
    bigsamples.append(holdover)
    total += holdover
else:
    #Gets the average of the last 10 samples minus the last 3
    total += holdover
    bigsamples.append(holdover)
    
    if len(bigsamples) > SAMPLES_SIZE:
        total -= bigsamples[0]
        del bigsamples[0]

average = total/len(bigsamples)


#print(f"{average} {smallavg} {abs(average-smallavg)}")
"""