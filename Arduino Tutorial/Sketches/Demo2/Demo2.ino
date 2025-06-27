/**********************************************************************
  Product     : Cokoino Real-Wheel Drive Steering Car Chassis kit
  Auther      : www.cokoino.com
  Modification: 2025/04/23
**********************************************************************/
#include<Servo.h>
Servo myservo;  // Create a servo class
#include <AFMotor.h>
AF_DCMotor motor1(1);//define motor1
AF_DCMotor motor2(2);//define motor2
AF_DCMotor motor3(3);//define motor3
AF_DCMotor motor4(4);//define motor4


void setup() 
{
 myservo.attach(9);  //Set the servo control pin as D9
 myservo.write(90);  //The servo is 90 degrees
}

void loop() 
{
  motor2.setSpeed(200);//setup the speed of motor1
  //motor2.setSpeed(200);//setup the speed of motor2
  motor3.setSpeed(200);//setup the speed of motor3
  //motor4.setSpeed(200);//setup the speed of motor4
  //car move forward
  motor2.run(FORWARD);//motor1 run BACKWARD
  //motor2.run(FORWARD); //motor2 run FORWARD
  motor3.run(FORWARD);//motor3 run BACKWARD
  //motor4.run(FORWARD); //motor4 run FORWARD
  delay(2000);
  motor2.run(RELEASE);// motor1 stop run
 // motor2.run(RELEASE);// motor2 stop run
  motor3.run(RELEASE);// motor3 stop run
  //motor4.run(RELEASE);// motor4 stop run
  delay(1000);
   //car move backward
  motor2.run(BACKWARD);// motor1 run FORWARD
  //motor2.run(BACKWARD);//motor2 run BACKWARD
  motor3.run(BACKWARD);// motor3 run FORWARD
 // motor4.run(BACKWARD);//motor4 run BACKWARD
  delay(2000);
  motor2.run(RELEASE);
  //motor2.run(RELEASE);
  motor3.run(RELEASE);
  //motor4.run(RELEASE);
  delay(1000);
  //car move forward and turn left
  motor2.setSpeed(200);///setup the speed of motor1
  //motor2.setSpeed(200);//setup the speed of motor2
  motor3.setSpeed(200);///setup the speed of motor3
  //motor4.setSpeed(100);//setup the speed of motor4
  myservo.write(60);  //The servo is 90 degrees
  delay(500);
  motor2.run(FORWARD);//motor1 run BACKWARD
  //motor2.run(FORWARD); //motor2 run FORWARD
  motor3.run(FORWARD);//motor3 run BACKWARD
  //
  //motor4.run(FORWARD); //motor4 run FORWARD
  delay(500);
  motor2.run(RELEASE);
  //motor2.run(RELEASE);
  motor3.run(RELEASE);
  //motor4.run(RELEASE);
  myservo.write(90);
  delay(1000);
   //car move forward and turn right
  motor2.setSpeed(200);///setup the speed of motor1
  //motor2.setSpeed(100);//setup the speed of motor2
  motor3.setSpeed(200);///setup the speed of motor3
 // motor4.setSpeed(200);//setup the speed of motor4
  myservo.write(120);  //The servo is 90 degrees
  delay(500);
  motor2.run(FORWARD);//motor1 run BACKWARD
  //motor2.run(FORWARD); //motor2 run FORWARD
  motor3.run(FORWARD);//motor3 run BACKWARD
  //motor4.run(FORWARD); //motor4 run FORWARD
  delay(500);
  motor2.run(RELEASE);
  //motor2.run(RELEASE);
  motor3.run(RELEASE);
  //motor4.run(RELEASE);
  myservo.write(90);
  delay(500);
}
