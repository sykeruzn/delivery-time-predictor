import { useState } from 'react';
import axios from 'axios';

export default function PredictPage() {
  const [distance, setDistance] = useState(0);
  const [fuel, setFuel] = useState(0);
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const res = await axios.post('http://localhost:8000/predict-delivery-time', {
      distance_km: distance,
      fuel_used: fuel,
    });
    setResult(res.data.predicted_time);
  };

  return (
    <div className="p-6">
      <h2>Delivery Time Predictor</h2>
      <input type="number" placeholder="Distance (km)" onChange={(e) => setDistance(Number(e.target.value))} />
      <input type="number" placeholder="Fuel Used (liters)" onChange={(e) => setFuel(Number(e.target.value))} />
      <button onClick={handleSubmit}>Predict</button>
      {result && <p>Estimated Time: {result} mins</p>}
    </div>
  );
}
