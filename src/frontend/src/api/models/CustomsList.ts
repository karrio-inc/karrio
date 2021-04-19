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
    Customs,
    CustomsFromJSON,
    CustomsFromJSONTyped,
    CustomsToJSON,
} from './';

/**
 * 
 * @export
 * @interface CustomsList
 */
export interface CustomsList {
    /**
     * 
     * @type {string}
     * @memberof CustomsList
     */
    next?: string;
    /**
     * 
     * @type {string}
     * @memberof CustomsList
     */
    previous?: string;
    /**
     * 
     * @type {Array<Customs>}
     * @memberof CustomsList
     */
    results: Array<Customs>;
}

export function CustomsListFromJSON(json: any): CustomsList {
    return CustomsListFromJSONTyped(json, false);
}

export function CustomsListFromJSONTyped(json: any, ignoreDiscriminator: boolean): CustomsList {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'next': !exists(json, 'next') ? undefined : json['next'],
        'previous': !exists(json, 'previous') ? undefined : json['previous'],
        'results': ((json['results'] as Array<any>).map(CustomsFromJSON)),
    };
}

export function CustomsListToJSON(value?: CustomsList | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'next': value.next,
        'previous': value.previous,
        'results': ((value.results as Array<any>).map(CustomsToJSON)),
    };
}


