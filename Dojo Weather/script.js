function scheduleA(event) {
        alert(this.options[this.selectedIndex].text);
}
function addShadow(element){
    element.classList.add ("shadow");
}
function removeShadow(element){
    element.classList.remove ("shadow");
}
function acceptclose()  {
    document.getElementById("cookiejar").style.display = 'none';
}
var hitemp = document.querySelector("#hitemp").innerHTML
var hitemp2 = document.querySelector("#hitemp2").innerHTML
var hitemp3 = document.querySelector("#hitemp3").innerHTML
var hitemp4 = document.querySelector("#hitemp4").innerHTML
var lowtemp = document.querySelector("#lowtemp").innerHTML
var lowtemp2 = document.querySelector("#lowtemp2").innerHTML
var lowtemp3 = document.querySelector("#lowtemp3").innerHTML
var lowtemp4 = document.querySelector("#lowtemp4").innerHTML

function calculatetemps(){
    var x = document.getElementById("temp").selectedIndex;
    if(x === 1){
    document.querySelector("#hitemp").innerHTML = (Math.round(hitemp * (9/5) + 32));
    document.querySelector("#hitemp2").innerHTML = (Math.round(hitemp2 * (9/5) + 32));
    document.querySelector("#hitemp3").innerHTML = (Math.round(hitemp3 * (9/5) + 32));
    document.querySelector("#hitemp4").innerHTML = (Math.round(hitemp4 * (9/5) + 32));
    document.querySelector("#lowtemp").innerHTML = (Math.round(lowtemp * (9/5) + 32));
    document.querySelector("#lowtemp2").innerHTML = (Math.round(lowtemp2 * (9/5) + 32));
    document.querySelector("#lowtemp3").innerHTML = (Math.round(lowtemp3 * (9/5) + 32));
    document.querySelector("#lowtemp4").innerHTML = (Math.round(lowtemp4 * (9/5) + 32));
    console.log(hitemp);
    console.log(hitemp2);
    console.log(hitemp3);
    console.log(hitemp4);
    console.log(lowtemp);
    console.log(lowtemp2);
    console.log(lowtemp3);
    console.log(lowtemp4);
    console.log(x);
    }
    if(x === 0){
    document.querySelector("#hitemp").i = hitemp;
    document.querySelector("#hitemp2").innerHTML = hitemp2;
    document.querySelector("#hitemp3").innerHTML = hitemp3;
    document.querySelector("#hitemp4").innerHTML = hitemp4;
    document.querySelector("#lowtemp").innerHTML = lowtemp;
    document.querySelector("#lowtemp2").innerHTML = lowtemp2;
    document.querySelector("#lowtemp3").innerHTML = lowtemp3;
    document.querySelector("#lowtemp4").innerHTML = lowtemp4;
    console.log(hitemp);
    console.log(hitemp2);
    console.log(hitemp3);
    console.log(hitemp4);
    console.log(lowtemp);
    console.log(lowtemp2);
    console.log(lowtemp3);
    console.log(lowtemp4);
    console.log(x);
    }

}