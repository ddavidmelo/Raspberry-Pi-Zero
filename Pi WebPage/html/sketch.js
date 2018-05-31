//https://processing.org/reference/


// document.write('<p>Your viewport width is '+viewportwidth+'x'+viewportheight+'</p>');

var Wsize = getWindowSize();

var cols, rows;
var wOffSet = Wsize[0] * 0.3; var hOffSet = - Wsize[1] / 4;
var w = Wsize[0] + wOffSet;
var h = Wsize[1] + hOffSet;
var scl = (w * h) / 61196; // scale of blocks
var flying = 0;

var terrain = [];

function setup() {

  var canvas = document.getElementById("canvasScript");


  createCanvas(Wsize[0], Wsize[1], WEBGL);


  setAttributes('antialias', true);
  cols = w / scl;
  rows = h / scl;
  frameRate(8);
  for (var x = 0; x < cols; x++) {
    terrain[x] = [];
    for (var y = 0; y < rows; y++) {
      terrain[x][y] = 0; //specify a default value for now
    }
  }
}

function draw() {

  flying -= 0.01;
  var yoff = flying;
  for (var x = 0; x < cols; x++) {
    var xoff = 0;
    for (var y = 0; y < rows; y++) {
      terrain[x][y] = map(noise(xoff, yoff), 1, 0, -50, 50);
      xoff += 0.2;
    }
    yoff += 0.2;
  }


  background(0);
  stroke(175);
  //Draw boat
  for (var y = 0; y < rows-1; y=y+2) 
  {
    var u = terrain[0][y];
  }
  DrawBoat(u/2);
  //End draw boat

  //Draw waves
  noFill();
  rotateX(PI/3);
  translate(-w/2 , -h/4);
  for (var y = 0; y < rows-1; y++) {
    beginShape(TRIANGLE_STRIP);
    for (var x = 0; x < cols; x++) {
      vertex(x*scl, y*scl, terrain[x][y]);
      vertex(x*scl, (y+1)*scl, terrain[x][y+1]);
    }
    endShape();
  }
  //End draw waves

 
}

function DrawBoat(u)
{
  //boat
  XOffSetBoat = 0;
  YOffSetBoat = 70+u;
  fill(255,255,255,255); // r,g,b,opacity
  beginShape();
    vertex(-100, -100 + YOffSetBoat);
    vertex(100, -100 + YOffSetBoat);
    vertex(150, -155 + YOffSetBoat);
    vertex(-150, -155 + YOffSetBoat);
  endShape(CLOSE);
  
  line(0, -155 + YOffSetBoat, 0, -200 + YOffSetBoat);

  beginShape();
    vertex(0, -200 + YOffSetBoat);
    vertex(100, -200 + YOffSetBoat);
    vertex(0, -340 + YOffSetBoat);
  endShape(CLOSE);
  //end of the boat
}

function getWindowSize()
{
  var viewportwidth;
  var viewportheight;
  // the more standards compliant browsers (mozilla/netscape/opera/IE7) use window.innerWidth and window.innerHeight

  if (typeof window.innerWidth != 'undefined')
  {
      viewportwidth = window.innerWidth,
      viewportheight = window.innerHeight
  }

  // IE6 in standards compliant mode (i.e. with a valid doctype as the first line in the document)

  else if (typeof document.documentElement != 'undefined'
     && typeof document.documentElement.clientWidth !=
     'undefined' && document.documentElement.clientWidth != 0)
  {
       viewportwidth = document.documentElement.clientWidth,
       viewportheight = document.documentElement.clientHeight
  }

  // older versions of IE

  else
  {
       viewportwidth = document.getElementsByTagName('body')[0].clientWidth,
       viewportheight = document.getElementsByTagName('body')[0].clientHeight
  }
  // document.write('<p>Your viewport width is '+viewportwidth+'x'+viewportheight+'</p>');
  return [viewportwidth,viewportheight];

}
