import { Component, OnInit } from '@angular/core';
import { News } from '../news'
import { NewsService } from '../news.service'

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {

  newses:News[];

  constructor(private newsService:NewsService) {}

  ngOnInit(): void {
    this.getNews();
  }

  getNews():void{
    this.newsService.getNews().subscribe(news=>this.newses = news);
  }
}