// Можна додати інтерактивність, наприклад, автоматичну зміну курсів або валідацію форм

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', function(event) {
        const amountInput = document.querySelector('input[name="amount"]');
        
        if (isNaN(amountInput.value) || amountInput.value <= 0) {
            event.preventDefault();
            alert('Please enter a valid positive number');
        }
    });
});

