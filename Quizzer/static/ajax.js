  $(function() {
    $(".button").click(function() {
      // validate and process form here

  var response =  $(".resp:checked").val();
  var quizid =document.getElementById('question_id')
   $.ajax({
    type: "POST",
    url: "test/"+quizid,
    data: response,

    }
  });
  return false;
  });
    $(document).ready(function() {

    var response =  $(".resp:checked").val();
    var quizid =document.getElementById('question_id')

    // process the form
    $('form').submit(function(event) {

        // process the form
        $.ajax({
            type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
            url         : 'test/'+, // the url where we want to POST
            data        : formData, // our data object

        })
    });

});