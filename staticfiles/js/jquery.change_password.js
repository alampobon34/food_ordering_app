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

  

    var $changePasswordForm = $('form[name="changePasswordForm"]');
  
    if ($changePasswordForm.length) {
      $changePasswordForm.validate({
        rules: {
          old_password: {
            required: true,
            minValue: true,
          },
          new_password1:{
              required: true,
              minValue:true,
              
          },
          new_password2:{
              required: true,
              minValue: true,
              //equalTo: "#new_password1"
          }
        },
        messages: {
            old_password: {
            required: "<em>**Old password field is required**</em>",
          },
          new_password1: {
            required: "<em>**New password field is required**</em>",
          },
          new_password2:{
            required: "<em>**Confirm password field is required**</em>",
            //equalTo: "<em>**Confirm password field does not match**</em>",
          }
        },
      });
    }
  });
  
  
  
  
  
  
  