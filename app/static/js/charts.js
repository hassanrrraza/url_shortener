/**
 * URL Shortener - Chart Initialization and Configuration
 * 
 * This file contains the initialization and configuration for all charts used in the application.
 * Separating this logic makes the codebase more maintainable.
 */

function initStatusChart(elementId) {
    const statusChartCtx = document.getElementById(elementId).getContext('2d');
    return new Chart(statusChartCtx, {
        type: 'doughnut',
        data: {
            labels: ['Active', 'Expired'],
            datasets: [{
                data: [0, 0],
                backgroundColor: [
                    'rgba(74, 222, 128, 0.6)',
                    'rgba(248, 113, 113, 0.6)'
                ],
                borderColor: [
                    'rgba(74, 222, 128, 1)',
                    'rgba(248, 113, 113, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#ffffff'
                    }
                }
            }
        }
    });
}

function initTopUrlsChart(elementId) {
    const topUrlsChartCtx = document.getElementById(elementId).getContext('2d');
    return new Chart(topUrlsChartCtx, {
        type: 'bar',
        data: {
            labels: [],
            datasets: [{
                label: 'Clicks',
                data: [],
                backgroundColor: 'rgba(247, 37, 133, 0.6)',
                borderColor: 'rgba(247, 37, 133, 1)',
                borderWidth: 1,
                borderRadius: 6
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        color: '#ffffff'
                    }
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        precision: 0,
                        color: '#8d99ae'
                    }
                },
                y: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: '#8d99ae'
                    }
                }
            }
        }
    });
}

function initWeekdayChart(elementId) {
    const weekdayCtx = document.getElementById(elementId).getContext('2d');
    return new Chart(weekdayCtx, {
        type: 'bar',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'URLs Created',
                data: [0, 0, 0, 0, 0, 0, 0],
                backgroundColor: function(context) {
                    const chart = context.chart;
                    const {ctx, chartArea} = chart;
                    if (!chartArea) {
                        return null;
                    }
                    // Create gradient
                    const gradient = ctx.createLinearGradient(0, 0, 0, 400);
                    gradient.addColorStop(0, 'rgba(76, 201, 240, 0.8)');
                    gradient.addColorStop(1, 'rgba(76, 201, 240, 0.2)');
                    return gradient;
                },
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: false
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        color: '#8d99ae'
                    }
                },
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        precision: 0,
                        color: '#8d99ae'
                    }
                }
            }
        }
    });
}

function initClickActivityChart(elementId) {
    const clickActivityCtx = document.getElementById(elementId).getContext('2d');
    return new Chart(clickActivityCtx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Clicks',
                data: [],
                backgroundColor: 'rgba(76, 201, 240, 0.3)',
                borderColor: 'rgba(76, 201, 240, 1)',
                tension: 0.4,
                fill: true,
                pointBackgroundColor: 'rgba(76, 201, 240, 1)',
                pointRadius: 4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: '#ffffff'
                    }
                },
                title: {
                    display: true,
                    text: 'URL Click Activity',
                    color: '#ffffff'
                }
            },
            scales: {
                x: {
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        color: '#8d99ae'
                    }
                },
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(255, 255, 255, 0.05)'
                    },
                    ticks: {
                        precision: 0,
                        color: '#8d99ae'
                    }
                }
            }
        }
    });
} 