/* tslint:disable */
/* eslint-disable */
/**
 * Purplship API
 *  ## API Reference  Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services.  The Purplship API is organized around REST. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  The Purplship API differs for every account as we release new versions. These docs are customized to your version of the API.   ## Versioning  When backwards-incompatible changes are made to the API, a new, dated version is released.  The current version is `2021.2.1`.   Read our API changelog and to learn more about backwards compatibility.  As a precaution, use API versioning to check a new API version before committing to an upgrade. 
 *
 * The version of the OpenAPI document: 2021.2.1
 * Contact: hello@purplship.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import {
    Shipment,
    ShipmentFromJSON,
    ShipmentFromJSONTyped,
    ShipmentToJSON,
} from './';

/**
 * 
 * @export
 * @interface ShipmentList
 */
export interface ShipmentList {
    /**
     * 
     * @type {string}
     * @memberof ShipmentList
     */
    next?: string;
    /**
     * 
     * @type {string}
     * @memberof ShipmentList
     */
    previous?: string;
    /**
     * 
     * @type {Array<Shipment>}
     * @memberof ShipmentList
     */
    results: Array<Shipment>;
}

export function ShipmentListFromJSON(json: any): ShipmentList {
    return ShipmentListFromJSONTyped(json, false);
}

export function ShipmentListFromJSONTyped(json: any, ignoreDiscriminator: boolean): ShipmentList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': ((json['results'] as Array<any>).map(ShipmentFromJSON)),
    };
}

export function ShipmentListToJSON(value?: ShipmentList | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'next': value.next,
        'previous': value.previous,
        'results': ((value.results as Array<any>).map(ShipmentToJSON)),
    };
}


