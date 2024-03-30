document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get user input
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    // Example validation (you should perform proper validation)
    if (email.trim() === '' || password.trim() === '') {
        document.getElementById('error-msg').innerText = 'Please enter both email and password.';
        return;
    }

    // Send data to server for validation (using AJAX)
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'login.php', true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
        if (xhr.status == 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.success) {
                // Redirect to dashboard or perform further actions
                alert('Login successful!');
            } else {
                document.getElementById('error-msg').innerText = response.message;
            }
        }
    };
    xhr.send('email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(password));
});
