let btn = document.querySelector(".icon-menu");
let navMenu =  document.querySelector(".header-menu-bg");
let menu = document.querySelector("#icon");
btn.addEventListener("click",()=>{
  clase = menu.getAttribute("class")
  if (clase === "fa-solid fa-bars") {
    navMenu.classList.add("show");
    menu.classList.replace("fa-solid","fa-solid")
    menu.classList.replace("fa-bars","fa-xmark")
  } else {
    navMenu.classList.remove("show");
    menu.classList.replace("fa-solid","fa-solid")
    menu.classList.replace("fa-xmark","fa-bars")
  }
})