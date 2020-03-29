import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseUrl = 'http://127.0.0.1:8000';
  httpHeaders = new HttpHeaders(
    {'Content-Type': 'application/json'}
  );

  constructor(private http: HttpClient) { }

  getAllUniversities(): Observable<any> {
    return this.http.get(this.baseUrl + '/api/universities/',
      {headers: this.httpHeaders});
  }


  getMetrics(): Observable<any> {
    return this.http.get(this.baseUrl + '/api/metrics/', {headers: this.httpHeaders});
  }

  getProfessors(): Observable<any> {
    return this.http.get(this.baseUrl + '/api/professors/', {headers: this.httpHeaders});
  }

}
