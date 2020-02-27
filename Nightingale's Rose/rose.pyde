months = ['Apr 1854','May 1854','Jun 1854','Jul 1854','Aug 1854','Sep 1854','Oct 1854','Nov 1854','Dec 1854','Jan 1855','Feb 1855','Mar 1855','Apr 1855','May 1855','Jun 1855','Jul 1855','Aug 1855','Sep 1855','Oct 1855','Nov 1855','Dec 1855','Jan 1856','Feb 1856','Mar 1856'];
diseases=[1.4,6.2,4.7,150,228.5,212.2,197,240.6,331.5,422.8,322.8,180.3,  177.5,171.8,247.6,107.5,129.9,47.5,32.8,56.4,25.3,11.4,6.6,3.9]
wounds=[50,70,30,20,70.4,82.1,151.7,115.8,41.7,30.7,16.3,12.8,  17.9,16.6,64.5,37.7,44.1,69.4,13.6,10.5,5,0.5,0,0]
others=[27,34.6,2.5,9.6,11.9,27.7,50.1,142.8,198,120,140.1,68.6,  21.2,12.5,9.6,9.3,6.7,5,4.6,10.1,7.8,113,85.2,49.1]



def scaled(x,starts,m):
    scaleMax=max(max(diseases[starts:starts+12]),max(wounds[starts:starts+12]),max(others[starts:starts+12]))
    return map(x,0,scaleMax,0,600)

def pieChart(x,y,Year,lastAngle):
  if Year==1:
      starts=0
      factor=1.6
  else:
      starts=12
      factor=0.9
  for i in range(starts,starts+12):
    noStroke();
    stroke(127,127,127)
    strokeWeight(1.5);
    fill(153,153,255,150);
    arc(x,y, factor*scaled(diseases[i],starts,"d"), factor*scaled(diseases[i],starts,"d"), lastAngle, lastAngle+(PI/6),PIE);
    fill(255,51,153,150);
    arc(x,y, factor*scaled(others[i],starts,"o"), factor*scaled(others[i],starts,"o"), lastAngle, lastAngle+(PI/6),PIE);
    fill(0,153,153,150);
    arc(x,y, factor*scaled(wounds[i],starts,"w"), factor*scaled(wounds[i],starts,"w"), lastAngle, lastAngle+(PI/6),PIE);
    lastAngle += (PI/6);
    
  for i in range(len(months)/2):
    rad=max(scaled(diseases[i],starts,"d"),scaled(wounds[i],starts,"w"),scaled(others[i],starts,"o"))
    if Year==1:
        factor=200
    else:
        factor=150
    text_x=x+factor*cos(lastAngle+PI/12)
    text_y=y+factor*sin(lastAngle+PI/12)
    fill(100);
    text(months[i][0:3], text_x, text_y,50,50 )
        
    lastAngle += (PI/6);
  
def setup(): 
    size(1800, 1000)
    frameRate(1)

Angle=PI        
def draw(): 

  noStroke();
  # noLoop();
  background(loadImage('bg.jpg'))
  
  global Angle
  Angle+=PI/6
  
  #make the charts
  pieChart(x=1200,y=480,Year=1,lastAngle=Angle)         #chart 1
  pieChart(x=450,y=350,Year=2,lastAngle=Angle+4*PI/3)   #chart 2

  #chart headings
  textSize(42);
  head="Causes of Mortality in the Army in the East"
  text(head,width/2 - textWidth(head)/2,40)
  textSize(22);
  text("April 1855 to March 1856",300,100)
  textSize(22);
  text("April 1854 to March 1855",1150,100)

  #legend
  fill(255,255,255)
  stroke(170,170,170)
  rect(300,890,1200,50)
  fill(153,153,255,150);
  rect(350,900, 30, 30);
  fill(255,51,153,150);
  rect(750,900, 30,30);
  fill(0,153,153,150);
  rect(1150,900,30,30);
  fill(0);
  textSize(15);
  fill(70);
  text("Zymotic diseases", 390,915);
  text("Wounds & injuries",790,915);
  text("All other causes", 1190,915);
  fill(70)
  text("*Data modified from original for better visualization",1300,980)
  

    
