import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
from getpass import getpass
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
buzz_pin = 32

GPIO.setup(buzz_pin, GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin, 1000)
frequency= [220, 440, 880, 1760]
color = [ 'R', 'G', 'B', 'Y' ]
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
def validate_guess(color_sequence_string, guess):
	if guess == color_sequence_string:
		print "you are correct"
	else:
		print "incorrect guess"
		print " the correct sequence is ", color_sequence_string
		print " your guess was: ", guess
		exit()

def loop():
	n = random.randint(0,3)
	color_sequence = [color[n]]
	frequency_sequence = [frequency[n]]
	while True:
		for i in range(0, len(color_sequence)): 
			Buzz.ChangeFrequency(frequency_sequence[i])
			Buzz.start(50)
			LED.setColor(color_sequence[i])
			time.sleep(0.5)
			Buzz.stop()
			LED.noColor()
			time.sleep(0.5)
		guess = getpass("Guess the color sequence: ")
   	 	color_sequence_string = ''.join(color_sequence) 
		validate_guess(color_sequence_string, guess.upper())
		n = random.randint(0,3)
		color_sequence.append(color[n])
		frequency_sequence.append(frequency[n])
		time.sleep(0.5)

if __name__ == '__main__':
	try:
		loop()
	except KeyboardInterrupt:
		print 'Goodbye'

