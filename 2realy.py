import RPi.GPIO as GPIO

# Define the GPIO pins that the relays are connected to
relay_pin_1 = 23
relay_pin_2 = 24

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the relay pins to output
GPIO.setup(relay_pin_1, GPIO.OUT)
GPIO.setup(relay_pin_2, GPIO.OUT)

# Turn on the first relay
print("Turning on relay 1")
GPIO.output(relay_pin_1, GPIO.HIGH)

# Wait for 5 seconds
time.sleep(5)

# Turn off the first relay
print("Turning off relay 1")
GPIO.output(relay_pin_1, GPIO.LOW)

# Turn on the second relay
print("Turning on relay 2")
GPIO.output(relay_pin_2, GPIO.HIGH)

# Wait for 5 seconds
time.sleep(5)

# Turn off the second relay
print("Turning off relay 2")
GPIO.output(relay_pin_2, GPIO.LOW)

# Close the GPIO pins
GPIO.cleanup()
