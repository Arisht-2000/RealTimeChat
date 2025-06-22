// Shared logic for all pages
window.joinChatroom = function() {
    const chatroomCode = document.getElementById('chatroomCode')?.value.trim();
    const errorMessage = document.getElementById('errorMessage');
    if (errorMessage) errorMessage.textContent = '';
    if (chatroomCode) {
        window.location.pathname = `/chatroom/${chatroomCode}/`;
    } else if (errorMessage) {
        errorMessage.textContent = 'Please enter a valid chatroom code.';
    }
}
