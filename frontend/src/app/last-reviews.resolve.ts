import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot } from '@angular/router';
import { Observable } from 'rxjs';
import {ApiService} from './api.service';

@Injectable()
export class LastReviewsResolve implements Resolve<any> {
  constructor(private apiService: ApiService) {}

  resolve(route: ActivatedRouteSnapshot): Observable<any> {
    return this.apiService.getLastReviews();
  }
}
