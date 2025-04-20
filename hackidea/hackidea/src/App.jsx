import React from 'react';
import { useState } from 'react';
import Ideagen from './components/ideagen';
import IdeaOutput from './components/ideaoutput';
import './App.css';

function App() {
  const [idea, setIdea] = useState(''); 
  const [track, setTrack] = useState('AI');
  const [techstack, setTechStack] = useState('mern stack');
  const [response, setResponse] = useState('');
    const handlegenerate= async()=>{
      try{
        const res=await fetch('http://127.0.0.1:5001/generate', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ idea,track,techstack}), // Send the idea to the backend
        });
        const data = await res.text();
        setResponse(data); // Update the response state with the result
      } catch (error) {
        console.error('Error:', error);
        setResponse("Error! Please try again."); // Handle error case
      }
    };
      
  return (
    <div className='text-center'>      
            <Ideagen idea={idea} setIdea={setIdea} onGenerate={handlegenerate} />
            <div className='text-center bg-gradient-to-tr from-pink-300 to-blue-300 text-blue-900 font-bold text-2xl rounded-lg p-4 mx-10 mt-10'>
            <IdeaOutput response={response} />
            </div>
    </div>
  );
}

export default App
