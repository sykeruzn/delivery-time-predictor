<?php

namespace App\Http\Controllers;

use App\Models\Delivery;
use App\Jobs\PredictDeliveryTime;
use Illuminate\Http\Request;

class DeliveryController extends Controller
{
    public function predict(Request $request)
    {
        $data = $request->only('distance_km', 'fuel_used');

        $response = Http::post('http://127.0.0.1:5000/predict', $data);

        return response()->json([
            'predicted_time' => $response->json()['eta_minutes'],
        ]);
    }

    public function store(Request $request)
    {
        $delivery = Delivery::create([
            'location' => $request->location,
            'distance_km' => $request->distance_km,
            'fuel_used' => $request->fuel_used,
        ]);

        // Dispatch job
        PredictDeliveryTime::dispatch($delivery);

        return response()->json([
            'message' => 'Delivery created and prediction job dispatched!',
            'data' => $delivery,
        ]);
    }
}
