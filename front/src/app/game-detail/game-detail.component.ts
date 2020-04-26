import { Component, OnInit, Input } from '@angular/core';
import {GameService} from '../game.service'
import{HttpClient} from '@angular/common/http'
import { DomSanitizer } from '@angular/platform-browser';
import {Game} from '../game'
import {ActivatedRoute} from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-game-detail',
  templateUrl: './game-detail.component.html',
  styleUrls: ['./game-detail.component.css']
})
export class GameDetailComponent implements OnInit {

  safeURL
  game:Game
  path:String


  constructor(private location:Location, private gameService: GameService, public route: ActivatedRoute, private _sanitizer: DomSanitizer) { }

  @Input() changedName:String

  ngOnInit(): void {
    this.getGame()
  }

  getGame(){
    let id = this.route.snapshot.paramMap.get('id');
    id = id.substr(1);
    this.gameService.getGame(id)
      .subscribe(game=>{
        this.game = game
        this.safeURL = this._sanitizer.bypassSecurityTrustResourceUrl(this.game.video_path)   
      })
  }
  
  share(productName) {
    window.alert('The ' + productName +' has been added to the Cart!');
  }

  buy(productName){
    window.alert('You bought ' + productName + "!")
  }

  goBack(): void {
    this.location.back();
  }

  saveChanges():void{
    let id = this.route.snapshot.paramMap.get('id');
    id = id.substr(1);
    this.gameService.updateGame(this.game, id).subscribe(()=>this.goBack());
  }

  addToCart(game:Game){
    // this.cartService.addToCart(game)
  } 

}
