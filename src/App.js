import React, { useState } from 'react';
import ReactDOM from 'react-dom';
    //import { uploadFile } from './api';

const API_BASE_URL = 'http://localhost:5000';    

function App() {
  const [file, setFile] = useState(null);
  const [data, setData] = useState('');

  function handleSubmit(event) {
    event.preventDefault();
    uploadFile(file);
  }

  function handleFileChange(event) {
    setFile(event.target.files[0]);
  }

  const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(`${API_BASE_URL}/upload`, {
    method: 'POST',
    body: formData,
  }).then(response => {
    if (!response.ok) {
      throw new Error('Error uploading file');
    }
    response = response.json().then(response =>  setData(response))
    return response;
  }).catch(error => {
    console.error(error);
  });

}
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload File</button>
      </form>

      <pre>{data.text}</pre>
    </div>
  );
}


export default App;
