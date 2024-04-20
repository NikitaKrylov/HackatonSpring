import { PUBLIC_ROUTING_KEY } from "$env/static/public";
import type { LngLat, YMap } from "@yandex/ymaps3-types";

/** Only call after ymap3.ready */
export const addLine = (map: YMap, coordinates: LngLat[]) => {
    const { YMapFeature } = ymaps3;

    const lineStringFeature = new YMapFeature({
        id: "line",
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

export const fetchRoute = async (from: LngLat, to: LngLat) => {
    const url = buildUrl(from, to);
    const response = await fetch(url);
    const data: RouteData = await response.json();
    const coords = data.features[0].geometry.coordinates;
    return coords;
};

const buildUrl = (from: LngLat, to: LngLat) => {
    const baseUrl = "https://api.openrouteservice.org/v2/directions/driving-car";
    const api_key = `api_key=${PUBLIC_ROUTING_KEY}`;
    const start = `start=${from[0]},%20${from[1]}`;
    const end = `end=${to[0]},%20${to[1]}`;
    return `${baseUrl}?${api_key}&${start}&${end}`;
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
