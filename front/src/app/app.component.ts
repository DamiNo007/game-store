import { Component , Input} from '@angular/core';
import {User} from "./user"
import {UserService} from './user.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'GAMESTORE';
  logged = false;
  loginForm = true;
  registerForm = false;

  constructor(private userService:UserService) { }
  
  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }
  wantToLogin(){
    this.loginForm = true
    this.registerForm = false
  }

  wantToRegister(){
    this.registerForm = true
    this.loginForm = false
  }


  /**LOGIN PART */
  @Input() first_name:string;
  @Input() password:string;

  userFullName:string;

  login() {
    this.userService.login(this.first_name, this.password)
      .subscribe(res => {

        localStorage.setItem('token', res.token);

        this.logged = true;

        this.getUser()

        this.first_name = '';
        this.password = '';
      });
  }

  getUser(){
    this.userService.getUser(this.first_name).subscribe(user =>{
      localStorage.setItem('user', JSON.stringify(user));
    });
  }

  

  logout() {
    localStorage.clear();
    this.logged = false;
  }

  // login(){
  //   for (let user of this.users){
  //     if(user.email.match(this.email)!=null && user.password.match(this.password)){
  //       this.userFullName = user.firstName + " " + user.lastName
  //       this.welcome()
  //     }
  //     else{
  //       this.error()
  //     }
  //   }
  // }


  welcome(name){
    window.alert('Welcome, ' + name +'!');
  }

  error(){
    window.alert('Incorrect login or password!')
  }

  /**REGISTER PART */



  @Input() userName:string
  @Input() userLastName:string
  @Input() userEmail:string
  @Input() userPassword:string

  createNewUser(){
    // this.user = {
    //   id:null,
    //   firstName:this.userName,
    //   lastName:this.userLastName,
    //   email:this.userEmail,
    //   password:this.userPassword
    // }

    // this.userService.addUser(this.user)
    // this.notification()
  }

  notification(){
    // window.alert('New user ' + this.user.firstName +' was created!');
  }

}
