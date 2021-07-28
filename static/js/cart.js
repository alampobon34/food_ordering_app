var updateBtns = document.getElementsByClassName("update-cart")
var obj;

for(var i=0; i<updateBtns.length; i++){
    var button = updateBtns[i]
    button.addEventListener('click', function() {
        //console.log("button clicked")
        var item_id = this.dataset.fooditem
        var action = this.dataset.action
        if(user=='AnonymousUser'){
            console.log('not logged in')
        }else{
            updateUserOrder(item_id,action)
        }
    })
}


function updateUserOrder(item_id, action){
    console.log("User is logged in sending data")

    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'item_id': item_id, 'action':action})
    })

    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        console.log('data',data)
        location.reload()

    })

}


var change= document.getElementsByClassName("update-cart")

for(var i=0; i<change.length; i++){
    change[i].addEventListener('click',function(){
        var item_id = this.dataset.item
        var action = this.dataset.action
        console.log(item_id)
        console.log(action)
        updateUserOrder(item_id,action)

    })
}