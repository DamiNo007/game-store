import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable, from} from 'rxjs';
import {Category} from './category'

export class LoginResponse {
  token: string;
}

export class DeleteResponse{
  deleted:Boolean;
}

@Injectable({
  providedIn: 'root'
})

export class CategoryService {

  constructor(private http: HttpClient) { }
  BASE_URL = 'http://127.0.0.1:8000';
  getCategoryList(): Observable<Category[]> {
    return this.http.get<Category[]>(`${this.BASE_URL}/categories/`);
  } 
}


