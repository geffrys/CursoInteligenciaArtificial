import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MusicExpertServiceService {

  private urlEvaluate = 'http://localhost:8000/evaluate';
  private urlMoods = 'http://localhost:8000/moods';
  private urlGenres = 'http://localhost:8000/genres';

  constructor(private http: HttpClient) { }

  evaluate(person: any): Observable<any> {
    return this.http.post(this.urlEvaluate, person);
  }

  getMoods(): Observable<any> {
    return this.http.get(this.urlMoods);
  }

  getGenres(): Observable<any> {
    return this.http.get(this.urlGenres)
  }
}
