import { useState } from 'react';
import React from 'react';
import Ideagen from './ideagen';
function IdeaOutput({ response }) {
  
  //console.log("Response in IdeaOutput:", response); for debugging
  if (!response) return <p className='py-4'>No idea generated</p>;
  const cleanline = response.replace(/\/\*/g, ''); // Replace escaped newlines with actual newlines
  const lines = cleanline.split('\n');
  return (
    <div style={{ whiteSpace: 'pre-wrap', fontFamily: 'monospace' }}>
      {lines.map((line,index)=>{
        if (line.startsWith('App Name:')) {
          return <h2 key={index}>{line}</h2>;
        } else if (line.startsWith('Description:')) {
          return <p key={index}><strong>{line}</strong></p>;
        } else if (line.startsWith('Features:')) {
          return <h3 key={index}>{line}</h3>;
        } else if (line.startsWith('Technology Stack:')) {
          return <h3 key={index}>{line}</h3>;
        } else if (line.startsWith('Use Cases:')) {
          return <h3 key={index}>{line}</h3>;
        } else if (line.startsWith('Flow Structure:')) {
          return <h3 key={index}>{line}</h3>;
        } else {
          return <p key={index}>{line}</p>; // Default rendering for other lines
        }
      })}
    
      
    </div>
    
  );
};
  
  export default IdeaOutput;