import { Component, OnInit, Input } from '@angular/core';
import {Game} from '../game'
import {GameService} from '../game.service'
import{CategoryService} from '../category.service'
import { Category } from '../category';
import { Observable, Subject } from 'rxjs';
import {ActivatedRoute} from '@angular/router';
import {
  debounceTime, distinctUntilChanged, switchMap
} from 'rxjs/operators';

@Component({
  selector: 'app-games',
  templateUrl: './games.component.html',
  styleUrls: ['./games.component.css']
})
export class GamesComponent implements OnInit {

  games:Game[];
  topGames:Game[];
  categories:Category[];
  anythingFound:boolean=false
  searchGames$:Observable<Game[]>;
  private searchTerms = new Subject<string>();

  catId:number;
  @Input() searchName:String;
  constructor(private gameService:GameService, private catService: CategoryService, public route:ActivatedRoute) { }

  ngOnInit(): void {
    this.getGames()
    this.getTopGames()
    this.getCategories();
  }

  search(term:string):void{
    this.searchTerms.next(term)
  }

  searchGame(term:string):void{
    this.searchTerms.next(term)

  }

  getGames():void{
    let id = this.route.snapshot.paramMap.get('id');
    id = id.substr(1);
    this.catId = parseInt(id)
    this.gameService.getGameList(id)
      .subscribe(games=>{this.games = games});
  }

  getCategories():void{
    this.catService.getCategoryList()
      .subscribe(categories => this.categories=categories)
  }


  getTopGames(){
    this.gameService.getGameList("action")
      .subscribe(topGames => this.topGames = topGames.slice(0, 10));
  }

}
