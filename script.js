document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get the value from the input field
    const name = document.getElementById('name').value;

    // Display the welcome message
    document.getElementById('userName').textContent = name;
    document.getElementById('signupForm').classList.add('hidden');
    document.getElementById('welcomeMessage').classList.remove('hidden');
});