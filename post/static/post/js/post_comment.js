$(document).ready(function() {
    $('#commentForm').submit(function() { // catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call

            success: function(response) { // on success..
                var currentdate = new Date();
                var datetime = currentdate.getDate() + "/"
                + (currentdate.getMonth()+1)  + "/"
                + currentdate.getFullYear() + " @ "
                + currentdate.getHours() + ":"
                + currentdate.getMinutes() + ":"
                + currentdate.getSeconds();
                var html_content =
                    '<br>' +
                        '<li>' +
                            '<div class="media"> ' +
                                '<a class="pull-left" href="#">' +
                                ' <img class="media-object" src="http://placehold.it/64x64" alt=""> ' +
                                '</a>' +
                                ' <div class="media-body" > ' +
                                    '<h4 class="media-heading">' +
                                        ' <small>'+datetime+
                                        '</small>'+
                                    '</h4>'+
                                    response["content"]+
                                '</div> ' +
                            '</div>' +
                        '</li>';
                $('#comment_list').prepend(html_content);
                $('#commentForm').trigger("reset");
            }
        });
        return false;
    });
});