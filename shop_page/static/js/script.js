let buttons = document.getElementsByClassName("buy")
console.log(buttons)

if (document.cookie==""){
    console.log(document.querySelector("#message").innerHTML)
    document.querySelector(".message").style.display = 'none'
    document.querySelector("#message").style.display = 'none'
}
// buttons[0].onclick = () =>{
//    console.log(11)
// }
// lick()
// let ar (event) => {
// let array = [0,1,2,3,4,5,6,7]
// let butt?on = 0
for (let count = 0; count < buttons.length; count++){
        // button=document.getElementById()
        // button.style.margineleft
    // console.log(count)
    // let button = buttons[0]
    // console.log(button.COMMENT_NODE)
    let button = buttons[count]
    console.log(button,button.id)

    button.addEventListener("click", function (event) {
        // 
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
            document.querySelector("#message").textContent = `${cookie.split(" ").length-1}`

        }
    // butto
    })
}
// })