import { Component, OnInit } from '@angular/core';
import {UserService} from '../user.service'
import {User} from '../user'

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor(private userService: UserService) { }
  currentUser:User
  jsonStr: string
  ngOnInit(): void {
    this.jsonStr = localStorage.getItem('user')
    let jsonObj: any = JSON.parse(this.jsonStr); 
    this.currentUser = <User>jsonObj
  }
}
