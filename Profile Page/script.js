
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
var username = document.querySelector(".brian");
function changeprofilename(){
    document.getElementById("brian").innerHTML = "Jane Doe";
}
var requests = document.getElementById("numrequests").innerHTML;
var connections = document.getElementById("numconnections").innerHTML;

function accepttodde(){
    document.getElementById("todde").style.display = 'none';
    requests--;
    connections++;
    document.getElementById("numrequests").innerHTML = requests;
    document.getElementById("numconnections").innerHTML = connections;
}
function acceptphilk(){
        document.getElementById("philk").style.display = 'none';
        requests--;
        connections++;
        document.getElementById("numrequests").innerHTML = requests;
        document.getElementById("numconnections").innerHTML = connections;
}
function closetodde(){
    document.getElementById("todde").style.display = 'none';
    requests--;
    document.getElementById("numrequests").innerHTML = requests;
}
function closephilk(){
        document.getElementById("philk").style.display = 'none';
        requests--;
        document.getElementById("numrequests").innerHTML = requests;
}
