import { Component, OnInit } from '@angular/core';
import {CartService} from '../cart.service' 
import {GameService} from '../game.service'
import {Game} from '../game'
import {Cart} from '../cart'
import {UserService} from '../user.service'
import {User} from '../user'

@Component({
  selector: 'app-cart',
  templateUrl: './cart.component.html',
  styleUrls: ['./cart.component.css']
})
export class CartComponent implements OnInit {


  cartElems:Cart[] 
  totalPrice: number

  totalCount: number

  jsonStr:string
  currentUser:User
  cart: Cart
  games: Game[]

  constructor(private userService:UserService, private gameService:GameService) { 
  }

  ngOnInit(): void {
    this.jsonStr = localStorage.getItem('user')
    let jsonObj: any = JSON.parse(this.jsonStr); 
    this.currentUser = <User>jsonObj
    this.getCart()
  }


  
  getCart(){
    this.userService.getCart(this.currentUser.id)
      .subscribe(cart => {
        this.cart = cart
        this.getGames()
      }  
      );
  }

  getGames(): void {
    this.userService.getCartGames(2)
      .subscribe(games => {
        this.games = games}  
      );
  }



  removeFromCart(cartElem:Cart){
    // this.cartService.removeFromCart(cartElem).subscribe();
    // this.cartElems = this.cartElems.filter(c => c !== cartElem);
    // this.getTotalPrice()
    // this.getTotalCount()
  }

  getTotalPrice(){
    // this.totalPrice=this.cartService.getTotalPrice()
  }

  getTotalCount(){
    // this.totalCount = this.cartService.getTotalCount()
  }

  getCartElems():void{
    // this.cartService.getCartElems()
    //   .subscribe(cartElems=>this.cartElems = cartElems)
  }

  onSelect(game:Game):void{
    // this.gameService.initializeGame(game)
  }

}
