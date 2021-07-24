const form = document.getElementById("form");
const pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;

// for register form
const username = document.getElementById("id_username").value;
const email = document.getElementById("id_email").value;
const password1 = document.getElementById("id_password1").value;
const password2 = document.getElementById("id_password2").value;

// for login form
// const email = document.getElementById("id_email").value;
//const password = document.getElementById("id_password").value;

function validate() {
  if (username.trim().length <= 2) {
    setError("username", "Username must have atleast 3 characters....");
    return false;
  } else if (email.trim() == null || email == "") {
    setError("email", "Email can't be blank...");
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

  return true;
}

function setError(id, error) {
  var field = document.getElementById(id);
  var f = document.getElementById(id);

  //f.innerHTML = error;
  var data = (field.getElementsByClassName("form-text")[0].innerHTML = error);
  console.log(data);
}


(function () {

  
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