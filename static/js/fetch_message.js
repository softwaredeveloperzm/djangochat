// Function to fetch and display messages
function fetchMessages(sender, receiver) {
    $.ajax({
        type: 'GET',
        url: '/fetch_messages/',
        data: {
            sender: sender,
            receiver: receiver
        },
        success: function(response) {
            if (response.status === 'Success') {
                let messageList = response.messages;
                let html = '';
                messageList.forEach(message => {
                    let messageClass = (message.sender__username === sender) ? 'sent-message' : 'received-message';
                    html += `<li class="${messageClass}">
                                <div class="message-content">
                                    ${message.message}
                                </div>
                                <small class="message-time">${new Date(message.date_posted).toLocaleString()}</small>
                            </li>`;
                });
                $("#messages-list").html(html);

                // Scroll to the bottom of the chat
                $("#messages-list").scrollTop($("#messages-list")[0].scrollHeight);
            } else {
                alert('Failed to fetch messages');
            }
        },
        error: function(xhr, status, error) {
            alert("An error occurred: " + error);
        }
    });
}
