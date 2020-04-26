import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompaniesComponent} from './companies/companies.component';
import {VacanciesComponent} from './vacancies/vacancies.component';
import { CompanyDetailsComponent } from './company-details/company-details.component';
import {VavancyDetailsComponent} from './vavancy-details/vavancy-details.component'
import { TempComponent } from './temp/temp.component';
import {CategoriesComponent} from './categories/categories.component'
import { GamesComponent } from './games/games.component';
import {GameDetailComponent} from './game-detail/game-detail.component'
import { ReviewComponent } from './review/review.component';
import { NewsComponent } from './news/news.component';
import {NewsDetailComponent} from './news-detail/news-detail.component'
import {ReviewsDetailComponent} from './reviews-detail/reviews-detail.component'
import { HomeComponent } from './home/home.component';
import { ContactComponent } from './contact/contact.component';
import {CartComponent} from './cart/cart.component'
import { ProfileComponent } from './profile/profile.component';

const routes: Routes = [
  { path: '', component: HomeComponent},
  { path: 'home', component: HomeComponent},
  { path: 'reviews', component: ReviewComponent},
  { path: 'news', component: NewsComponent},
  { path: 'cart', component: CartComponent},
  { path: 'contact', component: ContactComponent},
  { path: 'games', component: CategoriesComponent},
  { path: 'profile', component: ProfileComponent},
  { path: 'games/:id', component: GameDetailComponent},
  { path: 'news/:id', component: NewsDetailComponent},
  { path: 'reviews/:id', component: ReviewsDetailComponent},
  {path: 'categories/:id', component: GamesComponent },
  { path: 'companies/:id/vacancies', component: VacanciesComponent },
  { path: 'companies/:id', component: CompanyDetailsComponent },
  { path: 'vacancies/:id', component: VavancyDetailsComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }