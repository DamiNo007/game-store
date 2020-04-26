import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppComponent} from './app.component';
import {CompaniesComponent} from './companies/companies.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {AuthInterceptor} from './auth.interceptor';
import {RouterModule} from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { VacanciesComponent } from './vacancies/vacancies.component';
import {FormsModule} from '@angular/forms';
import { CompanyDetailsComponent } from './company-details/company-details.component';
import { VavancyDetailsComponent } from './vavancy-details/vavancy-details.component';
import { TempComponent } from './temp/temp.component';
import { CategoriesComponent } from './categories/categories.component';
import { CategoryDetailComponent } from './category-detail/category-detail.component';
import { GamesComponent } from './games/games.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { HomeComponent } from './home/home.component';
import { ReviewComponent } from './review/review.component';
import { ReviewsComponent } from './reviews/reviews.component';
import { NewsComponent } from './news/news.component';
import { MessagesComponent } from './messages/messages.component';
import { CartComponent } from './cart/cart.component';
import { GameboxComponent } from './gamebox/gamebox.component';
import { CardformComponent } from './cardform/cardform.component';
import { ProfileComponent } from './profile/profile.component';
import { GameDetailComponent } from './game-detail/game-detail.component';
import { NewsDetailComponent } from './news-detail/news-detail.component';
import { ReviewsDetailComponent } from './reviews-detail/reviews-detail.component';
import { ContactComponent } from './contact/contact.component';
import { UserComponent } from './user/user.component';

@NgModule({
  declarations: [
    AppComponent,
    CompaniesComponent,
    VacanciesComponent,
    CompanyDetailsComponent,
    VavancyDetailsComponent,
    TempComponent,
    CategoriesComponent,
    CategoryDetailComponent,
    GamesComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    ReviewComponent,
    ReviewsComponent,
    NewsComponent,
    MessagesComponent,
    CartComponent,
    GameboxComponent,
    CardformComponent,
    ProfileComponent,
    GameDetailComponent,
    NewsDetailComponent,
    ReviewsDetailComponent,
    ContactComponent,
    UserComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}