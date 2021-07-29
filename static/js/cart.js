var updateBtns = document.getElementsByClassName("update-cart");
var obj;

function updateUserOrder(item_id, action) {
  console.log("User is logged in sending data");

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
      location.reload();
    });
}

for (var i = 0; i < updateBtns.length; i++) {
  var button = updateBtns[i];
  button.addEventListener("click", function () {
    //console.log("button clicked")
    var item_id = this.dataset.fooditem;
    var action = this.dataset.action;
    if (user == "AnonymousUser") {
      console.log("not logged in");
    } else {
      updateUserOrder(item_id, action);
    }
  });
}
