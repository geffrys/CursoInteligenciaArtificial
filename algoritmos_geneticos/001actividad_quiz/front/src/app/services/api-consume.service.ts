import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiConsumeService {

  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) { }

  evaluate(condiciones: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/evaluate`, condiciones);
  }

  getMoods(): Observable<any> {
    return this.http.get(`${this.apiUrl}/moods`);
  }

  getGenres(): Observable<any> {
    return this.http.get(`${this.apiUrl}/genres`);
  }
}
