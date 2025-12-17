import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [summaryData, setSummaryData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSummaryData = async () => {
      try {
        const response = await axios.get('/api/analysis/summary');
        setSummaryData(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchSummaryData();
  }, []);

  if (loading) {
    return <div>Loading summary data...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>TACTIC Climate-Health Summary</h1>
      {summaryData && (
        <div style={{ border: '1px solid #ccc', padding: '15px', borderRadius: '8px' }}>
          <p><strong>Total Cases:</strong> {summaryData.total_cases}</p>
          <p><strong>Average Temperature:</strong> {summaryData.avg_temperature}°C</p>
          <p><strong>Total Rainfall:</strong> {summaryData.total_rainfall} mm</p>
          <p><strong>Population at Risk:</strong> {summaryData.population_at_risk}</p>
          <p><strong>Data Quality:</strong> {summaryData.data_quality}%</p>
          <p><strong>Last Updated:</strong> {new Date(summaryData.last_updated).toLocaleString()}</p>
        </div>
      )}
    </div>
  );
}

export default App;