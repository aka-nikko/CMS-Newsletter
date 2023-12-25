/*=============== PRELOADER ===============*/
var loader = document.getElementById("loader-wrapper");
window.addEventListener("load", function(){
  setTimeout(function(){
    loader.style.display = "none";
  },500)
});

/*=============== CHANGE THEME ===============*/
var themechange=document.getElementById("change-theme");
var body=document.body;

if(localStorage.getItem("theme")=="dark-mode"){
  body.classList.add("dark-mode");
}

themechange.onclick=function(){
  body.classList.toggle("dark-mode");
  if(body.classList.contains("dark-mode")){
    localStorage.setItem("theme","dark-mode");
  }else{
    localStorage.setItem("theme",":root");
  }
}

/*=============== MESSAGE-MODAL ===============*/
window.onload = () => {
    const myModal = new bootstrap.Modal('#messageModal');
    myModal.show();
}

/*=============== REGISTER-PASSWORDCHECK ===============*/
document.addEventListener("DOMContentLoaded", function () {
    const password1Input = document.querySelector("#floatingPassword1");
    const password2Input = document.querySelector("#floatingPassword2");
    const passwordMismatchMessage = document.querySelector("#passwordMismatchMessage");
    const signUpButton = document.querySelector("#signup-button");

    function checkPasswordMatch() {
        const password1 = password1Input.value;
        const password2 = password2Input.value;
        if (password1 === password2) {
            passwordMismatchMessage.style.display = "none";
            signUpButton.disabled = false;
        } 
        else {
            passwordMismatchMessage.style.display = "block";
            signUpButton.disabled = true;
        }
    }

    password1Input.addEventListener("input", checkPasswordMatch);
    password2Input.addEventListener("input", checkPasswordMatch);

    checkPasswordMatch();
});

/*=============== DISPLAY BROWSED IMAGE FILE NAME ===============*/
var input = document.getElementById('file-upload');
var infoArea = document.getElementById('file-upload-filename');
input.addEventListener('change', showFileName );
function showFileName( event ) {
  var input = event.srcElement;
  var fileName = input.files[0].name;
  infoArea.textContent = 'Image: ' + fileName;
}

/*=============== SUBMISSION-DRAGSORT ===============*/
function enableDragSort(listClass) {
const sortableLists = document.getElementsByClassName(listClass);
Array.prototype.map.call(sortableLists, (list) => {enableDragList(list)});
}

function enableDragList(list) {
Array.prototype.map.call(list.children, (item) => {enableDragItem(item)});
}

function enableDragItem(item) {
item.setAttribute('draggable', true)
item.ondrag = handleDrag;
item.ondragend = handleDrop;
}

function handleDrag(item) {
const selectedItem = item.target,
        list = selectedItem.parentNode,
        x = event.clientX,
        y = event.clientY;

selectedItem.classList.add('drag-sort-active');
let swapItem = document.elementFromPoint(x, y) === null ? selectedItem : document.elementFromPoint(x, y);

if (list === swapItem.parentNode) {
    swapItem = swapItem !== selectedItem.nextSibling ? swapItem : swapItem.nextSibling;
    list.insertBefore(selectedItem, swapItem);
}
}

function handleDrop(item) {
item.target.classList.remove('drag-sort-active');
}

(()=> {enableDragSort('drag-sort-enable')})();