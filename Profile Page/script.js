
function addShadow(element){
    element.classList.add ("shadow");
}
function removeShadow(element){
    element.classList.remove ("shadow");
}
function profileColor(element){
var x, y, z, random_col;
x = Math.round(Math.random()*256);
y = Math.round(Math.random()*256);
z = Math.round(Math.random()*256);
random_col = 'rgb('+x+','+y+','+z+')';

document.getElementById("profile-title").style.color= random_col;
}

function counter(){
    var num = document.getElementById("counting").innerHTML;
    num ++;
    document.getElementById("counting").innerHTML = num;
}