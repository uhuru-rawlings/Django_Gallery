const Indicator = () =>{
    let targets = document.getElementById("indicator");
    if(targets.style.display == "block"){
        targets.style.display = "none"
    }else{
        targets.style.display = "block"
    }
    setTimeout(Indicator, 1000)
}
window.onload = Indicator;