

$(function () {

  $.validator.addMethod(
    "minValue",
    function (value, element) {
      if (value.length < 4) return false;
      else {
        return true;
      }
    },
    "<em>**Please enter a valid input**</em>"
  );



  var $ShippingForm = $('form[name="Shipping-form"]');

  if ($ShippingForm.length) {
    $ShippingForm.validate({
      rules: {
        address: {
          required: true,
          minValue:true
        },
        area: {
          required: true,
          minValue:true
        },
        houseNo: {
          required: true,
          minValue:true
        },
        zipcode: {
          required: true,
          minValue:true,
          number:true
        },
      },
      messages: {
        address: {
          required: "<em>**Address field is required**</em>",
        },
        area: {
          required: "<em>**Area field is required**</em>",
        },
        houseNo: {
          required: "<em>**HouseNo field is required**</em>",
        },
        zipcode: {
          required: "<em>**ZipCode field is required**</em>",
          number: "<em>**Please type digits**</em>",

        }
      }
    });
  }
});



