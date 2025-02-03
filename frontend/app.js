document.getElementById('url-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const longUrl = document.getElementById('long-url').value;
    const response = await fetch('https://your-api-id.execute-api.region.amazonaws.com/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ longUrl }),
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('short-url').textContent = `Shortened URL: ${data.shortenedUrl}`;
    } else {
        document.getElementById('short-url').textContent = 'Error shortening the URL!';
    }
});
