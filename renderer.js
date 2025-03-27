// renderer.js
const { ipcRenderer } = require('electron');

document.addEventListener('DOMContentLoaded', () => {
  const promptBtn = document.getElementById('promptBtn');
  const resultDiv = document.getElementById('result');

  promptBtn.addEventListener('click', () => {
    const userInput = prompt('Enter something:');
    if (userInput !== null) {
      resultDiv.textContent = `You entered: ${userInput}`;
    }
  });
});
