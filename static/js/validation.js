function setError(id, error) {
  var field = document.getElementById(id);
  var f = document.getElementById(id);

  //f.innerHTML = error;
  var data = (field.getElementsByClassName("form-text")[0].innerHTML = error);
  console.log(data);
}

function Register() {
  var form = document.getElementById("form");
  var username = document.getElementById("id_username").value;
  var email = document.getElementById("id_email").value;
  var password1 = document.getElementById("id_password1").value;
  var password2 = document.getElementById("id_password2").value;
  var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

  if (username.trim() == null || username == "") {
    setError("username", "Username can't be blank...");
    return false;
  } else if (username.trim().length <= 2) {
    setError("username", "Username must have atleast 3 characters....");
    return false;
  } else if (email.trim() == null || email == "") {
    setError("email", "Email can't be blank...");
    email.focus();
    return false;
  } else if (password1.length < 6) {
    setError("password1", "Password must have atleast 3 characters...");
    return false;
  } else if (password2.length < 6) {
    setError("password2", "Confirm Password must have atleast 3 characters...");
    return false;
  } else if (password1 != password2) {
    setError("password2", "Password is not matched...");
    return false;
  }

  if (pattern.test(email)) {
    setError("email", "");
  } else {
    setError("email", "Please enter a valid email Address");
    return false;
  }
}

function LoginValidation() {
  var form = document.getElementById("form");
  var email = document.getElementById("id_email").value;
  var password = document.getElementById("id_password").value;
  var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

  if (email.trim() == null || email == "") {
    setError("email", "Email can't be blank...");
    return false;
  } else if (password.length < 6) {
    setError("password", "Password Must have atleast 6 characters long...");
    return false;
  } else if (email.trim() == null || username == "") {
    setError("email", "email address can't be blank...");
    return false;
  } else if (pattern.test(email)) {
    error("email", "");
  } else {
    error("email", "Please enter a valid email address");
    return false;
  }
}
