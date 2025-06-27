#  Product     : Cokoino Real-Wheel Drive Steering Car Chassis kit
#  Auther      : www.cokoino.com
#  Modification: 2025/05/13
import RPi.GPIO as GPIO # Import RPi.GPIO library
import time  # Import time library for delay
from time import sleep #Import sleep function from time module

# Define L298N module control pins
ENA = 12 #The ENA pin is connected to the GPO12 pin
ENB = 13 #The ENB pin is connected to the GPO13 pin
in1 = 23 #The in1 pin is connected to the GPO23 pin
in2 = 24 #The in2 pin is connected to the GPO24 pin
in3 = 25 #The in3 pin is connected to the GPO25 pin
in4 = 18 #The in4 pin is connected to the GPO18 pin
servo_pin = 21  # The servo is connected to the GPO21 pin
temp1=1 # Assign the variable temp1 to 1

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set pins to output mode
GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(ENB,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)

#Initialize L298N signal
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p1=GPIO.PWM(ENA,1000)  #Initialize the PWM of ENA pin and set the frequency to 1000Hz.
p2=GPIO.PWM(ENB,1000)  #Initialize the PWM of ENB pin and set the frequency to 1000Hz.
p1.start(30)  #Start PWM with an initial duty cycle of 30
p2.start(30)  #Start PWM with an initial duty cycle of 30
# Create PWM object with frequency set to 50Hz
pwm = GPIO.PWM(servo_pin, 50)
# Start PWM with an initial duty cycle of 0%
pwm.start(0) #Start PWM with an initial duty cycle of 0

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward lf-leftforward rf-rightforward l-low m-medium h-high e-exit")
print("\n")

def set_angle(angle):
    # Calculate duty cycle (0.5ms to 2.5ms=>0% -180%)
    duty_cycle = angle / 18 + 2  # transcoding
    pwm.ChangeDutyCycle(duty_cycle)  # Modify the duty cycle of the servo motor
    time.sleep(1)  # Wait for 1 second to complete the servo rotation

while(1): #while true

    x=input() #Retrieve your input and store it in variable x
    
    if x=='r':#Enter character r
        print("run")      #Print output string 'run'
        if(temp1==1):     # The variable temp1 is equal to 1
         set_angle(90)    # Set the servo to 90 degrees
         time.sleep(0.5)  # Wait for 0.5 seconds
         
         GPIO.output(in1,GPIO.LOW)  #Input low level to the IN1 pin of L298N
         GPIO.output(in2,GPIO.HIGH) #Input high level to the IN2 pin of L298N
         GPIO.output(in3,GPIO.LOW)  #Input low level to the IN3 pin of L298N
         GPIO.output(in4,GPIO.HIGH) #Input high level to the IN4 pin of L298N
         print("forward")           #Print output string 'forward'
         x='z'
        else:
         set_angle(90)  # Set the servo to 90 degrees
         time.sleep(0.5)  # Wait for 0.5 seconds
         GPIO.output(in1,GPIO.HIGH) #Input high level to the IN1 pin of L298N
         GPIO.output(in2,GPIO.LOW)  #Input low level to the IN2 pin of L298N
         GPIO.output(in3,GPIO.HIGH) #Input high level to the IN3 pin of L298N
         GPIO.output(in4,GPIO.LOW)  #Input low level to the IN4 pin of L298N
         print("backward")          #Print output string 'backward'
         x='z'


    elif x=='s':#Enter character s
        set_angle(90)  # Set the servo to 90 degrees
        time.sleep(0.5)  # Wait for 0.5 seconds
        GPIO.output(in1,GPIO.LOW)  #Input low level to the IN1 pin of L298N
        GPIO.output(in2,GPIO.LOW)  #Input low level to the IN2 pin of L298N
        GPIO.output(in3,GPIO.LOW)  #Input low level to the IN3 pin of L298N
        GPIO.output(in4,GPIO.LOW)  #Input low level to the IN4 pin of L298N
        print("stop")              #Print output string 'stop'
        x='z'

    elif x=='f':#Enter character f
        set_angle(90)  # Set the servo to 90 degrees
        time.sleep(0.5)  # Wait for 0.5 seconds
        GPIO.output(in1,GPIO.LOW)  #Input low level to the IN1 pin of L298N
        GPIO.output(in2,GPIO.HIGH) #Input high level to the IN2 pin of L298N
        GPIO.output(in3,GPIO.LOW)  #Input low level to the IN3 pin of L298N
        GPIO.output(in4,GPIO.HIGH) #Input high level to the IN4 pin of L298N
        print("forward")           #Print output string 'forward'
        temp1=1                    # Assign the variable temp1 to 1
        x='z'

    elif x=='b':#Enter character b
        set_angle(90)  # Set the servo to 90 degrees
        time.sleep(0.5)  # Wait for 0.5 seconds
        GPIO.output(in1,GPIO.HIGH) #Input high level to the IN1 pin of L298N
        GPIO.output(in2,GPIO.LOW)  #Input low level to the IN2 pin of L298N
        GPIO.output(in3,GPIO.HIGH) #Input high level to the IN3 pin of L298N
        GPIO.output(in4,GPIO.LOW)  #Input low level to the IN4 pin of L298N
        print("backward")          #Print output string 'backward'
        temp1=0                    # Assign the variable temp1 to 0
        x='z'
        
    elif x=='lf':#Enter character lf
        print("leftforward")
        set_angle(110)  # Set the servo to 110 degrees
        time.sleep(0.5)  # Wait for 0.5 seconds
        GPIO.output(in1,GPIO.LOW)  #Input low level to the IN1 pin of L298N
        GPIO.output(in2,GPIO.HIGH) #Input high level to the IN2 pin of L298N
        GPIO.output(in3,GPIO.LOW)  #Input low level to the IN3 pin of L298N
        GPIO.output(in4,GPIO.HIGH) #Input high level to the IN4 pin of L298N
        temp1=0                    # Assign the variable temp1 to 0
        x='z'
        
    elif x=='rf':#Enter character rf
        print("rightforward")
        set_angle(70)  # Set the servo to 70 degrees
        time.sleep(0.5)  # Wait for 0.5 seconds
        GPIO.output(in1,GPIO.LOW)  #Input low level to the IN1 pin of L298N
        GPIO.output(in2,GPIO.HIGH) #Input high level to the IN2 pin of L298N
        GPIO.output(in3,GPIO.LOW)  #Input low level to the IN3 pin of L298N
        GPIO.output(in4,GPIO.HIGH) #Input high level to the IN4 pin of L298N
        temp1=0                    #Assign the variable temp1 to 0
        x='z'
   
        
    elif x=='l':#Enter character l
        print("low")
        p1.ChangeDutyCycle(30)    #Adjust the duty cycle of the p1 PWM signal to 30
        p2.ChangeDutyCycle(30)    #Adjust the duty cycle of the p2 PWM signal to 30
        x='z'
    elif x=='m':#Enter character m
        print("medium")
        p1.ChangeDutyCycle(60)    #Adjust the duty cycle of the p1 PWM signal to 60
        p2.ChangeDutyCycle(60)    #Adjust the duty cycle of the p2 PWM signal to 60
        x='z'
    elif x=='h':#Enter character h
        print("high")
        p1.ChangeDutyCycle(90)    #Adjust the duty cycle of the p1 PWM signal to 90
        p2.ChangeDutyCycle(90)    #Adjust the duty cycle of the p2 PWM signal to 90
        x='z'
    elif x=='e':#Enter character e
        GPIO.cleanup()            #Clean GPIO settings
        print("GPIO Clean up")
        break                     #Terminate the loop
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

