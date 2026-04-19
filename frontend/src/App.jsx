import { useState } from "react";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");
  const [mode, setMode] = useState("eli5");

  const handleSubmit = async () => {
    const res = await fetch("http://127.0.0.1:8000/explain", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ 
        text: input,
        mode: mode
      }),
    });

    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div className="container">
      <h1>Ask a question and choose the answering mode</h1>

      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter a question..."
      />

      <label>Choose mode:</label>

      <select value={mode} onChange={(e) => setMode(e.target.value)}>
        <option value="eli5">Explain like I'm 5</option>
        <option value="caveman">Explain like I'm a Caveman</option>
        <option value="super">Explain in super detail</option>
      </select>

      <button onClick={handleSubmit}>Explain</button>

      <p className="response">{response}</p>
    </div>
  );
}

export default App;