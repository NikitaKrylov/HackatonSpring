import Marker, { type MarkerData } from "./Marker.svelte";
import type { YMapMarker, YMap } from "@yandex/ymaps3-types";

export const addMarker = (map: YMap, data: MarkerData, click: (data: MarkerData) => void) => {
    const marker = createMarkerElem(data, click);
    map.addChild(marker);
    return marker;
};

function createMarkerElem(marker: MarkerData, click: (data: MarkerData) => void): YMapMarker {
    const markerElement = document.createElement("div");
    new Marker({
        target: markerElement,
        props: { data: marker, click }
    });
    return new ymaps3.YMapMarker(
        {
            coordinates: marker.location,
            properties: marker
        },
        markerElement
    );
}
