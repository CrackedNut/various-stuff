function setup() {
  createCanvas(400, 400, WEBGL);
  frameRate(60);
}

function draw() {
  background(0);
  rotateX(millis() * 0.001);
  rotateY(millis() * 0.001);
  rotateY(millis() * 0.001);
  box(50, 50, 50);

}
