// Debug script for analytics dashboard
document.addEventListener('DOMContentLoaded', function() {
    console.log('Debug script loaded for analytics dashboard');
    
    // Fetch analytics data and log it
    fetch('/api/analytics')
        .then(response => {
            console.log('API Response Status:', response.status);
            return response.json();
        })
        .then(data => {
            console.log('Analytics API Data:', data);
            
            // Log specific sections
            console.log('Total URLs:', data.total_urls);
            console.log('Total Clicks:', data.total_clicks);
            console.log('Active URLs:', data.active_urls);
            console.log('Expired URLs:', data.expired_urls);
            console.log('Clicks over time:', data.clicks_over_time);
            console.log('Creation trends:', data.creation_trends);
            console.log('URLs data:', data.urls);
            
            // Check for missing data
            const missingData = [];
            if (data.total_urls === undefined) missingData.push('total_urls');
            if (data.total_clicks === undefined) missingData.push('total_clicks');
            if (data.active_urls === undefined) missingData.push('active_urls');
            if (data.expired_urls === undefined) missingData.push('expired_urls');
            if (!data.clicks_over_time) missingData.push('clicks_over_time');
            if (!data.creation_trends) missingData.push('creation_trends');
            if (!data.urls) missingData.push('urls');
            
            if (missingData.length > 0) {
                console.error('Missing data in API response:', missingData);
            }
        })
        .catch(error => {
            console.error('Error fetching analytics data:', error);
            document.body.insertAdjacentHTML('afterbegin', 
                `<div style="background: red; color: white; padding: 10px; position: fixed; top: 0; left: 0; right: 0; z-index: 9999;">
                    Error loading analytics data: ${error.message}
                </div>`
            );
        });
}); 