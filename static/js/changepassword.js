form.addEventListener("submit", (e) => {
  e.preventDefault();

  passwordChange();
});

function setError(id, error) {
  var field = document.getElementById(id);
  var f = document.getElementById(id);

  //f.innerHTML = error;
  var data = (field.getElementsByClassName("form-text")[0].innerHTML = error);
  console.log(data);
}

function passwordChange() {
  var form = document.getElementById("form");
  var old_password = document.getElementById("old_password").value;
  var new_password1 = document.getElementById("new_password1").value;
  var new_password2 = document.getElementById("new_password2").value;

  if (old_password == null || old_password == "") {
    setError("old_password", "Password Must have atleast 6 characters long...");
    return false;
  } else if (new_password1 == null || new_password1 == "") {
    setError("new_password1", "Password can't be blank...");
    return false;
  } else if (new_password2 == null || new_password2 == "") {
    setError("new_password2", "Password can't be blank...");
    return false;
  } else if (password1 != password2) {
    setError("new_password2", "Password is not matched...");
    return false;
  } else if (new_password1.length < 6) {
    setError(
      "new_password1",
      "Password Must have atleast 6 characters long..."
    );
    return false;
  } else if (new_password2.length < 6) {
    setError(
      "new_password2",
      "Password Must have atleast 6 characters long..."
    );
    return false;
  }
}

function print() {
  var old_password = document.getElementById("old_password").value;
  var new_password1 = document.getElementById("new_password1").value;
  var new_password2 = document.getElementById("new_password2").value;
  console.log(old_password);
  console.log(new_password1);
  console.log(new_password2);
  return false;
}

