document.getElementById('inputForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/submit', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    document.getElementById('message').textContent = data.message;
});
