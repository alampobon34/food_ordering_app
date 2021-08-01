$(function () {
    $.validator.addMethod(
        "minLength",
        function (value, element) {
          if (value.length < 3) return false;
          else {
            return true;
          }
        },
        "<em>**UserName must be more than 2 characters long**</em>"
      );
  
      
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
  
    var $registerForm = $('form[name="registerForm"]');
  
    if ($registerForm.length) {
      $registerForm.validate({
        rules: {
          email: {
            required: true,
            validEmail: true,
          },
          password1: {
            required: true,
            minValue: true,
          },
          password2:{
              required: true,
              minValue:true,
              equalTo: "#password1"
          },
          username:{
              required: true,
              minLength:true
          }
        },
        messages: {
          email: {
            required: "<em>**Email field is required**</em>",
            // minLength: "<em>**Email address is to short**</em>",
            email: "<em>**Please enter a valid email address**</em>",
          },
          password1: {
            required: "<em>**Password field is required**</em>",
          },
          password2:{
            required: "<em>**Confirm password field is required**</em>",
            equalTo: "<em>**Confirm password field does not match**</em>",
          },
          username:{
            required: "<em>**username field is required**</em>",
          }
        },
      });
    }
  });
  
  
  
  
  
  
  