

function setError(id, error) {
  var field = document.getElementById(id);

  //f.innerHTML = error;
  var data = (field.getElementsByClassName("form-text")[0].innerHTML = error);
  console.log(data);
}

function clearError() {
  var errors = document.getElementsByClassName("form-text");
  for (let item of errors) {
    item.innerHTML = "";
  }
}




function ShippingAddress(){
  clearError();
  var form = document.getElementById("shippingForm");

  var address = document.forms["shippingForm"]["address"].value;
  var area = document.forms["shippingForm"]["area"].value;
  var houseNo = document.forms["shippingForm"]["houseNo"].value;
  var zipcode = document.forms["shippingForm"]["zipcode"].value;


  if (address == "") {
    // alert("Enter a email address");
    setError("add_address", "Enter the address...");
    return false;
  }
  if (area == "") {
    // alert("Enter a email address");
    setError("add_area", "Enter the area...");
    return false;
  }
  if (houseNo == "") {
    // alert("Enter a email address");
    setError("add_houseNo", "Enter the house no...");
    return false;
  }
  if (zipcode == "") {
    // alert("Enter a email address");
    setError("add_zipcode", "enter the zipcode...");
    return false;
  }
  if (zipcode == "." || zipcode=="e") {
    // alert("Enter a email address");
    setError("add_zipcode", "zip code must have digits...");
    return false;
  }
  if (zipcode.length !=4) {
    // alert("Enter a email address");
    setError("add_zipcode", "Zip code has 4 digits...");
    return false;
  }


}