// Auto dismiss alerts after 3 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            alert.classList.remove('show');
            alert.classList.add('fade');
            setTimeout(function() {
                alert.remove();
            }, 500);
        }, 3000);
    });
});

// Set minimum date on booking form to today
document.addEventListener('DOMContentLoaded', function() {
    const dateInput = document.querySelector('input[type="date"]');
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
    }
});

// Confirm before cancelling a booking
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.btn-outline-danger');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to cancel this booking?')) {
                e.preventDefault();
            }
        });
    });
});
