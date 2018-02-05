
function removeFromArray(arr, elt) {
  for(var i = arr.length -1; i >= 0; i--) {
    if(arr[i] == elt) {
      arr.splice(i, 1);
    }
  }
}

function heuristic(a, b) {
  var d = dist(a.i, a.j, b.i, b.j);
  return d;
}

let cols = 25;
let rows = 25;
var grid = new Array(cols, rows, 0);
var w, h;
var x;
var y;
var path = [];

var openSet = []
var closedSet = []

var start;
var end;

function Spot(i, j) {
  this.f = 0;
  this.g = 0;
  this.h = 0;
  this.i = i;
  this.j = j;
  this.neighbors = [];
  this.previous = undefined;

  this.show = function(col){
    fill(col);
    noStroke();
    rect(this.i * w, this.j * h, w - 1, h - 1);
  }

  this.addNeighbors = function(grid) {
    var i = this.i;
    var j = this.j;
    if(i < cols-1){
      this.neighbors.push(grid[i+1][j]);
    }
    if(i > 0) {
      this.neighbors.push(grid[i-1][j]);
    }
    if(j < rows -1) {
      this.neighbors.push(grid[i][j+1]);
    }
    if(j > 0) {
      this.neighbors.push(grid[i][j-1]);
    }
  }
}

function setup() {
  console.log("A*");
  createCanvas(400,400);

  w = width / cols;
  h = height / rows;

  for(var i = 0; i < cols; i++) {
    grid[i] = [];
    for(var j = 0; j < rows; j++)
    {
      grid[i][j] = new Spot(i, j);
    }
  }

  for(var i = 0; i < cols; i++) {
    for(var j = 0; j < rows; j++)
    {
      grid[i][j].addNeighbors(grid);
    }
  }

  start = grid[0][0];
  end = grid[rows-1][cols-1];

  openSet.push(start);
  console.log(grid);
}

function draw() {

  if(openSet.length > 0){
    //Can keep going
    var winner = 0;
    for(var i = 0; i < openSet.length; i++) {
      if(openSet[i].f < openSet[winner].f) {
        winner = i;
      }
    }
    var current = openSet[winner];
    if(current == end) {
      var temp = current;
      path.push(temp);
      while(temp.previous)
      {
        path.push(temp.previous);
        temp = temp.previous;
      }
      console.log("Done!");
    }

    removeFromArray(openSet, current);
    closedSet.push(current)

    var neighbors = current.neighbors;
    for(var i = 0; i < neighbors.length; i++){
      var neighbor = neighbors[i];

      if(!closedSet.includes(neighbor)) {
          var tempg = current.g + 1;

          if(openSet.includes(neighbor))
          {
            if(tempg < neighbor.g) {
              neighbor.g = tempg;
            }
          }
          else {
            neighbor.g = tempg;
            openSet.push(neighbor);
          }

          neighbor.h = heuristic(neighbor, end);
          neighbor.f = neighbor.g + neighbor.h;
          neighbor.previous = current;

      }

    }
  } else {
    // no solution
  }

  background(0);

  for(var i = 0; i < cols; i++) {
    for(var j = 0; j < rows; j++) {
      grid[i][j].show(color(255));
    }
  }

  for(var i = 0; i < closedSet.length; i++)
  {
    closedSet[i].show(color(255,0,0));
  }

  for(var i = 0; i < openSet.length; i++)
  {
    openSet[i].show(color(0, 255, 0));
  }

  for(var i = 0; i < path-length; i++) {
    path[i].show(color(0, 0, 255));
  }

}
