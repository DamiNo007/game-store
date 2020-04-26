import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Review } from './review';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})


export class ReviewService {
    
  constructor(private http:HttpClient) { }
  BASE_URL = 'http://127.0.0.1:8000';

  getReviews(): Observable<Review[]> {
    return this.http.get<Review[]>(`${this.BASE_URL}/reviews/`)
  }

  getReview(id): Observable<Review>{
      return this.http.get<Review>(`${this.BASE_URL}/reviews/${id}/`)
  }
}