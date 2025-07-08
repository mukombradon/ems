
    // Venue selection logic
    const venueInput = document.getElementById('venue');
    const venueIdInput = document.getElementById('venue_id');
    const locationInput = document.getElementById('location');
    const options = document.querySelectorAll('#venue-options option');

    venueInput.addEventListener('input', function () {
        const inputValue = this.value;
        let matched = false;

        options.forEach(option => {
            if (option.value === inputValue) {
                // Set venue ID
                venueIdInput.value = option.dataset.id;

                // Format and set location string
                const address = option.dataset.address || '';
                const city = option.dataset.city || '';
                const country = option.dataset.country || '';
                const locationString = `${address}, ${city}, ${country}`.replace(/(,\s*)+$/, ''); // clean up trailing commas

                locationInput.value = locationString;
                matched = true;
            }
        });

        if (!matched) {
            venueIdInput.value = '';
            locationInput.value = '';
        }
    });