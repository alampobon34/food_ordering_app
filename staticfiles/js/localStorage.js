var button = document.getElementsByClassName("update-cart");

for (var i = 0; i < button.length; i++) {
  button[i].addEventListener("click", function () {
      var item_id = this.id
      console.log(item_id)
      
  });
}

