function cordinate(){
    document.querySelector("#message").style.top = `-19`
    let names = document.getElementsByClassName("name")
    let discountButton = document.getElementsByClassName("discountButton")
    let priceButton = document.getElementsByClassName("priceButton")
    // let ctx= document.getElementById("canvas").getContent("2d")
    let h = document.querySelectorAll("h1")
    let discount = document.getElementsByClassName("discount")
    let price = document.getElementsByClassName("price")
    // for (let count = 0; count < discount.length; count++){
    //     // names[count].style.left = 1000
    //     // names[count].style.top = count*321+145
    //     priceButton[count].style.top = count*321+180
    //     priceButton[count].style.left = 450 
    //     discountButton[count].style.left = 475
    //     discountButton[count].style.top = count*321+210
    //     // console.log(h[count].textContent.length*10)
    // }
    let buttons = document.getElementsByClassName("buy")
    if (document.cookie=="" || document.querySelector("#message").textContent=="0"){
        console.log(document.querySelector("#message").innerHTML)
        document.querySelector(".message").style.display = 'none'
        document.querySelector("#message").style.display = 'none'
    }
}
export default cordinate