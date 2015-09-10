#include <Servo.h>
 
Servo myservo;
             
 
int pos = 0; 
int led = 10;
int distance = 0;

int sensorPin = 5; // ultrasonic range finder
 
void setup()
{
  myservo.attach(9);
  pinMode(led, OUTPUT);  
  Serial.begin(9600);
  myservo.write(10);
}
 
 
void loop()
{
 
  distance = analogRead(sensorPin);
 
  Serial.println(distance);
 
  delay(20);
 
  react(distance);

 
 
}

void react(int distance)
{
 
 
 if(distance < 10){
   
    myservo.write(100);
    blink();
    myservo.write(10);
    delay(20);
   
  }else{
    myservo.write(10);
   
  }

  //blink();
 
 
 
}


void blink()
{
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(150);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(150); 
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(150);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(150);
}
