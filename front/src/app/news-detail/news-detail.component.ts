import { Component, OnInit, Input } from '@angular/core';
import {NewsService} from '../news.service';
import {HttpClient} from '@angular/common/http';
import {News} from '../news';
import {ActivatedRoute} from '@angular/router';
import { Location } from '@angular/common';


@Component({
  selector: 'app-news-details',
  templateUrl: './news-detail.component.html',
  styleUrls: ['./news-detail.component.css']
})
export class NewsDetailComponent implements OnInit {

  news: News;

  constructor(private location: Location, private newsService: NewsService, public route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.getNews()
  }

  getNews(){
    let id = this.route.snapshot.paramMap.get('id');
    id = id.substr(1);
    this.newsService.getNewsDetail(id)
      .subscribe(news=>{
        this.news = news
      })
  }
}
