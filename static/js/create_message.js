$(document).ready(function() {

    // Handle message sending
    $(document).on('submit', '#task-form', function(e) {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: $(this).data('url'),
            data: {
                message: $("#message").val(),
                user_sender: $("#user_sender").val(),
                receiver_username: $("#receiver_username").val(),
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                if (response.status === 'Message sent successfully') {
                    // Fetch messages after sending
                    fetchMessages(response.user_sender, response.user_receiver);
                    // Clear the message input field
                    $("#message").val('');
                } else {
                    alert("Failed to send message");
                }
            },
            error: function(xhr, status, error) {
                alert("An error occurred: " + error);
            }
        });
    });

    
});
