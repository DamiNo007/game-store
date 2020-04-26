import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Game} from './game'

export class LoginResponse {
  token: string;
}

export class DeleteResponse{
  deleted:Boolean;
}

@Injectable({
  providedIn: 'root'
})
export class GameService {

  constructor(private http:HttpClient) { }

  BASE_URL = 'http://127.0.0.1:8000';

  getGameList(id): Observable<Game[]> {
    return this.http.get<Game[]>(`${this.BASE_URL}/categories/${id}/games/`);
  }

  getGame(id) :Observable<Game>{
    return this.http.get<Game>(`${this.BASE_URL}/games/${id}/`)
  }

  updateGame(game:Game, id):Observable<Game>{
    return this.http.put<Game>(`${this.BASE_URL}/games/${id}/`,{
      game
    })
  }
}
