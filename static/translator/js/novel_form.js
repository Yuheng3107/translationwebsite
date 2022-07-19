

window.addEventListener("DOMContentLoaded", (e)=>{
    const picLabel = document.querySelector("label[for=id_picture]");
    const picture = document.querySelector("#id_picture");
    picture.onchange = function () {
        if (picture.files.length){
            picLabel.innerHTML = picture.files[0].name;
        } else {
            picLabel.innerHTML = "no file chosen"
        }
    }


})