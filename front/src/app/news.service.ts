import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { News } from './news';
import { Observable, of } from 'rxjs';

export class LoginResponse {
  token: string;
}

export class DeleteResponse{
  deleted:Boolean;
}

@Injectable({
  providedIn: 'root'
})
export class NewsService {

  constructor(private http: HttpClient) { }
  BASE_URL = 'http://127.0.0.1:8000';

  getNews(): Observable<News[]> {
    return this.http.get<News[]>(`${this.BASE_URL}/news/`)
  }

  getNewsDetail(id):Observable<News>{
    return this.http.get<News>(`${this.BASE_URL}/news/${id}/`)
  }
}
