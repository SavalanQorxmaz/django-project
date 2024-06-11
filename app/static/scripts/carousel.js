

const carousel = document.getElementById('carousel')


let carouselItems =[]
if(carousel){
    carouselItems = Array.from(carousel.children[0].children)
}


carouselItems.forEach(item=>{
    item.style.width = `${document.documentElement.clientWidth}px`
    // console.log(item.clientWidth)
})

window.addEventListener('resize',()=>{
    carousel.style.width = `${document.documentElement.clientWidth}px`
    carousel.children[0].scrollLeft = 0
    // console.log(carousel.clientWidth)
    carouselItems.forEach(item=>{
        item.style.width = `${document.documentElement.clientWidth}px`
       
    })
})

let date = new Date()

let time  = new Date().getTime()
let newTime = new Date().getTime()
const carouselEvent =()=>{
    newTime++
 if(carousel){
    if(newTime - time >500){
        
        time = newTime
        carousel.children[0].scrollLeft += document.documentElement.clientWidth
        if(carousel.children[0].scrollWidth - carousel.children[0].scrollLeft-10  <= document.documentElement.clientWidth){
            carousel.children[0].scrollLeft = 0
        }
        
    }
 }
    requestAnimationFrame(carouselEvent)
}
requestAnimationFrame(carouselEvent)


carousel?.addEventListener('click', (e)=>{
    e.stopPropagation()
    console.log(e.currentTarget)
    console.log(e.target)
})
