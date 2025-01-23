<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Parakh Quiz Solver</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css">
</head>
<body>
  <article class="markdown-body">
    <h1>Parakh Quiz Solver</h1>

    <p>This project provides a tool to automate answering questions on the Parakh platform.  It leverages the power of Google Gemini's large language model to analyze questions and provide accurate answers.  **Use this tool responsibly and ethically, adhering to Parakh's terms of service.**</p>

    <h2>Getting Started</h2>

    <ol>
      <li><strong>Prerequisites:</strong>  Ensure you have Python 3 installed. You will also need to obtain a Google Gemini API key.</li>
      <li><strong>Installation:</strong> Clone this repository: <code>git clone <repository_url></code></li>
      <li><strong>API Key:</strong> Replace <code>API_KEY_HERE</code> in <code>main.py</code> with your actual Google Gemini API key.</li>
      <li><strong>Run the Solver:</strong> Start the Python script: <code>python3 main.py</code></li>
      <li><strong>Open Parakh and Login:</strong> Open your Parakh quiz in a browser.</li>
      <li><strong>Open Developer Tools:</strong> In your browser, open the developer console (usually by pressing F12).</li>
      <li><strong>Paste and Run:</strong> Copy the contents of <code>console.js</code> and paste it into the browser's console.  Press Enter.</li>
      <li><strong>Answering Questions:</strong> Click on the question number to get the answer via an alert.  Mark the answer and proceed to the next question.</li>
      <li><strong>NaN Handling:</strong> If the script returns "NaN" (Not a Number) for an answer, restart the <code>python3 main.py</code> process.</li>
    </ol>

    <h2>Files</h2>
    <ul>
      <li><code>main.py</code>: The main Python script that interacts with the Google Gemini API.</li>
      <li><code>console.js</code>: The JavaScript code to be injected into the Parakh browser console.</li>
    </ul>

    <h2>Demo Video</h2>
    <p>
      <a href="<video_link_here>">
        <img src="<gif_image_here>" alt="Demo GIF" width="600">
      </a>
    </p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Disclaimer</h2>
    <p>This tool is provided "as is" without warranty of any kind. Use at your own risk. The authors are not responsible for any misuse or consequences resulting from the use of this tool.  Always respect the terms of service of the Parakh platform.</p>

  </article>
</body>
</html>