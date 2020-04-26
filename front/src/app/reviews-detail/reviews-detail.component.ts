import { Component, OnInit } from '@angular/core';
import {ReviewService} from '../review.service';
import {HttpClient} from '@angular/common/http';
import {Review} from '../review';
import { Location } from '@angular/common';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-reviews-details',
  templateUrl: './reviews-detail.component.html',
  styleUrls: ['./reviews-detail.component.css']
})
export class ReviewsDetailComponent implements OnInit {

  review: Review;

  constructor(private location: Location, private reviewService: ReviewService, public route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.getReview()
  }

  getReview(){
    let id = this.route.snapshot.paramMap.get('id');
    id = id.substr(1);
    this.reviewService.getReview(id)
      .subscribe(review=>{
        this.review = review
      })
  }

}
