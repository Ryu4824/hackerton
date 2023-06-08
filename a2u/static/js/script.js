function flipPreview(container) {
  $(container).toggleClass("flipped");
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function imageUpload() {
  var formData = new FormData();
  var uploadImage = $("#imageInput")[0].files[0];
  formData.append("name", uploadImage);
  console.log(uploadImage);

  $(".preview-container").removeClass("flipped");
  $(".preview-container").removeAttr("onclick");
  $("#loading").show();

  $.ajax({
    url: "./image/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
    success: function (response) {
      $(".preview-container").attr("onclick", "flipPreview(this)");
      $("#loading").hide();
      console.log(response);
      $(".preview-front").attr("src", `/static/inputs/${response}`);
      $(".preview-back").attr("src", `/static/results/${response}`);
    },
    error: function (xhr, error) {
      $(".preview-container").attr("onclick", "flipPreview(this)");
      $("#loading").hide();
      console.error(xhr.status + ": " + error);
    },
  });
}
