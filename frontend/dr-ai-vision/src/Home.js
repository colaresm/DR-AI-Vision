import React from "react";
import { useNavigate } from "react-router-dom";
import "./App.css";

function HomePage() {
  const navigate = useNavigate();

  const handleRedirect = () => {
    navigate("/upload");
  };

  return (
    <div className="home-container">
      <header className="home-header">
        <h1 className="home-title">DR-AI-VISION</h1>
        <p className="home-subtitle">
          Inteligência Artificial para Diagnóstico da Retinopatia Diabética
        </p>
      </header>

      <main>
        <button className="home-button" onClick={handleRedirect}>
          Enviar Imagem para Análise
        </button>
      </main>
    </div>
  );
}

export default HomePage;
