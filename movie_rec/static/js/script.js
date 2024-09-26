const searchBar = document.getElementById('search-input');
const box = document.getElementById('box');

searchBar.addEventListener('click', function() {
    if(box.classList.contains('visible')){
        box.classList.remove('visible');
        box.classList.add('hidden');
    } else {
        box.classList.remove('hidden');
        box.classList.add('visible');
    }
    
    
    function handleCheckbox(checkbox) {
      var isChecked = checkbox.checked;
      var optionText = checkbox.parentNode.textContent.trim();
      console.log('Option ' + optionText + ' is ' + (isChecked ? 'checked' : 'unchecked'));
      // Perform any desired action based on the checkbox state
    }
})
