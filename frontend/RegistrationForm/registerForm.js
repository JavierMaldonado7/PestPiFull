document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get form input values
    var firstName = document.getElementById('firstName').value.trim();
    var lastName = document.getElementById('lastName').value.trim();
    var telephone = document.getElementById('telephone').value.trim();
    var email = document.getElementById('email').value.trim();
    var password = document.getElementById('password').value.trim();
    var repeatPassword = document.getElementById('repeatPassword').value.trim();
    var role = document.getElementById('role').value;
    var gender = document.querySelector('input[name="gender"]:checked');

    // Validate form input
    if (firstName === '' || lastName === '' || telephone === '' || email === '' || password === '' || repeatPassword === '' || role === '' || gender === null) {
        alert('Please fill in all fields.');
        return;
    }

    if (password !== repeatPassword) {
        alert('Passwords do not match.');
        return;
    }

    // Submit form data to server
    var formData = new FormData();
    formData.append('firstName', firstName);
    formData.append('lastName', lastName);
    formData.append('telephone', telephone);
    formData.append('email', email);
    formData.append('password', password);
    formData.append('role', role);
    formData.append('gender', gender.value);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'register.php', true);
    xhr.onload = function() {
        if (xhr.status == 200) {
            alert(xhr.responseText); // Display response from server
            // You can redirect or perform other actions based on the response
        }
    };
    xhr.send(formData);
});
