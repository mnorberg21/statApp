
const NUM_ROWS = 6;

const addBtn = document.getElementById('addScore');

const inputWrapper = () => {
  const saveButton = document.getElementById('save');
  const newForm = document.getElementById('inputData');
  handleInput(saveButton, newForm)
};

const handleInput = (saveButton, newForm) => {
    // Get a reference to the table
    const tableRef = document.getElementById('data');
    
    // Insert a row at the end of the table
    let newRow = tableRef.insertRow();

    const formMapping = {
      0: 'date',
      1: 'course',
      2: 'score',
      3: 'fairways',
      4: 'greens',
      5: 'threePutts'
    };

    // Insert a row cells
    for (let i = 0; i < NUM_ROWS; i++) {     
      let newCell = newRow.insertCell(i);
      newCell.innerHTML = document.getElementById(formMapping[i]).value;
      document.getElementById(formMapping[i]).value = null;
    }

    // Hide form and button
    if (saveButton.style.display === 'block') {
      saveButton.style.display = 'none';
      newForm.style.display = 'none';
    }

    // Remove event listener
    saveButton.removeEventListener('click', inputWrapper);
};

addBtn.addEventListener('click', () => {
  // Collect references to HTML features
  const saveButton = document.getElementById('save');
  const newForm = document.getElementById('inputData');

  // Show the save button
  if (saveButton.style.display === 'none') {
    saveButton.style.display = 'block';
  }
  
  // Show the input form
  if (newForm.style.display === 'none') {
    newForm.style.display = 'block';
  }

  // Update table after form submission
  // Hide save button and form after submission
  saveButton.addEventListener('click', inputWrapper);
});
