active = false
navigation_container = document.getElementById("navigation-container")

function showMenu(){
    if (active == false){
            navigation_container.style.transition = "all 2s";
            navigation_container.style.display = "inline";
            active = true      
    }
    else if(active){ 
    navigation_container.style.display = "none";
    active = false 
    }
}




