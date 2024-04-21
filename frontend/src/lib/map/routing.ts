import { PUBLIC_ROUTING_KEY } from "$env/static/public";
import type { LngLat, YMap } from "@yandex/ymaps3-types";

/** Only call after ymap3.ready */
export const addLine = (map: YMap, coordinates: LngLat[]) => {
    const { YMapFeature } = ymaps3;

    const lineStringFeature = new YMapFeature({
        geometry: {
            type: "LineString",
            coordinates
        },
        style: {
            stroke: [{ width: 3, color: "#F35757" }]
        }
    });
    map.addChild(lineStringFeature);
    return lineStringFeature;
};

export const fetchRoute = async (coords: LngLat[]) => {
    const url = "https://api.openrouteservice.org/v2/directions/driving-car/geojson";
    const body = JSON.stringify({ coordinates: coords });
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: PUBLIC_ROUTING_KEY
        },
        body
    });
    const data: RouteData = await response.json();
    return data.features[0].geometry.coordinates as LngLat[];
};

type RouteData = {
    type: "FeatureCollection";
    bbox: [number, number, number, number];
    features: [
        {
            bbox: [number, number, number, number];
            type: "Feature";
            properties: {
                segments: unknown[];
                summary: { distance: number; duration: number };
                way_points: [0, 23];
            };
            geometry: {
                coordinates: LngLat[];
                type: "LineString";
            };
        }
    ];
    metadata: unknown;
};
