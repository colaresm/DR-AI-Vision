import React, { useState } from "react";
import "./UploadPage.css";

function UploadPage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);

    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreviewUrl(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleUpload = () => {
    if (!selectedFile) {
      alert("Por favor, selecione uma imagem antes de enviar.");
      return;
    }
    alert(`Imagem "${selectedFile.name}" enviada com sucesso!`);
    
  };

  return (
    <div className="upload-container">
      <header className="upload-header">
        <h1 className="upload-title">Envio de Imagem</h1>
        <p className="upload-subtitle">
          Carregue uma imagem de retina para análise com o DR-AI-VISION
        </p>
      </header>

      <main className="upload-content">
        <div className="upload-box">
          <input
            type="file"
            accept="image/*"
            id="fileInput"
            onChange={handleFileChange}
            hidden
          />
          <label htmlFor="fileInput" className="upload-label">
            {selectedFile ? "Alterar imagem" : "Selecionar imagem"}
          </label>

          {previewUrl && (
            <div className="image-preview">
              <img src={previewUrl} alt="Preview" />
            </div>
          )}

          <button className="upload-button" onClick={handleUpload}>
            Enviar para Análise
          </button>
        </div>
      </main>
    </div>
  );
}

export default UploadPage;
