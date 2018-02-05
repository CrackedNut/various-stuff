let pointc = 53;

function rpoint(x, y) {
  this.x = x;
  this.y = y;
  point(this.x, this.y);
  this.pos = function() {
    return this.position();
  }
}

function setup() {
  createCanvas(400, 400);
  angleMode(DEGREES);
}

function draw() {
  translate(200, 200);
  background(0);
  push();
  noFill();
  stroke(200);
  strokeWeight(2);
  ellipse(0, 0, 150, 150);
  pop();
  stroke(255);
  strokeWeight(15);
  push();
  rotate(frameCount * 0.1);
  let point1 = new rpoint(pointc, pointc);
  pop();
  push();
  rotate(frameCount * 0.5);
  let point2 = new rpoint(pointc, pointc);
  pop();

  console.log(point2.pos());
}
