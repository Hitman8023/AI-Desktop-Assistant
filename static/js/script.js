async function postData(url = "", data = {}) {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json", // Corrected the Content-Type
      },
      body: JSON.stringify(data),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const responseData = await response.json();
    return responseData;
  } catch (error) {
    console.error("Error during POST request:", error.message);
    throw error; // Rethrow the error for higher-level handling if needed
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const voiceButton = document.getElementById("voiceButton");
  const questionInput = document.getElementById("questionInput");
  const sendButton = document.getElementById("sendButton");
  const right2 = document.querySelector(".right2");
  const right1 = document.querySelector(".right1");
  const question1 = document.getElementById("question1");
  const question2 = document.getElementById("question2");
  const solution = document.getElementById("solution");

  if (window.SpeechRecognition || window.webkitSpeechRecognition) {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();

    recognition.continuous = true;
    recognition.interimResults = true;

    let isListening = false;

    voiceButton.addEventListener("click", function () {
      if (!isListening) {
        isListening = true;
        recognition.start();
      } else {
        isListening = false;
        recognition.stop();
      }
    });

    sendButton.addEventListener("click", async () => {
      try {
        const questionValue = questionInput.value;
        questionInput.value = "";
        right2.style.display = "block";
        right1.style.display = "none";

        question1.innerHTML = questionValue;
        question2.innerHTML = questionValue;

        // Send the questionValue to the server using POST request
        const result = await postData("/process_voice_input", { question: questionValue });
 
        // Now you can use the result from the server as needed
        solution.innerHTML = result.answer;
      } catch (error) {
        // Handle the error as needed (e.g., display an error message to the user)
        console.error("Error during button click:", error.message);
      }
    });

    recognition.onresult = function (event) {
      const result = event.results[event.results.length - 1];
      const transcript = result[0].transcript;

      questionInput.value = transcript;
    };

    recognition.onend = function () {
      if (isListening) {
        recognition.start();
      }
    };
  } else {
    // Browser doesn't support Web Speech API
    console.error("Your browser doesn't support the Web Speech API. Please use a compatible browser.");
  }
});

document.getElementById("newChatButton").addEventListener("click", function() {
  location.reload(); // Reload the current page
});

document.addEventListener("DOMContentLoaded", function () {
  var input = document.getElementById("questionInput");

  input.addEventListener("keyup", function (event) {
      if (event.keyCode === 13) {
          event.preventDefault();
          document.getElementById("sendButton").click();
      }
 });
});
