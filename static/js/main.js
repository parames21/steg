// Initialize FilePond
document.addEventListener('DOMContentLoaded', function() {
    // File upload initialization
    const fileInputs = document.querySelectorAll('.filepond');
    fileInputs.forEach(input => {
        FilePond.create(input, {
            labelIdle: 'Drag & Drop your image or <span class="filepond--label-action">Browse</span>',
            styleItemPanel: {
                backgroundColor: 'rgba(255, 255, 255, 0.1)'
            }
        });
    });

    // Password toggle functionality
    const passwordToggles = document.querySelectorAll('.password-toggle');
    passwordToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const input = this.previousElementSibling;
            if (input.type === 'password') {
                input.type = 'text';
                this.textContent = '👁‍🗨';
            } else {
                input.type = 'password';
                this.textContent = '👁';
            }
        });
    });

    // Copy to clipboard functionality
    const copyBtn = document.querySelector('.copy-btn');
    if (copyBtn) {
        copyBtn.addEventListener('click', function() {
            const messageText = document.querySelector('.message-reveal').textContent;
            navigator.clipboard.writeText(messageText).then(() => {
                Swal.fire({
                    title: 'Copied!',
                    text: 'Message copied to clipboard',
                    icon: 'success',
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 3000
                });
            });
        });
    }

    // Flash messages using SweetAlert2
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        Swal.fire({
            text: message.textContent,
            icon: message.dataset.type || 'info',
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000
        });
    });
});

// Page transition animations using GSAP
window.addEventListener('load', () => {
    gsap.from('main > *', {
        opacity: 0,
        y: 20,
        duration: 0.8,
        stagger: 0.2,
        ease: 'power2.out'
    });
}); 