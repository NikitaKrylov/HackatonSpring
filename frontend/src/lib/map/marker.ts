import Marker, { type MarkerData } from "./Marker.svelte";
import type { YMapMarker, YMap } from "@yandex/ymaps3-types";

export const addMarker = (map: YMap, data: MarkerData) => {
    const marker = createMarkerElem(data);
    map.addChild(marker);
    return marker;
};

function createMarkerElem(marker: MarkerData): YMapMarker {
    const markerElement = document.createElement("div");
    new Marker({
        target: markerElement,
        props: { data: marker }
    });
    return new ymaps3.YMapMarker(
        {
            coordinates: marker.location,
            properties: marker
        },
        markerElement
    );
}
