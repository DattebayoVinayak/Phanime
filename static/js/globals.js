let menuBtn = document.querySelector('.menu-btn');
let menu = document.querySelector('.menu')
let closeBtn = document.querySelector('.close-menu');

let menuLinks = document.querySelectorAll('.menuLink')

menuBtn.addEventListener('click',()=>{
  menu.style.display = 'flex';
})

closeBtn.addEventListener('click',()=>{
  menu.style.display = 'none';
})

menuLinks.forEach((menuLink)=>{
  let smenu = menuLink.nextElementSibling;
  menuLink.addEventListener('click',()=>{
    smenu.style.display = 'flex';
  })
  menuLink.addEventListener('mouseout',()=>{
    smenu.style.display = 'none';
  })
  smenu.addEventListener('mouseover',()=>{
    smenu.style.display = 'flex';
  })
  smenu.addEventListener('mouseout',()=>{
    smenu.style.display = 'none';
  })
});
