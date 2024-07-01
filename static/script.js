document.addEventListener('DOMContentLoaded', (event) => {
    const reportList = document.getElementById('report-list');
    const reportContent = document.getElementById('report-content');
    
    if (reportList) {
        const currentUsername = reportList.dataset.username;
        const links = reportList.getElementsByClassName('report-link');
        for (let link of links) {
            link.addEventListener('click', function(event) {
                if (link.dataset.user !== currentUsername && currentUsername !== 'admin') {
                    alert('Access Denied');
                    event.preventDefault();
                }
            });
        }
    }
    
    if (reportContent) {
        const currentUsername = reportContent.dataset.username;
        const sessionUsername = reportContent.dataset.username;
        if (currentUsername !== sessionUsername && sessionUsername !== 'admin') {
            document.body.innerHTML = '<h2>Access Denied</h2>';
        }
    }
});
