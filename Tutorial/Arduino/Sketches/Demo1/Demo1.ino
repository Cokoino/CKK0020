/**********************************************************************
  Product     : Cokoino Real-Wheel Drive Steering Car Chassis kit
  Auther      : www.cokoino.com
  Modification: 2025/04/23
**********************************************************************/

#include<Servo.h>
Servo myservo;  // Create a servo class

#define ENA 6 //Define the A enable end as 6
#define inPinN1 7//Define the input signal terminal IN1 as 7
#define inPinN2 8//Define the input signal terminal IN2 as 8

#define ENB 5//Define the A enable end as 5
#define inPinN3 9//Define the input signal terminal IN3 as 9
#define inPinN4 10//Define the input signal terminal IN4 as 10

//Duty cycle value: 0~255,the larger the duty cycle, the faster the motor rotates
const int speedA = 200;//The duty cycle of the left rear wheel motor speed can be adjusted to control the speed, and it is recommended not to be lower than 150
const int speedB = 200;//The duty cycle of the left rear wheel motor speed can be adjusted to control the speed, and it is recommended not to be lower than 150

void setup() {
  // put your setup code here, to run once:
  myservo.attach(2);  //Set the servo control pin as D2
  delay(100);//delay 0.1 second
  myservo.write(90); //Rotate the servo to 90 degrees to center the front wheel shaft
  delay(1000);//delay 1 second

  pinMode(ENA, OUTPUT);//Define the UNO R3 pin connected to the ENA terminal as the output mode
  pinMode(inPinN1,OUTPUT);//Define the UNO R3 pin connected to the N1 terminal as the output mode
  pinMode(inPinN2,OUTPUT);//Define the UNO R3 pin connected to the N2 terminal as the output mode
  pinMode(ENB,OUTPUT);//Define the UNO R3 pin connected to the ENB terminal as the output mode
  pinMode(inPinN3,OUTPUT);//Define the UNO R3 pin connected to the N3 terminal as the output mode
  pinMode(inPinN4,OUTPUT);//Define the UNO R3 pin connected to the N4 terminal as the output mode
}

void loop() {
  // put your main code here, to run repeatedly:
  forwardPwm(speedA,speedB);//The rear wheels rotate, causing the car to move forward
  delay(2000);//move forward 2 seconds
  stop();
  delay(1000);//Maintain a 2-second stop state

  backwardPwd(speedA, speedB);//The rear wheels rotate, causing the car to move backward
  delay(2000);//move backward 2 seconds
  stop();
  delay(1000);//Maintain a 2-second stop state

  forwardRight(speedB);
  delay(500);
  stop();
  delay(1000);//Maintain a 2-second stop state

  forwardLeft(speedB);
  delay(500);
  stop();
  delay(1000);//Maintain a 2-second stop state
}

//PWM regulates the forward speed
void forwardPwm(int valueA,int valueB)
{
  myservo.write(90); //Initialize the servo to the 90 degree position
  delay(500);//delay 0.5 second
  forwardPwmA(valueA);//Left rear wheel forward
  forwardPwmB(valueB);//Right rear wheel forward
}

//Left rear wheel
void forwardPwmA(int value)
{
  analogWrite(ENA, value);//Input PWM signal to ENA
  digitalWrite(inPinN1,HIGH);//Input high level to N1
  digitalWrite(inPinN2,LOW);//Input low level to N2
}
//Right rear wheel
void forwardPwmB(int value)
{
  analogWrite(ENB, value);//Input PWM signal to ENB
  digitalWrite(inPinN3,HIGH);//Input high level to N3
  digitalWrite(inPinN4,LOW);//Input low level to N4
}

//stop
void stop()
{
  stopA();//Stop the left rear wheel rotation
  stopB();//Stop the right rear wheel rotation
}

void stopA()
{
  analogWrite(ENA, LOW);//Input low level to ENA
  digitalWrite(inPinN1,LOW);//Input low level to N1
  digitalWrite(inPinN2,LOW);//Input low level to N2
}

void stopB()
{
  analogWrite(ENB, LOW);//Input low level to ENB
  digitalWrite(inPinN3,LOW);//Input low level to N3
  digitalWrite(inPinN4,LOW);//Input low level to N4
}

//value:0~255
//PWM regulation of reverse speed
void backwardPwd(int valueA,int valueB)//Initialize the servo to the 90 degree position
{
  myservo.write(90); //Initialize the servo to the 90 degree position
  delay(500);//delay 0.5 second
  backwardPwdA(valueA);//Left rear wheel backward
  backwardPwdB(valueB);//Right rear wheel backward
}

//Left rear wheel
void backwardPwdA(int value)
{
  analogWrite(ENA, value);//Input PWM signal to ENA
  digitalWrite(inPinN1, LOW);//Input low level to N1
  digitalWrite(inPinN2, HIGH);//Input high level to N2
}
//Right rear wheel
void backwardPwdB(int value)
{
  analogWrite(ENB, value);//Input PWM signal to ENB
  digitalWrite(inPinN3, LOW);//Input low level to N3
  digitalWrite(inPinN4, HIGH);//Input high level to N4
}

//Left front movement
void forwardLeft(int value)
{
  myservo.write(120);  //Turn the front wheel steering axis to the left by 30 degrees
  delay(1000);//delay 1 second
  forwardPwmA(value);//Left rear wheel forward
  forwardPwmB(value);//Right rear wheel forward
}

//Right front movement
void forwardRight(int value)
{
  myservo.write(60); //Turn the front wheel steering axis to the right by 30 degrees
  delay(1000);//delay 1 second
  forwardPwmA(value);//Left rear wheel forward
  forwardPwmB(value);//Right rear wheel forward
}
