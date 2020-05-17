import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import {Comment} from './comment';
import {University} from './university';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  baseUrl = 'https://api.ocenika.com';
  httpHeaders = new HttpHeaders(
    {'Content-Type': 'application/json'}
  );

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(private http: HttpClient) { }

  getAllUniversities() {
    return this.http.get(this.baseUrl + '/api/universities/',
      {headers: this.httpHeaders})
      .pipe(
        catchError(this.handleError<any>('get universities', []))
      );
  }


  getMetrics(): Observable<any> {
    return this.http.get(this.baseUrl + '/api/metrics/', {headers: this.httpHeaders});
  }

  getProfessors(): Observable<any> {
    return this.http.get(this.baseUrl + '/api/professors/', {headers: this.httpHeaders});
  }

  getProfessor(id): Observable<any> {
    return this.http.get(this.baseUrl + '/api/professors/' + id + '/', {headers: this.httpHeaders});
  }

  addComment(comment: Comment): Observable<any> {
    return this.http.post(this.baseUrl + '/api/ratings/', comment, this.httpOptions);
  }

  getProfessorRatingCount(id): Observable<any> {
    return this.http.get(this.baseUrl + '/api/ratings/total_ratings/', {params: {professor_id: id}, headers: this.httpHeaders});
  }

  getProfessorsByUniversity(id): Observable<any> {
    return this.http.get(this.baseUrl + '/api/professors/', {params: {universities: id}, headers: this.httpHeaders});
  }

  getProfessorByName(name): Observable<any> {
    return this.http.get(this.baseUrl + '/api/professors/', {params: {search: name}, headers: this.httpHeaders});
  }

  getProfessorRatings(professorId) {
    return this.http.get(this.baseUrl + '/api/ratings/', {params: {professor: professorId}, headers: this.httpHeaders});
  }

  getLastReviews() {
    return this.http.get(this.baseUrl + '/api/ratings/last_ratings/');
  }

  getPolicyURL() {
    return this.http.get(this.baseUrl + '/api/policy');
  }


  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      return of(result as T);
    };
  }

}
