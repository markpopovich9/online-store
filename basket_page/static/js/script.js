let plusButtons = document.querySelectorAll(".edit2")
let minusButtons = document.getElementsByClassName("edit1")
let countText = document.querySelectorAll("#count")
function cordinate(){
    let y = 175
    let borders = document.querySelectorAll(".border")
    let listCount = document.querySelectorAll("#count")
    let listEdit = document.querySelectorAll(".edit")
    // listEdit[0].style.top = 75
    // listCount[0].style.top = -20
    // borders[0].style.top = 175
    for (let count = 0; count < borders.length; count++){
        borders[count].style.top = y+count*300
        listCount[count].style.top = -20
        listEdit[count].style.top = 75
}}
// console.log(plusButtons,document.getElementsByClassName("edit2").length)
console.log(minusButtons)
function destroy(){
    let divs = document.querySelectorAll(".start")
    console.log(divs)
    for (let count = 0; count < divs.length; count++){
        // console.log(id)
        let div = divs[count]
        let id = div.id
        let cookie = document.cookie.split("=")[1].split(" ")
        let count1 = 0
        console.log(cookie)
        for (let count2 = 0; count2 < cookie.length; count2++ ){
            // console.log(`${cookie[count]}`)/
            if (`${cookie[count2]}`==`${id}`){
                count1++
            }
        }
    if(count1 == 0){
        div.remove()

    }}
    cordinate()
}
destroy()
function counting (id){
    console.log(id)
    let text = countText[id-1]
    let cookie = document.cookie.split("=")[1].split(" ")
    let count1 = 0
    console.log(cookie)
    for (let count = 0; count < cookie.length; count++ ){
        console.log(`${cookie[count]}`)
        if (`${cookie[count]}`==`${id}`){
            count1++
        }
    }
    
    text.textContent = `${count1}`
    destroy()
}

for (let count = 0; count < plusButtons.length; count++){
    let button = plusButtons[count]
    let id = button.id
    counting(id)
    button.addEventListener("click", function (event){
        if (document.cookie==""){
            // document.querySelector(".message").style.display = 'block'
            // document.querySelector("#message").style.display = 'block'
            document.cookie=`products=${id};path=/`
        }
        else{
            var cookie = document.cookie.split("=")[1]
            console.log('hello')
            // console.log("end", cookie) 
            cookie =  cookie + ' ' + id
            document.cookie = `products=${cookie};path=/`
            counting(id)
            // document.querySelector("#message").textContent = `${cookie.split(" ").length-1}`

        }
    })
    console.log(2)
}
for (let count = 0; count < minusButtons.length; count++){
    let button = minusButtons[count]
    button.addEventListener("click", function (event){
        if (document.cookie==""){
            // document.querySelector(".message").style.display = 'block'
            // document.querySelector("#message").style.display = 'block'
            // document.cookie=`products=${button.id};path=/`
        }
        else{
            var cookie = document.cookie.split("=")[1].split(" ")
            console.log('hello')
            // console.log("end", cookie) 
            cookie.splice(cookie.indexOf(button.id),1)
            document.cookie = `products=${cookie.join(" ")};path=/`
            // document.querySelector("#message").textContent = `${cookie.split(" ").length-1}`
            console.log((12))
            counting(button.id)
        }

})}