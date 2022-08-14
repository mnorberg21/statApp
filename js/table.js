
const NUM_COLS = 6;

window.onload = () => {

  const formRow = document.getElementById('formRow');
  formRow.style.display = "none";

  const saveButton = document.getElementById('save');
  saveButton.style.display = "none";

  const tableRef = document.getElementById('data');

  const formMapping = {
    0: 'date',
    1: 'course',
    2: 'score',
    3: 'fairways',
    4: 'greens',
    5: 'threePutts'
  };

  // Initialize table
  fetch('http://127.0.0.1:5001/rest').then(res => {
    return res.json();
  }).then(text => {
    console.log('GET Initialization Response:');
    console.log(text);
    for (let i = 0; i < text.length; i++) {
      let newRow = tableRef.insertRow(tableRef.rows.length - 1);
      for (let j = 0; j < NUM_COLS; j++) {     
        let newCell = newRow.insertCell(j);
        newCell.innerHTML = (text[i])[formMapping[j]];
      }
    }
  });

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
    // Insert a row at the end of the table
    let newRow = tableRef.insertRow(tableRef.rows.length - 1);

    // Store the new object to be submitted
    let addObj = {}

    // Insert row cells
    for (let i = 0; i < NUM_COLS; i++) {     
      let newCell = newRow.insertCell(i);
      newCell.innerHTML = document.getElementById(formMapping[i]).value;
      addObj[formMapping[i]] = document.getElementById(formMapping[i]).value;
      document.getElementById(formMapping[i]).value = null;
    }

    // Post request options
    let options = {
      method: 'POST',
      body: JSON.stringify(addObj),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    };

    // Post operation status
    fetch('http://127.0.0.1:5001/rest', options).then(res => {
      return res.json();
    }).then(text => {
      console.log('POST Operation Status');
      console.log(text);
    });

    saveButton.style.display = 'none';
    formRow.style.display = 'none';
  });
};
