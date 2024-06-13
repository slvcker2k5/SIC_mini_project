from gpiozero import LED
led_red=LED(20)
while True:
    a=input()
    if a.upper()=="ON":
        led_red.on()
    elif a.upper()=="OFF":
        led_red.off()
    else:
        print("invalid command")
