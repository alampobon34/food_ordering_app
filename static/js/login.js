var email = document.getElementById("login_email").value;
var password = document.getElementById("login_password").value;
var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

function setError(id, error) {
  var field = document.getElementById(id);
  var f = document.getElementById(id);

  //f.innerHTML = error;
  var data = (field.getElementsByClassName("form-text")[0].innerHTML = error);
  console.log(data);
}

function LoginValidation() {
  //   var form = document.getElementById("form");
  //   var email = document.getElementById("id_email").value;
  //   var password = document.getElementById("id_password").value;
  //   var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

  if (email == null || email == "") {
    setError("email", "Email can't be blank...");
    return false;
  }
  if(email.length < 3){
    setError("email", "Email address is to short...");
    return false;
  }
  if (password.length < 6) {
    setError("password", "Password Must have atleast 6 characters long...");
    return false;
  }
  if (email.trim() == null || username == "") {
    setError("email", "email address can't be blank...");
    return false;
  }
  if (pattern.test(email)) {
    error("email", "");
  } 
  else {
    error("email", "Please enter a valid email address");
    return false;
  }
}


// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()