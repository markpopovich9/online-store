function add_modal(){
    let form = document.querySelector(".modal-window-add")
    let background = document.querySelector(".background")
    let text = document.querySelector(".addText")
    let plus = document.querySelector(".plus")
    text.addEventListener("click", function(){
        
        form.style.display = "flex"
        background.style.display = "flex"
        
    })
}
export default add_modal