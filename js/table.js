
const NUM_ROWS = 6;

window.onload = () => {
  const formRow = document.getElementById('formRow');
  formRow.style.display = "none";

  const saveButton = document.getElementById('save');
  saveButton.style.display = "none";

  const addBtn = document.getElementById('addScore');
  addBtn.addEventListener('click', () => {
    // Show the form row
    if (formRow.style.display === 'none') {
      formRow.style.display = 'table-row';
    }

    // Show the save button
    if (saveButton.style.display === 'none') {
      saveButton.style.display = 'block';
    }
  });

  saveButton.addEventListener('click', () => {
    // Get a reference to the table
    const tableRef = document.getElementById('data');
        
    // Insert a row at the end of the table
    let newRow = tableRef.insertRow(tableRef.rows.length - 1);

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

    saveButton.style.display = 'none';
    formRow.style.display = 'none';
  });
};
