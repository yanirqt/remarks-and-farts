import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import pygame
import random
import board
import neopixel
   

#button_fart = 10
#button_speech = 16
led_fart = 0 
led_speech = 1

button_fart = 23
button_speech = 4

farts_count = 22  

speech = ["1_im_tirtzu","2_agada","shotim","dagim_halomot_retuvim","sneeze","hertzel_amar",
          "oded_amar","lev_sherutim","magvonim_rechecv","metuka","krem_shizuf",
          "naal_bait_teva","american_anthem","my_neck","sini","boxachoc","mevugarim_etzba",
          "mario","ohavim_naknikiot","ruah_shoreket","margol_1","margol_2","margol_3",
          "margol_4","margol_5","ahla_burn","caffe_ugandi","maim_md_caful","rothin","manamana",
          "bati_nidlakti","ruah_noshevet_krira","yeled_tze_maim","peter_laugh",
          "bahura_eroma_nahar","berlin","hamin","let_one_go","mami_lagur","tamtamtam",
          "eats_you","kus_emek_max_stock","one_day","fart_song","kesher_adam_naal",
          "rami_klain","this_summer"]
speech_position = 0
max_speech_position = 46


def play_fart():
    pixels[led_fart] = (0, 0, 0)
    pixels.show()
    random_fart_num = random.randrange(farts_count)
    file = '/home/pi/sounds/farts/'+ str(random_fart_num) +'.wav'
    print("opening ", file)
    soun_obj=pygame.mixer.Sound(file)
    soun_obj.play()
    pixels[led_speech] = (255, 255, 255)
    pixels.show()	

def play_speech():
    global speech_position
    global max_speech_position
    pixels[led_speech] = (0, 0, 0)
    pixels.show()
    print("currnet position ", speech_position)
    file = '/home/pi/sounds/speech/'+ speech[speech_position] +'.wav'
    print("opening ", file)
    while pygame.mixer.get_busy():
            continue
	    #time.sleep(0.01) 
    soun_obj=pygame.mixer.Sound(file)
    print("length",soun_obj.get_length())
    soun_obj.play()
    
    if speech_position >= max_speech_position:
    	speech_position = 0
    else:
    	speech_position = speech_position + 1
    time.sleep(soun_obj.get_length()-1)	
    pixels[led_fart] = (255, 255, 255)
    pixels.show()	

def button_fart_callback(channel):
    time.sleep(0.1)
    GPIO.remove_event_detect(button_fart)
    print("FART")
    play_fart()
    time.sleep(0.1)
    setupFart()

def button_speech_callback(channel):
    time.sleep(0.1)
    GPIO.remove_event_detect(button_speech)
    print("speech")
    play_speech()
    time.sleep(2)
    setupSpeech()
    
def setupFart():
  GPIO.add_event_detect(button_fart, GPIO.RISING, callback=button_fart_callback,bouncetime=500) 

def setupSpeech():
  GPIO.add_event_detect(button_speech, GPIO.RISING, callback=button_speech_callback,bouncetime=500) 
    

pygame.init()
pygame.mixer.init(48000, -16, 1, 1024)
pixels = neopixel.NeoPixel(
    board.D18, 2, brightness=0.6, auto_write=False, pixel_order=neopixel.GRB
)

pixels[led_speech] = (255, 255, 255)
pixels.show()

GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Use physical pin numsbering
#GPIO.setmode(GPIO.BCM)
GPIO.setup(button_fart, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_speech, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(button_fart,GPIO.BOTH,callback=button_fart_callback) # Setup event on pin 10 rising edge
GPIO.add_event_detect(button_speech,GPIO.BOTH,callback=button_speech_callback) # Setup event on pin 18 rising edge

#message = input("Press enter to quit\n\n") # Run until someone presses enter
while 1:
    time.sleep(5)

pixels[led_speech] = (0, 0, 0)
pixels[led_fart] = (0, 0, 0)
pixels.show()

GPIO.cleanup() # Clean up
