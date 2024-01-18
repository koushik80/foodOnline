document.addEventListener("DOMContentLoaded", function() {
        var currentYearElement = document.getElementById("currentYear");
        if (currentYearElement) {
            var currentYear = new Date().getFullYear();
            currentYearElement.innerHTML = 'All Rights Reserved. Developed By <a href="https://portfolio-koushik.netlify.app/">Koushik</a> &copy; ' + currentYear;
        }
    });