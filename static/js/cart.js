var update_cart = document.getElementsByClassName("update-cart")

for(var i=0; i<update_cart.length; i++){
    var button = update_cart[i]
    button.addEventListener('click', function() {
        console.log("button clicked")
        var target = event.target.parentElement.parentElement.parentElement
        console.log(target)
    })
}
