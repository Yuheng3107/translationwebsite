

window.addEventListener("DOMContentLoaded", (e)=>{
    const picLabel = document.querySelector("label[for=id_picture]");
    const picture = document.querySelector("#id_picture");
    const rawsLabel = document.querySelector("label[for=id_raws]")
    const raws = document.querySelector("#id_raws");
    picture.onchange = function () {
        if (picture.files.length){
            picLabel.innerHTML = picture.files[0].name;
        } else {
            picLabel.innerHTML = "no file chosen"
        }
    }
    raws.onchange = function () {
        if (raws.files.length){
            rawsLabel.innerHTML = raws.files[0].name;
        } else {
            rawsLabel.innerHTML = "no file chosen"
        }
    }


})