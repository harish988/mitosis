$(document).ready(function() {
  $('input[type="file"]').on('click', function() {
      $(".file_names").html("");
    })
  if ($('input[type="file"]')[0]) {
    var fileInput = document.querySelector('label[for="et_pb_contact_brand_file_request_0"]');
    fileInput.ondragover = function() {
      this.className = "et_pb_contact_form_label changed";
      return false;
    }
    fileInput.ondragleave = function() {
      this.className = "et_pb_contact_form_label";
      return false;
    }
    fileInput.ondrop = function(e) {
      e.preventDefault();
      var fileNames = e.dataTransfer.files;
      for (var x = 0; x < fileNames.length; x++) {
        console.log(fileNames[x].name);
        $=jQuery.noConflict();
        $('label[for="et_pb_contact_brand_file_request_0"]').append("<div class='file_names'>"+ fileNames[x].name +"</div>");
      }
    }
    $('#et_pb_contact_brand_file_request_0').change(function() {
      var file = $('#et_pb_contact_brand_file_request_0')[0].files[0]
      var fileNames = $('#et_pb_contact_brand_file_request_0')[0].files[0].name;
      $('label[for="et_pb_contact_brand_file_request_0"]').append("<div class='file_names'>"+ fileNames +"</div>");
      $('label[for="et_pb_contact_brand_file_request_0"]').css('background-color', '##eee9ff');
      var form = new FormData();
      form.append("file", file, file.name);
      console.log(form)
      var settings = {
        "url": "http://127.0.0.1:8000/upload",
        "method": "POST",
        "timeout": 0,
        "headers": {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
      };

        $.ajax(settings).done(function (response) {
          console.log(response);
        });
    });
    }
  });
  
  