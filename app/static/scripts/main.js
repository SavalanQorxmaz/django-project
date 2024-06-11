
import './carousel.js'
import './advanced.js'
import './header.js'

const analog = document.getElementById("analog");
const hour = document.getElementById("hour");
const minute = document.getElementById("minute")
const second = document.getElementById("second")


window.addEventListener('resize',()=>{
    window.innerWidth<772?document.body.style.backgroundColor = 'yellow':document.body.style.backgroundColor = 'green'
    
})


let deg = 0;
for(let i=0;i<30;i++){


    
    let line = document.createElement("div");
    line.classList.add("line")
 
    line.style.transform = `rotateZ(${deg}deg)`;
    
analog.appendChild(line)

  for(let j=0;j<2;j++){
    let lineChild = document.createElement("div");
    if(i%5 == 0){
         lineChild.classList.add("long-line");
         
     }else{
         lineChild.classList.add("short-line")
     }
 line.appendChild(lineChild)
  }

 
    deg +=6
}




function analogC(){


    const date = new Date();
    let milliSeconds = date.getMilliseconds();
    let seconds = date.getSeconds();
    let minutes = date.getMinutes();
    let hours = date.getHours();
    let year = date.getFullYear();
    let month = date.getMonth();
    let monthDay = date.getDate();
    let weekDay = date.getDay();

    // analog clock
    let secondPosition = 360 / 60 * seconds + 360 /60000 *milliSeconds;
    let minutePosition = 360 / 60 * minutes + seconds / 10;
    let analogHours = hours;
    if(hours >11){
        analogHours -= 12;
    }
    let hourPosition = 360 / 12 * analogHours + minutes / 12 * 6;

    hour.style.transform = `rotateZ(${hourPosition}deg)`
    minute.style.transform = `rotateZ(${minutePosition}deg)`
    second.style.transform = `rotateZ(${secondPosition}deg)`



requestAnimationFrame(analogC)

}

requestAnimationFrame(analogC)


const canvas = document.getElementById("load-canvas");
const ctx = canvas.getContext("2d");
let raf;

const line = {
  startX: 100,
  startY: 100,
  stopX: 106,
  stopY: 100,
  currentX: 100,
  currentY: 100,
  direction: 'x',
  color: "blue",
  draw() {
    ctx.moveTo(this.startX, this.startY)
    ctx.lineTo(this.currentX,this.currentY);
    ctx.stroke()
  },
};

function draw() {
    
  raf = window.requestAnimationFrame(draw);
  line.draw();


  switch(line.direction){
    case 'x':{
       
        if(line.currentX!=line.stopX){
                line.currentX-=Math.abs(line.startX-line.stopX)/(line.startX-line.stopX)*3
            
        }
        else{
            
            line.stopY+= line.stopX-line.startX -Math.abs(line.startX-line.stopX)/(line.startX-line.stopX)*6
            line.startX = line.stopX
            line.direction ='y'
        }
    }
    break;
    case 'y':{
        if(line.currentY!=line.stopY){
            line.currentY-=Math.abs(line.startY-line.stopY)/(line.startY-line.stopY)*3
        }
        else{
            line.stopX+= line.startY-line.stopY+Math.abs(line.startY-line.stopY)/(line.startY-line.stopY)*6
            if(line.stopX-line.startX>80){
                ctx.clearRect(0,0,200,200)
                
                ctx.beginPath()
                line.startX= 100
                line.startY= 100
                line.stopX= 103
                line.stopY= 100
                line.currentX= 103
                line.currentY= 103
                line.direction= 'x'
              
            }
            line.startY = line.stopY
            line.direction ='x'
        }
    }
    break;
    
  }

}

canvas.addEventListener("mouseover", (e) => {
  raf = window.requestAnimationFrame(draw);
});

// canvas.addEventListener("mouseout", (e) => {
//   window.cancelAnimationFrame(raf);
// });

// line.draw();
raf = window.requestAnimationFrame(draw);





window.addEventListener("load", (event) => {
    
    setTimeout(()=>{
    
        document.getElementById('load-cover').style.display= 'none'
    window.cancelAnimationFrame(raf);
    },1000)
  });




