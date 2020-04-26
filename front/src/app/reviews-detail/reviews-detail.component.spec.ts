import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReviewsDetailComponent } from './reviews-detail.component';

describe('ReviewsDetailComponent', () => {
  let component: ReviewsDetailComponent;
  let fixture: ComponentFixture<ReviewsDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReviewsDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReviewsDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
