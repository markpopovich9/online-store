let plusButtons = document.querySelectorAll(".edit2")
let minusButtons = document.getElementsByClassName("edit1")
let countText = document.querySelectorAll(".count")
// console.log(plusButtons,document.getElementsByClassName("edit2").length)
for (let count = 0; count < plusButtons.length; count++){
    let button = plusButtons[count]
    button.addEventListener("click", function (event){
        if (document.cookie==""){
            document.querySelector(".message").style.display = 'block'
            document.querySelector("#message").style.display = 'block'
            document.cookie=`products=${button.id};path=/`
        }
        else{
            var cookie = document.cookie.split("=")[1]
            console.log('hello')
            // console.log("end", cookie) 
            cookie =  cookie + ' ' + button.id
            document.cookie = `products=${cookie};path=/`
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
        }

})}