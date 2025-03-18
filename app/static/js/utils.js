/**
 * URL Shortener - Utility Functions
 * 
 * This file contains helper functions used throughout the application.
 */

/**
 * Formats a URL for display by truncating it if it's too long
 * @param {string} url - The URL to format
 * @param {number} maxLength - Maximum length before truncation
 * @returns {string} The formatted URL
 */
function formatUrl(url, maxLength = 40) {
    if (!url) return '';
    if (url.length > maxLength) {
        return url.substring(0, maxLength - 3) + '...';
    }
    return url;
}

/**
 * Formats a date for display
 * @param {string} dateString - The date string to format
 * @returns {string} The formatted date
 */
function formatDate(dateString) {
    if (!dateString) return 'Never';
    
    try {
        const date = new Date(dateString);
        return new Intl.DateTimeFormat('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        }).format(date);
    } catch (e) {
        console.error('Error formatting date:', e);
        return 'Invalid Date';
    }
}

/**
 * Creates a status badge HTML for a URL based on its expiry date
 * @param {string} expiryDate - The expiry date string
 * @returns {string} HTML for the status badge
 */
function getStatusBadge(expiryDate) {
    if (!expiryDate) return '<span class="badge bg-success">Active</span>';
    
    try {
        const expiry = new Date(expiryDate);
        const now = new Date();
        return expiry > now 
            ? '<span class="badge bg-success">Active</span>'
            : '<span class="badge bg-danger">Expired</span>';
    } catch (e) {
        console.error('Error checking status:', e);
        return '<span class="badge bg-warning">Unknown</span>';
    }
}

/**
 * Shows a toast notification
 * @param {string} message - The message to display
 * @param {string} type - The type of toast (success or error)
 * @param {number} duration - How long to show the toast in ms
 */
function showToast(message, type = 'success', duration = 3000) {
    const toastContainer = document.getElementById('toastContainer');
    
    if (!toastContainer) {
        console.error('Toast container not found');
        return;
    }
    
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `
        <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i>
        <span>${message}</span>
    `;
    
    toastContainer.appendChild(toast);
    
    // Remove toast after animation completes
    setTimeout(() => {
        toast.remove();
    }, duration);
}

/**
 * Copies text to clipboard
 * @param {string} text - The text to copy
 * @returns {Promise} Promise that resolves when the text is copied
 */
async function copyToClipboard(text) {
    try {
        await navigator.clipboard.writeText(text);
        return true;
    } catch (err) {
        console.error('Failed to copy text: ', err);
        return false;
    }
} 