function loginValidation() {
  clearError();
  var form = document.getElementById("loginForm");

  var email = document.forms["loginForm"]["login_email"].value;
  var password = document.forms["loginForm"]["login_password"].value;
  var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

  console.log(email, password);
  if (email == "") {
    // alert("Enter a email address");
    setError("login_email", "Enter a email address...");
    return false;
  }

  if (password == "") {
    // alert("Enter the password");
    setError("login_password", "Enter the password...");
    return false;
  }

  if (email.length < 6) {
    // alert("Email address is too short..");
    setError("login_email", "Email address is too short..");
    return false;
  }

  if (password.length < 8) {
    // alert("password is too short..");
    setError("login_password", "Password is too short..");
    return false;
  }
  if (pattern.test(email)) {
    return true;
  } else {
    // alert("enter a valid email address..");
    setError("login_email", "Please enter a valid email address..");
    return false;
  }
}

function RegisterValidation() {
  clearError();
  var form = document.getElementById("registerForm");

  var username = document.forms["registerForm"]["id_username"].value;
  var email = document.forms["registerForm"]["id_email"].value;
  var password1 = document.forms["registerForm"]["id_password1"].value;
  var password2 = document.forms["registerForm"]["id_password2"].value;
  var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

  console.log(email, password1);

  if (username == "") {
    // alert("Enter a email address");
    setError("reg_username", "Enter a username...");
    return false;
  }
  if (email == "") {
    // alert("Enter a email address");
    setError("reg_email", "Enter a email address...");
    return false;
  }

  if (password1 == "") {
    // alert("Enter the password");
    setError("reg_password1", "Enter the password...");
    return false;
  }
  if (password2 == "") {
    // alert("Enter the password");
    setError("reg_password2", "Enter the password...");
    return false;
  }
  if (username.length < 3) {
    // alert("Email address is too short..");
    setError("reg_username", "username is too short..");
    return false;
  }
  if (email.length < 6) {
    // alert("Email address is too short..");
    setError("reg_email", "Email address is too short..");
    return false;
  }

  if (password1.length < 8) {
    // alert("password is too short..");
    setError("reg_password1", "Password is too short..");
    return false;
  }
  if (password1 != password2) {
    setError("reg_password2", "Password is not matched...");
    return false;
  }
  if (pattern.test(email)) {
    return true;
  } else {
    // alert("enter a valid email address..");
    setError("reg_email", "Please enter a valid email address..");
    return false;
  }
}




function changePasswordValidation() {
  clearError();
  var form = document.getElementById("changePasswordForm");

  var old_password = document.forms["changePasswordForm"]["old_password"].value;
  var new_password1 =
    document.forms["changePasswordForm"]["new_password1"].value;
  var new_password2 =
    document.forms["changePasswordForm"]["new_password2"].value;
  var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

  console.log(old_password, new_password1, new_password2);

  if (old_password == "") {
    // alert("Enter a email address");
    setError("old_password", "Enter the current password of your account...");
    return false;
  }

  if (new_password1 == "") {
    // alert("Enter the password");
    setError("new_password1", "New Password can not be blank...");
    return false;
  }
  if (new_password2 == "") {
    // alert("Enter the password");
    setError("new_password2", "Confirm Password can not be blank...");
    return false;
  }

  if (new_password1.length < 8) {
    // alert("password is too short..");
    setError("new_password1", "Password length is too short..");
    return false;
  }
  if (new_password1 != new_password2) {
    setError("new_password2", "Password does not matched...");
    return false;
  }
}

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

// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms).forEach(function (form) {
    form.addEventListener(
      "submit",
      function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }

        form.classList.add("was-validated");
      },
      false
    );
  });
})();


