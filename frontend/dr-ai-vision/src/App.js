import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import HomePage from "./Home.js";
import UploadPage from "./pages/AnalysisReportIndividual.js";

function App() {
  return (
    <Router>
      <Routes>
        {/* Rota inicial (home) */}
        <Route path="/" element={<HomePage />} />

        {/* Rota de upload */}
        <Route path="/upload" element={<UploadPage />} />

        {/* Redirecionamento padrão caso a rota não exista */}
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </Router>
  );
}

export default App;
