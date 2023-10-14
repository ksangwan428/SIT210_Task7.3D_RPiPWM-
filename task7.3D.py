# Import necessary modules
from time import sleep
from gpiozero import DistanceSensor, PWMOutputDevice

# Create a PWM Buzzer on GPIO pin 13
buzzer = PWMOutputDevice(13)

# Create a distance sensor with echo on GPIO 18 and trigger on GPIO 17
distance_sensor = DistanceSensor(echo=18, trigger=17)

# Define a safe_exit function to handle termination signals (unused in this code, but kept for context)
def exit_safely():
    exit(1)

# Main function to control the buzzer pulse based on distance
def main():
    running = True
    try:
        # Turn on the buzzer initially
        buzzer.on()

        while running:
            # Get the distance from the sensor
            distance = distance_sensor.value
            print(f'Distance: {distance:1.2f} meters')

            # Calculate the duty cycle for buzzer intensity
            intensity = round(1.0 - distance, 1)

            # Ensure the intensity is not below 0
            if intensity < 0:
                intensity = 0.0

            # Set the buzzer pulse
            buzzer.value = intensity

            # Sleep for a short duration
            sleep(0.1)

    except KeyboardInterrupt:
        pass

    finally:
        # Clean up and close the sensor
        running = False
        distance_sensor.close()

# Entry point of the program
if __name__ == '__main__':
    main()
