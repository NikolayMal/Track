$("form[name=signup_form").submit(function (e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      window.location.href = "/dashboard/";
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function (e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      window.location.href = "/dashboard/";
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=insert_form").submit(function (e) {
  var $form = $(this);
  var $success = $form.find(".success");
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/insert",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  })
  e.preventDefault();
})