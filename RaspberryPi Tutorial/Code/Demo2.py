#  Product     : Cokoino Real-Wheel Drive Steering Car Chassis kit
#  Auther      : www.cokoino.com
#  Modification: 2025/05/13
import RPi.GPIO as GPIO # Import RPi.GPIO library
import time  # Import time library for delay
from time import sleep

# Define cokoino 4wd robot hat control pins
NSLEEP1 = 12  # The 1# drv8833 NSLEEP pin is connected to the GPO12 pin
AN11 = 17     # The 1# drv8833 AN1 pin is connected to the GPO17 pin
AN12 = 27     # The 1# drv8833 AN2 pin is connected to the GPO27 pin
BN11 = 22     # The 1# drv8833 BN1 pin is connected to the GPO22 pin
BN12 = 23     # The 1# drv8833 BN2 pin is connected to the GPO23 pin
NSLEEP2 = 13  # The 2# drv8833 NSLEEP pin is connected to the GPO13 pin
AN21 = 24     # The 2# drv8833 AN1 pin is connected to the GPO24 pin
AN22 = 25     # The 2# drv8833 AN2 pin is connected to the GPO25 pin
BN21 = 26     # The 2# drv8833 BN1 pin is connected to the GPO26 pin
BN22 = 16     # The 2# drv8833 BN2 pin is connected to the GPO16 pin

servo_pin = 21  # The servo is connected to the GPO21 pin
temp1=1         # Assign the variable temp1 to 1

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
# Set pins to output mode
GPIO.setup(NSLEEP1,GPIO.OUT)
GPIO.setup(NSLEEP2,GPIO.OUT)
GPIO.setup(AN11,GPIO.OUT)
GPIO.setup(AN12,GPIO.OUT)
GPIO.setup(BN21,GPIO.OUT)
GPIO.setup(BN22,GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)
#Initialize DRV8833 signal
GPIO.output(AN11,GPIO.LOW)
GPIO.output(AN12,GPIO.LOW)
GPIO.output(BN21,GPIO.LOW)
GPIO.output(BN22,GPIO.LOW)

p1=GPIO.PWM(NSLEEP1,1000) #Initialize the PWM of NSLEEP1 pin and set the frequency to 1000Hz.
p2=GPIO.PWM(NSLEEP2,1000) #Initialize the PWM of NSLEEP2 pin and set the frequency to 1000Hz.
p1.start(30) #Start PWM with an initial duty cycle of 30
p2.start(30) #Start PWM with an initial duty cycle of 30

# Create PWM object with frequency set to 50Hz
pwm = GPIO.PWM(servo_pin, 50)
# Start PWM with an initial duty cycle of 0%
pwm.start(0)#Start PWM with an initial duty cycle of 30
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high lf-leftforward rf-rightforward e-exit")
print("\n")

def set_angle(angle):
    # Calculate duty cycle (0.5ms to 2.5ms=>0% -180%)
    duty_cycle = angle / 18 + 2  # transcoding
    pwm.ChangeDutyCycle(duty_cycle)  # Modify the duty cycle of the servo motor
    time.sleep(1)  # Wait for 1 second to complete the servo rotation

while(1):      #while true

    x=input()  #Retrieve your input and store it in variable x
    
    if x=='r': #Enter character r
        print("run")
        if(temp1==1):   # The variable temp1 is equal to 1
         set_angle(90)  # Set the servo to 90 degrees
         time.sleep(0.5)  # Wait for 0.5 seconds
         GPIO.output(AN11,GPIO.HIGH) #Input high level to the AN1 pin of 1 # DRV8833
         GPIO.output(AN12,GPIO.LOW)  #Input low level to the AN2 pin of 1 # DRV8833
         GPIO.output(BN21,GPIO.HIGH) #Input high level to the BN1 pin of 2 # DRV8833
         GPIO.output(BN22,GPIO.LOW)  #Input low level to the BN2 pin of 2 # DRV8833
         print("backward")
         x='z'
        else:
         set_angle(90)    # Set the servo to 90 degrees
         time.sleep(0.5)  # Wait for 0.5 seconds
         GPIO.output(AN11,GPIO.LOW)  #Input low level to the AN1 pin of 1 # DRV8833
         GPIO.output(AN12,GPIO.HIGH) #Input high level to the AN2 pin of 1 # DRV8833
         GPIO.output(BN21,GPIO.LOW)  #Input low level to the BN1 pin of 2 # DRV8833
         GPIO.output(BN22,GPIO.HIGH) #Input high level to the BN2 pin of 2 # DRV8833
         print("forward")
         x='z'


    elif x=='s':#Enter character s
        print("stop")
        set_angle(90)  # Set the servo to 90 degrees
        time.sleep(0.5)  # Wait for 0.5 seconds
        GPIO.output(AN11,GPIO.LOW) #Input low level to the AN1 pin of 1 # DRV8833
        GPIO.output(AN12,GPIO.LOW) #Input low level to the AN2 pin of 1 # DRV8833
        GPIO.output(BN21,GPIO.LOW) #Input low level to the BN1 pin of 2 # DRV8833
        GPIO.output(BN22,GPIO.LOW) #Input low level to the BN2 pin of 2 # DRV8833
        x='z'

    elif x=='f':#Enter character f
        print("forward")
        set_angle(90)  # Set the servo to 90 degrees
        time.sleep(0.5)  # Wait for 0.5 seconds
        GPIO.output(AN11,GPIO.LOW)
        GPIO.output(AN12,GPIO.HIGH)
        GPIO.output(BN21,GPIO.LOW)
        GPIO.output(BN22,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='b':#Enter character b
        print("backward")
        set_angle(90)  # Set the servo to 90 degrees
        time.sleep(0.5)  # Wait for 0.5 seconds
        GPIO.output(AN11,GPIO.HIGH)
        GPIO.output(AN12,GPIO.LOW)
        GPIO.output(BN21,GPIO.HIGH)
        GPIO.output(BN22,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='lf':#Enter character lf
        print("leftforward")
        set_angle(110)  # Set the servo to 110 degrees
        time.sleep(0.5)  # Wait for 0.5 seconds
        GPIO.output(AN11,GPIO.LOW)
        GPIO.output(AN12,GPIO.HIGH)
        GPIO.output(BN21,GPIO.LOW)
        GPIO.output(BN22,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='rf':#Enter character rf
        print("rightforward")
        set_angle(70)  # Set the servo to 70 degrees
        time.sleep(0.5)  # Wait for 0.5 seconds
        GPIO.output(AN11,GPIO.LOW)
        GPIO.output(AN12,GPIO.HIGH)
        GPIO.output(BN21,GPIO.LOW)
        GPIO.output(BN22,GPIO.HIGH)
        temp1=0
        x='z'
        
    elif x=='l':#Enter character l
        print("low")
        p1.ChangeDutyCycle(30) #Adjust the duty cycle of the p1 PWM signal to 30
        p2.ChangeDutyCycle(30) #Adjust the duty cycle of the p2 PWM signal to 30
        x='z'
    elif x=='m':#Enter character m
        print("medium")
        p1.ChangeDutyCycle(60)
        p2.ChangeDutyCycle(60)
        x='z'
    elif x=='h':#Enter character h
        print("high")
        p1.ChangeDutyCycle(90)
        p2.ChangeDutyCycle(90)
        x='z'
    elif x=='e':#Enter character e
        GPIO.cleanup()  # Clean GPIO settings
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

