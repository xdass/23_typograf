/**
 * Created by Dass on 25.01.2018.
 */
const form = document.getElementById('raw_text_form');
const original_text = document.getElementById('original_text');
const result_text = document.getElementById('result_text');

form.addEventListener('submit', function(e) {
  e.preventDefault()
  fetch('http://127.0.0.1:5000/action',
    {
       headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      method: 'POST',
      body: JSON.stringify({'text': original_text.value})
    })
    .then(response => response.json())
    .then(json_data => {
      result_text.disabled = false
      result_text.textContent = json_data['beauty_text']
    })
});