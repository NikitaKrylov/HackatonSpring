import type { DomEventHandlerObject, YMapListener } from "@yandex/ymaps3-types";
import type { MarkerData } from "./Marker.svelte";

export function createCallbacks(events: Events): YMapListener {
    const clickCallback = (object: DomEventHandlerObject) => {
        if (object && object.type == "marker") {
            let data = object.entity.properties as MarkerData;
            events.click?.(data);
        }
    };

    const { YMapListener } = ymaps3;
    const mapListener = new YMapListener({
        layer: "any",
        onClick: clickCallback
    });
    return mapListener;
}

export type Events = {
    click?: (marker: MarkerData) => void;
};
