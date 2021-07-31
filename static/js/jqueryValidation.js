$(function () {
  $.validator.addMethod(
    "minValue",
    function (value, element) {
      if (value.length < 4) return false;
      else {
        return true;
      }
    },
    "<em>**Password must be more than 6 characters long**</em>"
  );

  $.validator.addMethod(
    "validEmail",
    function (value, element) {
      var regex =
        /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
      var pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
      if (regex.test(value)) {
        return true;
      } else {
        return false;
      }
    },
    "<em>**Please enter a valid email address**</em>"
  );

  var $loginForm = $("#loginForm");

  if ($loginForm.length) {
    $loginForm.validate({
      rules: {
        email: {
          required: true,
          validEmail: true,
        },
        password: {
          required: true,
          minValue: true,
        },
      },
      messages: {
        email: {
          required: "<em>**Email field is required**</em>",
          // minLength: "<em>**Email address is to short**</em>",
          email: "<em>**Please enter a valid email address**</em>",
        },
        password: {
          required: "<em>**Password field is required**</em>",
        },
      },
    });

  }
});
