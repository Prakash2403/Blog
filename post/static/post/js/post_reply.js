$(document).ready(function() {
    $('#replyForm_99').submit(function() { // catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: "GET", // GET or POST
            url: $(this).attr('action'), // the file to call

            success: function(response) { // on success..
                var html_content =
                    '<br>' +
                        '<li>' +
                            '<div class="media"> ' +
                                '<a class="pull-left" href="#">' +
                                ' <img class="media-object" src="http://placehold.it/64x64" alt=""> ' +
                                '</a>' +
                                ' <div class="media-body" > ' +
                                    '<h4 class="media-heading">' +
                                        ' <small>August 25, 2014 at 9:30 PM</small> ' +
                                    '</h4>'
                                    +response["content"]+
                                '</div> ' +
                            '</div>' +
                        '</li>';
                $('#reply_list_99').append(html_content);
                $('#replyForm_99').trigger("reset");
            }
        });
        return false;
    });
});