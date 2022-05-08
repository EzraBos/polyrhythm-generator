#import threading
import time
#import winsound
#from playsound import playsound
import pygame

pygame.mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 2**12)
beep1 = pygame.mixer.Sound("beep1.wav")
beep2 = pygame.mixer.Sound("beep2.wav")
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)



def maybe_play(current_time):
    print(current_time)
    if current_time == 0.2:
        channel1.unpause()
    if current_time == 0:
        channel2.unpause()
    
    if current_time == 1:
        channel1.pause()
    if current_time == 0.6:
        channel2.pause()

# setup
channel1.play(beep1, loops = 0)
channel2.play(beep2, loops = 0)
channel1.pause()
channel2.pause()

time.sleep(0.5)

current_time = -0.1
while True: 
    # control time
    current_time += 0.1 # this is in ms
    current_time = round(current_time, 1)
    if current_time == 1: current_time = 0 # keep smol
    print(current_time)

    # maybe play sound
    if current_time == 0 or current_time == 0.5:
        channel1.play(beep1, loops=0)
    if current_time == 0 or current_time == 0.3 or current_time == 0.6:
        channel2.play(beep2, loops=0)
    
    time.sleep(0.1)
    

# Different failed variations to accomplish the same goal 

def speed_func(ratio, tempo):
     return (tempo - (tempo / ratio)) / tempo
 
def pulse(beep_num, speed):
    my_speed = speed_func(speed, 120)
    #time.sleep(my_speed)
    #time.sleep(my_speed)
    #playsound(f"beep{beep_num}.mp3") # beep1.mp3 if beep_num is 1
    #winsound.PlaySound(f"beep{beep_num}.wav", winsound.SND_ASYNC)
    channel2.play(beep2, loops = -1)

while True:
    my_speed1 = speed_func(2, 120)
    my_speed2 = speed_func(2, 120)
    pulse(1, 2)
    #pulse(2, 3)
    time.sleep(.5)




while True:   
    threading.Thread(target=pulse, args=(frequency1, .5)).start()
    threading.Thread(target=pulse, args=(frequency2, .5)).start()
    thread_pulse1 = threading.Thread(target=pulse, args=(1, 3,))
    thread_pulse2 = threading.Thread(target=pulse, args=(2, 2,))
    thread_pulse1.start()
    thread_pulse2.start()

    thread_pulse1.join()
    thread_pulse2.join()


# alternative theory: making a timeline and placing beats within that

def main():
    beat = 12
    beats = [
        (800, 6),
        (1000, 6)
    ]

    def play_sound(sound_list, t):
        to_play = 0
        for sound in sound_list:
            freq, time = sound
            if t % time == 0:
                to_play += freq
        if to_play != 0:
            winsound.Beep(to_play, 100)

    for i in range(1):
        for t in range(beat):
            play_sound(beats, t)
            time.sleep(1/beat)

if __name__== "__main__":
    main()
