const showModels = (clicked_id) =>{
    document.getElementsByClassName(clicked_id)[0].style.display = "block";
}

const closeModels = () =>{
    let array = document.getElementsByClassName("models");
    for(let i = 0; i <array.length; i++){
       array[i].style.display = "none";
    }

}


const closeModelsD = () =>{
    let array = document.getElementsByClassName("models");
    for(let i = 0; i <array.length; i++){
       array[i].style.display = "none";
    }
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