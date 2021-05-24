$("#textareaID").keyup(function(){
      $("#infoarea").text("Characters left: " + (1000 - $(this).val().length));
    });