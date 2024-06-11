const contactsIcon = document.getElementById('contacts-icon')
const contacts = document.getElementById('contacts')
const backToTop = document.getElementById('back-to-top')


    // if(contacts.classList.contains('contacts-show'))
    contactsIcon.addEventListener('click',(e)=>{
        e.preventDefault()
        if(contacts.classList.contains('contacts-show')&& e.target.classList.contains('contacts-icon-close')){
            contacts.classList.remove('contacts-show')
            contacts.classList.add('contacts-hide')
            e.target.classList.remove('contacts-icon-close')
            e.target.classList.add('contacts-icon-open')
            contactsIcon.innerHTML = ' &#9742;'
            document.body.style.overflow = 'auto'
            if(backToTop.classList.contains('back-to-top-hide') && document.documentElement.scrollTop>100){
                backToTop.classList.add('back-to-top-show')
                backToTop.classList.remove('back-to-top-hide')
            }
        }
        else {
        
            contacts.classList.remove('contacts-hide')
            contacts.classList.add('contacts-show') 
            e.target.classList.add('contacts-icon-close')
            e.target.classList.remove('contacts-icon-open')
            contactsIcon.innerHTML = '&#x2718;'
    
            document.body.style.overflow = 'hidden'
            if(backToTop.classList.contains('back-to-top-show')){
                backToTop.classList.remove('back-to-top-show')
                backToTop.classList.add('back-to-top-hide')
            }
        }
     
     }  )

window.addEventListener('scroll',(e)=>{
    if(document.documentElement.scrollTop>200 && contacts.classList.contains('contacts-hide')){
        backToTop.classList.remove('back-to-top-hide')
        backToTop.classList.add('back-to-top-show')

    }
    else{
        backToTop.classList.remove('back-to-top-show')
        backToTop.classList.add('back-to-top-hide')
    }

})

backToTop.addEventListener('click',(e)=>{
    e.preventDefault()
    document.documentElement.scrollTop = 0
})