cities,city,city_lat,city_lon=[],[],[],[]
temps,temp_lon,temp,temp_days,temp_mon,temp_day=[],[],[],[],[],[]
marches,lonp,latp,surv,dir,divn=[],[],[],[],[],[]
os.chdir('C:/Users/nishant/Documents/Data Viz/1.2/minard')

# read geocode
with open("data_geo.csv") as f:
  content = f.read().splitlines()
# global city,city_lat,city_lon
for l in content:
  cities.append(l.split(","))

city.append([item[2] for item in cities])
city=city[0][1:]
city_lat.append([item[1] for item in cities])
city_lat=city_lat[0][1:]
city_lat=[float(x) for x in city_lat]
city_lon.append([item[0] for item in cities])
city_lon=city_lon[0][1:]
city_lon=[float(x) for x in city_lon]

# read temperature        
with open("data_temp.csv") as f:
  content = f.read().splitlines()
# global temp_lon,temp,temp_days,temp_mon,temp_day
for l in content:
  temps.append(l.split(","))

temp_lon.append([item[0] for item in temps])
temp_lon=temp_lon[0][1:]
temp_lon=[float(x) for x in temp_lon]
temp.append([item[1] for item in temps])
temp=temp[0][1:]
temp=[float(x) for x in temp]
temp_days.append([item[2] for item in temps])
temp_days=temp_days[0][1:]
temp_days=[float(x) for x in temp_days]
temp_mon.append([item[3] for item in temps])
temp_mon=temp_mon[0][1:]
temp_day.append([item[4] for item in temps])
temp_day=temp_day[0][1:]
# temp_day=[float(x) for x in temp_day]

# read marching        
with open("data_marching.csv") as f:
  content = f.read().splitlines()
# global lonp,latp,surv,dir,divn
for l in content:
  marches.append(l.split(","))

lonp.append([item[0] for item in marches])
lonp=lonp[0][1:]
lonp=[float(x) for x in lonp]
latp.append([item[1] for item in marches])
latp=latp[0][1:]
latp=[float(x) for x in latp]
surv.append([item[2] for item in marches])
surv=surv[0][1:]
surv=[float(x) for x in surv]
dir.append([item[3] for item in marches])
dir=dir[0][1:]
divn.append([item[4] for item in marches])
divn=divn[0][1:]
divn=[float(x) for x in divn]



def setup():
    size(1800,1000);
    background(255);
    #noStroke();
    # noLoop();
    frameRate(100);

def scaleIt(x,feature,axis):
    if axis=='x':
        return ((x-min(feature))*1300/(max(feature)-min(feature)))+200
    else: 
        return height-((x-min(feature))*300/(max(feature)-min(feature)))-500
        
def draw():

    background(loadImage('bg1.jpg'))
    
# write viz heading
    fill(100)
    textSize(50)
    head="MINARD'S MAP OF NAPOLEON'S RUSSIA CAMPAIGN"
    text(head, width/2 - textWidth(head)/2,100)
            
# draw path
    for i in range(0,47):
        x_from=scaleIt(lonp[i],lonp,'x')
        y_from=scaleIt(latp[i],latp,'y')
        x_to=scaleIt(lonp[i+1],lonp,'x')
        y_to=scaleIt(latp[i+1],latp,'y')
        strokeWeight((surv[i]*50.0)/max(surv))
        strokeJoin(ROUND);
        
        if divn[i]==1:
            stroke(148,0,211,120)
        elif divn[i]==2:
            stroke(255,153,51,180)
        else:
            stroke(0,204,102,120)
        # delay(10);
        line(x_from,y_from,x_to,y_to)

# write city name at appropriate coordinate
    for i,c in enumerate(city):
        x=scaleIt(city_lon[i],city_lon,'x')
        y=scaleIt(city_lat[i],city_lat,'y')
        # print x,y
        fill(250)
        stroke(150)
        circle(x,y,10)
        fill(50)
        textSize(15)
        text(c, x+10,y+5)

#legend
    strokeWeight(3)
    stroke(150)
    fill(255,255,255,0)
    rect(1540,340,150,150)
    noStroke()
    fill(148,0,211);
    rect(1550, 350, 30,30);
    fill(255,153,51);
    rect(1550,400, 30,30);
    fill(0,204,102);
    rect(1550,450,30,30);
    # fill(0);
    textSize(15);
    fill(70);
    text("Divison 1", 1590,370);
    text("Divison 2", 1590,420);
    text("Divison 3", 1590,470);

# draw temp
    textSize(130)
    fill(200)
    text("Temperature (C)",350,750)
    strokeWeight(10);
    strokeJoin(ROUND);
    stroke(98, 252, 134, 150);
    
    for i in range(0,len(temp)-1):
        x_from=scaleIt(temp_lon[i],temp_lon,'x')
        y_from=scaleIt(temp[i],temp,'y')+400
        x_to=scaleIt(temp_lon[i+1],temp_lon,'x')
        y_to=scaleIt(temp[i+1],temp,'y')+400
        stroke(255,69,0,100)
        strokeWeight(temp[i]+40)
        line(x_from,y_from,x_to,y_to);
        fill(50);
        textSize(15);
        text(str(temp[i])[0:3]+'C',x_from,y_from);
                        
