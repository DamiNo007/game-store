import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {User} from './user'
import {Game} from './game'
import {GameBox} from './box'
import {Cart} from './cart'

export class LoginResponse {
  token: string;
}

export class DeleteResponse{
  deleted:Boolean;
}

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  user:User
  BASE_URL = 'http://127.0.0.1:8000';


  login(username, password): Observable<LoginResponse> {
    return this.http.post<LoginResponse>(`${this.BASE_URL}/login/`, {
      username,
      password
    });
  }

  getUser(username): Observable<User>{
    return this.http.get<User>(`${this.BASE_URL}/users/${username}/`)
  }

  getUserGames(box_id):Observable<Game[]>{
    return this.http.get<Game[]>(`${this.BASE_URL}/${box_id}/usergames/`)
  }

  getCartGames(cart_id):Observable<Game[]>{
    return this.http.get<Game[]>(`${this.BASE_URL}/${cart_id}/cartgames/`)
  }

  getCart(user_id):Observable<Cart>{
    return this.http.get<Cart>(`${this.BASE_URL}/${user_id}/cart/`)
  }

  getGameBox(user_id):Observable<GameBox>{
    return this.http.get<GameBox>(`${this.BASE_URL}/${user_id}/game_box/`)
  }

  deinitiaizeUser(){
    this.user = null
  }

  initializeUser(user){
    this.user = user
  }

  returnUser(){
    return this.user
  }
}
