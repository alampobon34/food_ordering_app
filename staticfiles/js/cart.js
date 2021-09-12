var updateBtns = document.getElementsByClassName("update-cart");
var obj;

function updateUserOrder(item_id, action) {
  //console.log("User is logged in sending data");

  var url = "/update_item/"

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ 'item_id': item_id, 'action': action }),
  })
    .then((response) => {
      return response.json();
    })

    .then((data) => {
      console.log("data", data);
      //var qty = document.getElementById("quantity").innerHTML=data;
      location.reload();
    });
}

for (var i = 0; i < updateBtns.length; i++) {
  var button = updateBtns[i];
  
  button.addEventListener("click", function (e) {
    //console.log("button clicked")
    var item_id = this.dataset.fooditem;
    var action = this.dataset.action;

    if(action=='delete'){
        var con = confirm("Do you really want to delete this item?")

        if(con==true){
          action='delete'
        }else{
          action=''
        }
    }
    if (user == "AnonymousUser") {
      console.log("not logged in");
      var con = confirm("Please login first..Do you want to redirect login page??")
      if(con==true){
        window.location.replace("http://127.0.0.1:8000/login/");
          } 
      
    } else {
      updateUserOrder(item_id, action);
    }
  });
}
