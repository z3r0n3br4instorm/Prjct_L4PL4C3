const int analogInputPin = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  randomSeed(analogRead(analogInputPin));

}

void loop() {
  // put your main code here, to run repeatedly:
  int noiseValue = analogRead(analogInputPin);
  int randomNumber= random(0,255);

  Serial.print("Noise Value :");
  Serial.print(noiseValue);
  Serial.print("\nRandom Number :");
  Serial.println(randomNumber);

}
