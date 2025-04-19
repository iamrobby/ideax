import { useState } from 'react';
import axios from 'axios';


export default function AICodeDebugger() {
  const [code, setCode] = useState('');
  const [inputData, setInputData] = useState('');
  const [output, setOutput] = useState('');

  const runDebugger = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/fetch', {
        code,
        input_data: inputData
      });
      setOutput(response.data.output);
    } catch (error) {
      setOutput(`Error: ${error.response?.data?.message || error.message}`);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">AI Code Debugger</h1>

      <label className="block font-semibold mb-2">Code:</label>
      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        rows="8"
        className="w-full p-2 border rounded mb-4 font-mono"
        placeholder="Enter your Python code here"
      />

      <label className="block font-semibold mb-2">Input Data:</label>
      <textarea
        value={inputData}
        onChange={(e) => setInputData(e.target.value)}
        rows="4"
        className="w-full p-2 border rounded mb-4 font-mono"
        placeholder="Enter simulated input() values (e.g. foo\nbar)"
      />

      <button
        onClick={runDebugger}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        Run
      </button>

      <div className="mt-6">
        <h2 className="font-semibold">Output:</h2>
        <pre className="bg-gray-200 p-4 rounded whitespace-pre-wrap">{output}</pre>
      </div>
    </div>
  );
}