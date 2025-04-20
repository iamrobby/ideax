import React from "react";
import { useState } from 'react';
function Ideagen({idea, setIdea, onGenerate}) {
  const[track, setTrack] = useState("AI");
  const[techstack, setTechStack] = useState("mern stack");
  const handlegenretaClick=()=>{
    onGenerate({idea,track,techstack});
  };
  return (
    <div className="Ideagen bg-gradient-to-tr from-pink-300 to-blue-300 p-8 rounded-lg shadow-lg max-w-md mx-auto mt-10">
      <h1 className="text-4xl"><span className="text-blue-700">AI IDEA</span><span className="text-black"> Generator</span></h1>
      <p className="text-xl text-gray-700 text-center">Enter your idea:</p>
      <textarea
        type="text"
        placeholder="Enter your idea here"
        className="border-2 border-gray-300 rounded-lg p-2 mb-4 w-full max-w-lg resize-y"
            value={idea}
            onChange={(e) => setIdea(e.target.value)}
            ></textarea>
            <label className="text-xl text-gray-700 mt-4 block">Select a Track to build on:</label>
      <select className="border-2 border-pink-300 rounded-lg p-2 mb-4 w-full max-w-lg resize-y"
      value={track}
      onChange={(e)=>setTrack(e.target.value)}>
        <option value="AI">AI</option>
        <option value="softeare tech">Software</option>
        <option value="health">Health</option>
        <option value="education">Education</option>
        <option value="entertainment">Entertainment</option>
        
      </select>
      <label className="text-xl text-gray-700 mt-4 block">Select a Preferred tech Stack:</label>
      <select className="border-2 border-gray-300 rounded-lg p-2 mb-4 w-full max-w-md resize-y"
      value={techstack}
      onChange={(e)=>setTechStack(e.target.value)}>
        <option value="mern stack">MERN</option>
        <option value="mean stack">MEAN</option>
        <option value="java stack">JAVA FULL STACK</option>
        <option value="LAMP">LAMP</option>
      </select>
      <p>
      <button className="rounded-sm bg-black px-6 py-2 text-white border-r-pink-300" onClick={handlegenretaClick}>Generate</button>
        </p>    
    </div>
  );
}
export default Ideagen;