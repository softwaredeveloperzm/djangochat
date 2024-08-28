function autoRefreshMessages() {
    let sender = $("#user_sender").val();
    let receiver = $("#receiver_username").val();
    if (sender && receiver) {
        fetchMessages(sender, receiver);
    }
}

// Refresh the messages every 5 seconds
setInterval(autoRefreshMessages, 1000);