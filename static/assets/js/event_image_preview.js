   // Image preview functionality
    document.getElementById('event-image').addEventListener('change', function(e) {
        const preview = document.getElementById('image-preview');
        preview.innerHTML = '';

        if (this.files && this.files[0]) {
            const reader = new FileReader();
            reader.onload = function(e) {
                const previewItem = document.createElement('div');
                previewItem.className = 'image-preview-item';

                const img = document.createElement('img');
                img.src = e.target.result;
                img.alt = 'Event Image Preview';

                const removeBtn = document.createElement('div');
                removeBtn.className = 'remove-image';
                removeBtn.innerHTML = '&times;';
                removeBtn.onclick = function() {
                    previewItem.remove();
                    document.getElementById('event-image').value = '';
                };

                previewItem.appendChild(img);
                previewItem.appendChild(removeBtn);
                preview.appendChild(previewItem);
            }
            reader.readAsDataURL(this.files[0]);
        }
    });
