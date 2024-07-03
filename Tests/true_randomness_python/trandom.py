import pyfirmata
import time
import random

board = pyfirmata.Arduino('/dev/ttyUSB0')
analog_input_pin = 0

it = pyfirmata.util.Iterator(board)
it.start()

board.analog[analog_input_pin].enable_reporting()
initial_noise_value = board.analog[analog_input_pin].read()
random.seed(initial_noise_value if initial_noise_value is not None else 0)
baud_rate = 9600

def loop():
    # Read noise value from analog pin
    noise_value = board.analog[analog_input_pin].read()
    if noise_value is not None:
        # Convert the analog value from 0-1 to 0-1023 range
        noise_value = int(noise_value * 1023)
        # Generate a random number
        random_number = random.randint(0, 255)

        # Print the values
        print(f"Noise Value: {noise_value}")
        print(f"Random Number: {random_number}")

while True:
    loop()
    time.sleep(1)
