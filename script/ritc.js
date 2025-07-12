function showPage(toTab){
    var currentSelectedTab = document.querySelector('[aria-selected=true]')
    var currentSelectedWindow = document.querySelector('[aria-current=true]')
    var newTab, newWindow;

    switch (toTab) {
        case "email":
            newTab = document.getElementById('emailTab')
            newWindow = document.getElementById('emailWindow')
            break;
        case "home":
            newTab = document.getElementById('homeTab')
            newWindow = document.getElementById('homeWindow')
            break;
        default:
            console.log("Cannot find toTab");
            break;
    }

    if(newTab != null && newWindow != null){
        currentSelectedTab.ariaSelected = false;
        currentSelectedWindow.ariaCurrent = false;
        currentSelectedWindow.hidden = true;
        newTab.ariaSelected = true;
        newWindow.ariaCurrent= true;
        newWindow.hidden = false;
    }
}