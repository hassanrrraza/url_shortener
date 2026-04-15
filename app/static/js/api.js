/**
 * URL Shortener - API Service
 * 
 * This file contains all API calls to the backend service.
 * Centralizing these calls makes the codebase more maintainable.
 */

class UrlShortenerAPI {
    /**
     * Fetches all URLs from the server
     * @returns {Promise} Promise object representing the API response
     */
    static async getUrls() {
        const response = await fetch('/api/urls');
        if (!response.ok) {
            throw new Error(`API returned status: ${response.status}`);
        }
        return await response.json();
    }
    
    /**
     * Creates a new shortened URL
     * @param {Object} urlData - The URL data to shorten
     * @returns {Promise} Promise object representing the API response
     */
    static async createUrl(urlData) {
        const response = await fetch('/api/shorten', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(urlData)
        });

        let payload = null;
        try {
            payload = await response.json();
        } catch (e) {
            /* empty or non-JSON body */
        }

        if (!response.ok) {
            const msg = (payload && (payload.error || payload.message))
                || `Failed to shorten URL (${response.status})`;
            throw new Error(msg);
        }

        return payload;
    }
    
    /**
     * Deletes a URL by its ID
     * @param {number} urlId - The ID of the URL to delete
     * @returns {Promise} Promise object representing the API response
     */
    static async deleteUrl(urlId) {
        const response = await fetch(`/api/urls/${urlId}`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            throw new Error(`API returned status: ${response.status}`);
        }
        
        return await response.json();
    }
    
    /**
     * Gets analytics data from the server
     * @returns {Promise} Promise object representing the API response
     */
    static async getAnalytics() {
        const response = await fetch('/api/analytics');
        
        if (!response.ok) {
            throw new Error(`API returned status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        return data;
    }
} 