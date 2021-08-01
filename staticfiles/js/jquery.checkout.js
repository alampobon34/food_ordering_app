

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

  var $ShippingForm = $('form[name="ShippingForm"]');

  if ($ShippingForm.length) {
    $ShippingForm.validate({
      rules: {
        address: {
          required: true,
        },
        area: {
          required: true,
        },
        houseNo: {
          required: true,
        },
        zipcode: {
          required: true,
        },
      },
      messages: {
        address: {
          required: "<em>**Email field is required**</em>",
        },
        area: {
          required: "<em>**Password field is required**</em>",
        },
        houseNo: {
          required: "<em>**Confirm password field is required**</em>",
        },
        zipcode: {
          required: "<em>**username field is required**</em>",
        }
      }
    });
  }
});



