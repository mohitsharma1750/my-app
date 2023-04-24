
const API_BASE_URL = 'http://localhost:5000';

export const uploadFile = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(`${API_BASE_URL}/upload`, {
    method: 'POST',
    // mode: 'no-cors',
    body: formData,
  }).then(response => {
    if (!response.ok) {
      throw new Error('Error uploading file');
    }
    return response;
  }).then(data => {
    console.log('File uploaded successfully:', data);
    return data;
  }).catch(error => {
    console.error(error);
  });

}
