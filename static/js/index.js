const showModels = (clicked_id) =>{
    document.getElementsByClassName(clicked_id)[0].style.display = "block";
}

const closeModels = () =>{
    document.getElementsByClassName("models").style.display = "none";
}

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