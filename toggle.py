from machine import Pin
import time

led = Pin(18, Pin.OUT)
button = Pin(22, Pin.IN, Pin.PULL_DOWN)

led.off()

while True:
    if button.value() == 1:
        time.sleep(0.05)

        # Check that the button is still pressed.
        if button.value() == 1:
            if led.value() == 0:
                led.on()
            else:
                led.off()

            # Wait for the button to be released.
            while button.value() == 1:
                time.sleep(0.01)

            time.sleep(0.05)

    time.sleep(0.01)