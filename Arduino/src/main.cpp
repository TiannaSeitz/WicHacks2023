#include <Arduino.h>

int switch_pin = 2;
int button_1_pin = 3;
int button_2_pin = 4;
int LED_R_pin = 5;
int LED_B_pin = 6;
int LED_G_pin = 7;
int output_pin = 8;

int switch_state = 0;
int button_1_state = 0;
int button_2_state = 0;

void SOS(int message);

void setup() 
{
  Serial.begin(9600);

  pinMode(switch_pin, INPUT);
  pinMode(button_1_pin, INPUT);
  pinMode(button_2_pin, INPUT);
  pinMode(LED_R_pin, OUTPUT);
  pinMode(LED_B_pin, OUTPUT);
  pinMode(LED_G_pin, OUTPUT);
  pinMode(output_pin, OUTPUT);
  
  digitalWrite(LED_R_pin, 0);
  digitalWrite(LED_B_pin, 0);
  digitalWrite(LED_G_pin, 0);

  digitalWrite(output_pin, 0);
}

void loop() 
{
  
  while(digitalRead(switch_pin) == 0)
  {
    delay(1000);
    digitalWrite(LED_G_pin, 1);
    digitalWrite(LED_R_pin, 0);
  }
  digitalWrite(LED_R_pin, 1);
  digitalWrite(LED_G_pin, 0);

  delay(100);

  button_1_state = digitalRead(button_1_pin);
  Serial.print(button_1_state);

  button_2_state = digitalRead(button_2_pin);
  Serial.println(button_2_state);

  if(button_1_state == 1)
  {
    delay(1000);
    button_2_state = digitalRead(button_2_pin);
    if(button_2_state == 1)
    {
      SOS(3);
    }
    else
    {
      SOS(1);
    }
  }
  else if(button_2_state == 1)
  {
    delay(1000);
    button_1_state = digitalRead(button_1_pin);
    if(button_1_state == 1)
    {
      SOS(3);
    }
    else
    {
      SOS(2);
    }
  }

}

void SOS(int message) //1 = escort to car (button 1), 2 = call a cab (button 2), 3 = call police (both buttons)
{
  if(message == 1)
  {
    digitalWrite(LED_B_pin, 1);
    digitalWrite(LED_G_pin, 0);
    digitalWrite(LED_R_pin, 0);
    while(1)
    {
      Serial.println("signal 1");
      digitalWrite(output_pin, 1);
      delay(25);
      digitalWrite(output_pin, 0);
      delay(25);
    }
  }
  
  if(message == 2)
  {
    digitalWrite(LED_B_pin, 1);
    digitalWrite(LED_G_pin, 1);
    digitalWrite(LED_R_pin, 0);
    while(1)
    {
      Serial.println("signal 2");
      digitalWrite(output_pin, 1);
      delay(50);
      digitalWrite(output_pin, 0);
      delay(50);
    }
  }

  if(message == 3)
  {
    digitalWrite(LED_B_pin, 0);
    digitalWrite(LED_G_pin, 0);
    digitalWrite(LED_R_pin, 0);
    while(1)
    {
      Serial.println("signal 3");
      digitalWrite(output_pin, 1);
      delay(100);
      digitalWrite(output_pin, 0);
      delay(100);
    }
  }
}