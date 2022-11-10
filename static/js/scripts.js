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

$("form[name=reloadspendingtable_form").submit(function (e) {
  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/reloadspendingtable",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      i = 0
      maxLoop = Math.min(6, resp.success.length-1)
      var insertdata = "";
      for( i; i < maxLoop; i = i+1) {       
        insertdata = insertdata + "<tr><td>" + resp.success[i][0] + '</td><td>' + resp.success[i][1] + '</td>' + '</td><td>' + resp.success[i][2] + '</td></tr>';
      }
      $("#result").html(insertdata);
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  })
  e.preventDefault();
})