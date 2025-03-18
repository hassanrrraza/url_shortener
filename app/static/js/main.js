// Global variables for charts
let clicksChart, devicesChart, browsersChart, osChart;
let currentShortUrl = '';

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    // Form submission
    const urlForm = document.getElementById('urlForm');
    urlForm.addEventListener('submit', handleFormSubmit);

    // Load URL list when modal is opened
    const urlListModal = document.getElementById('urlListModal');
    urlListModal.addEventListener('show.bs.modal', loadUrlList);
});

// Handle form submission
async function handleFormSubmit(e) {
    e.preventDefault();
    
    const formData = {
        url: document.getElementById('url').value,
        custom_alias: document.getElementById('customAlias').value,
        expiration_date: document.getElementById('expirationDate').value,
        tags: document.getElementById('tags').value,
        description: document.getElementById('description').value
    };

    try {
        const response = await fetch('/api/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();
        
        if (response.ok) {
            showResult(data.short_url);
            currentShortUrl = data.short_url.split('/').pop();
        } else {
            showError(data.error);
        }
    } catch (error) {
        showError('An error occurred while shortening the URL');
    }
}

// Show the shortened URL result
function showResult(shortUrl) {
    const resultDiv = document.getElementById('result');
    const shortUrlInput = document.getElementById('shortUrl');
    
    shortUrlInput.value = shortUrl;
    resultDiv.classList.remove('d-none');
    resultDiv.classList.add('show');
    
    // Hide analytics if showing
    const analyticsDiv = document.getElementById('analytics');
    analyticsDiv.classList.add('d-none');
    analyticsDiv.classList.remove('show');
}

// Copy shortened URL to clipboard
function copyToClipboard() {
    const shortUrl = document.getElementById('shortUrl');
    shortUrl.select();
    document.execCommand('copy');
    
    showToast('URL copied to clipboard!');
}

// Show analytics for the current URL
async function showAnalytics() {
    if (!currentShortUrl) return;

    try {
        const response = await fetch(`/api/analytics/${currentShortUrl}`);
        const data = await response.json();
        
        if (response.ok) {
            displayAnalytics(data);
        } else {
            showError('Failed to load analytics');
        }
    } catch (error) {
        showError('An error occurred while loading analytics');
    }
}

// Display analytics data
function displayAnalytics(data) {
    const analyticsDiv = document.getElementById('analytics');
    analyticsDiv.classList.remove('d-none');
    analyticsDiv.classList.add('show');

    // Destroy existing charts
    if (clicksChart) clicksChart.destroy();
    if (devicesChart) devicesChart.destroy();
    if (browsersChart) browsersChart.destroy();
    if (osChart) osChart.destroy();

    // Create new charts
    createClicksChart(data.analytics.clicks_by_date);
    createDevicesChart(data.analytics.devices);
    createBrowsersChart(data.analytics.browsers);
    createOSChart(data.analytics.os);
}

// Create clicks timeline chart
function createClicksChart(clicksData) {
    const ctx = document.getElementById('clicksChart').getContext('2d');
    const labels = Object.keys(clicksData);
    const data = Object.values(clicksData);

    clicksChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Clicks per Day',
                data: data,
                borderColor: '#4361ee',
                backgroundColor: 'rgba(67, 97, 238, 0.1)',
                tension: 0.3,
                fill: true
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Click Timeline'
                }
            }
        }
    });
}

// Create devices pie chart
function createDevicesChart(devicesData) {
    const ctx = document.getElementById('devicesChart').getContext('2d');
    
    devicesChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: Object.keys(devicesData),
            datasets: [{
                data: Object.values(devicesData),
                backgroundColor: ['#4361ee', '#3f37c9', '#f72585']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Device Types'
                }
            }
        }
    });
}

// Create browsers chart
function createBrowsersChart(browsersData) {
    const ctx = document.getElementById('browsersChart').getContext('2d');
    
    browsersChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(browsersData),
            datasets: [{
                label: 'Browser Usage',
                data: Object.values(browsersData),
                backgroundColor: '#4895ef'
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Browser Distribution'
                }
            }
        }
    });
}

// Create OS chart
function createOSChart(osData) {
    const ctx = document.getElementById('osChart').getContext('2d');
    
    osChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: Object.keys(osData),
            datasets: [{
                data: Object.values(osData),
                backgroundColor: ['#4361ee', '#3f37c9', '#f72585', '#4895ef']
            }]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Operating Systems'
                }
            }
        }
    });
}

// Load list of URLs
async function loadUrlList() {
    try {
        const response = await fetch('/api/urls');
        const urls = await response.json();
        
        const urlList = document.getElementById('urlList');
        urlList.innerHTML = '';
        
        urls.forEach(url => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><a href="${url.short_url}" target="_blank">${url.short_url}</a></td>
                <td>${truncateUrl(url.original_url)}</td>
                <td>${url.total_clicks}</td>
                <td>${formatDate(url.created_at)}</td>
                <td>
                    <button class="btn btn-sm btn-primary" onclick="showUrlAnalytics('${url.short_url}')">
                        Analytics
                    </button>
                </td>
            `;
            urlList.appendChild(row);
        });
    } catch (error) {
        showError('Failed to load URL list');
    }
}

// Helper functions
function truncateUrl(url, maxLength = 50) {
    return url.length > maxLength ? url.substring(0, maxLength) + '...' : url;
}

function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString();
}

function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'copy-success';
    toast.textContent = message;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

function showError(message) {
    // You can implement a more sophisticated error display
    alert(message);
} 