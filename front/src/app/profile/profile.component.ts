import { Component, OnInit, Input} from '@angular/core';
import {Game} from '../game';
import {GameService} from '../game.service';
import {CategoryService} from '../category.service';
import { Category } from '../category';
import { Observable, Subject } from 'rxjs';
import {User} from '../user'
import {UserService} from '../user.service'
import {GameBox} from '../box'

import {
  debounceTime, distinctUntilChanged, switchMap
} from 'rxjs/operators';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  currentUser: User
  games: Game[];
  categories: Category[];
  jsonStr: string
  box:GameBox

  constructor(private userService: UserService, private gameDetService: GameService, private catService: CategoryService) { }


  ngOnInit(): void {
    this.jsonStr = localStorage.getItem('user')
    let jsonObj: any = JSON.parse(this.jsonStr); 
    this.currentUser = <User>jsonObj
    this.getGameBox()
  }

  getGameBox(){
    this.userService.getGameBox(this.currentUser.id)
      .subscribe(box => {
        this.box = box
        this.getGames()
      }  
      );
  }

  getGames(): void {
    this.userService.getUserGames(this.box.id)
      .subscribe(games => {
        this.games = games}  
      );
  }
}
