// Define the pins connected to the OSOYOO module
#define IN1 6   // Motor A direction pin 1
#define IN2 7   // Motor A direction pin 2
#define ENA 5   // Motor A enable pin (PWM speed control)

#define IN1B 11   // Motor B direction pin 1
#define IN2B 12   // Motor B direction pin 2
#define ENAB 10   // Motor B enable pin (PWM speed control)

void setup() {
  // Set the control pins as outputs
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);

  pinMode(IN1B, OUTPUT);
  pinMode(IN2B, OUTPUT);
  pinMode(ENAB, OUTPUT);

  // Initialize motor to stop
  stopMotor();

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String receivedData = Serial.readStringUntil('\n'); // Read until newline character
    if (receivedData == "in") {
      rotateClockwise(255);
    } else if (receivedData == "out") {
      rotateCounterClockwise(255);
    } else if (receivedData == "stop") {
      stopMotor();
    }
  }

  
}

// Function to rotate the motor clockwise with speed control (0-255)
void rotateClockwise(int speed) {
  digitalWrite(IN1, HIGH);  // Set IN1 High
  digitalWrite(IN2, LOW);   // Set IN2 Low
  analogWrite(ENA, speed);  // Enable motor with specified speed
  digitalWrite(IN1B, HIGH);  // Set IN1 High
  digitalWrite(IN2B, LOW);   // Set IN2 Low
  analogWrite(ENAB, speed);  // Enable motor with specified speed
}

// Function to rotate the motor counter-clockwise with speed control (0-255)
void rotateCounterClockwise(int speed) {
  digitalWrite(IN1, LOW);   // Set IN1 Low
  digitalWrite(IN2, HIGH);  // Set IN2 High
  analogWrite(ENA, speed);  // Enable motor with specified speed
  digitalWrite(IN1B, LOW);   // Set IN1 Low
  digitalWrite(IN2B, HIGH);  // Set IN2 High
  analogWrite(ENAB, speed);  // Enable motor with specified speed
}

// Function to stop the motor (free stop state)
void stopMotor() {
  // Alternatively, setting both IN1/IN2 to HIGH or LOW results in a brake state
  analogWrite(ENA, 0); // ENA signal 0 puts motor in free stop state
  analogWrite(ENAB, 0); // ENA signal 0 puts motor in free stop state
}