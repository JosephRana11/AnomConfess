
(function () {
  var btn = document.getElementsByClassName("feedback-body__submit")[0];
  btn.onclick = function(e) {
    e.preventDefault();

    // Get the CSRF token from the HTML
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // Example AJAX request
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '{% url "IndexLink" %}');
    xhr.setRequestHeader('X-CSRFToken', csrfToken);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        // Handle response
        if (xhr.status === 200) {
          
        }
      }
    };
    xhr.send();
  };
})();

