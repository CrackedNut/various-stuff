var w;
var h;

function setup() {
	createCanvas(700, 700);
	angleMode(DEGREES);
	w = 0;
	h = 0;
}

function draw() {
	background(0);

	let hr = hour();
	let min = minute();
	let sc = second();

	translate(width/2, width/2);

	let sc1 = map(sc, 0, 60, 0, 360);
	let min1 = map(min, 0, 60, 0, 360);
	let hr1 = map(hr % 12, 0, 12, 0, 360);

	push();
	rotate(sc1-90);
	stroke(255, 150, 100);
	line(0, 0, 125, 0);
	pop();

	push();
	rotate(min1-90);
	stroke(100, 255, 150);
	line(0, 0, 75, 0);
	pop();

	push();
	rotate(hr1-90);
	stroke(150, 100, 255);
	line(0, 0, 50, 0);
	pop();

	rotate(-90);
	noFill()
	strokeWeight(10);

	stroke(255, 150, 100);
	arc(w, h, width/2, width/2, 0, sc1);

	stroke(100, 255, 150);
	arc(w, h, width/2.15, width/2.15, 0, min1);

	stroke(150, 100, 255);
	arc(w, h, width/2.325, width/2.325, 0, hr1);

	stroke(255);
	point(0,0);
}
