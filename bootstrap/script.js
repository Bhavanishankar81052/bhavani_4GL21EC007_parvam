const header = document.querySelector("header");

window.addeventListener("Scroll",function(){
    header.classlist.toggle("sticky",window.scrollY > 0);
});

let menu = document.querySelector('#menu-icon');
let navbar= document.querySelector('.navbar');

menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navbar.classList.open('bx-x');
};
window.onscroll = () => {
    menu.classList.remove('bx-x');
    navbar.classList.remove('bx-x');

}


