import {AfterViewInit, Component, Input, OnInit} from '@angular/core';
import {ApiService} from '../api.service';

@Component({
  selector: 'app-last-reviews',
  templateUrl: './last-reviews.component.html',
  styleUrls: ['./last-reviews.component.css']
})
export class LastReviewsComponent implements OnInit, AfterViewInit {
  slideIndex = 1;
  @Input() reviews;

  constructor(
    private apiService: ApiService
  ) { }

  ngOnInit(): void {
  }

  ngAfterViewInit() {
    this.showSlides(this.slideIndex);
  }

  range(n) {
    n = this.reviews.length;
    return Array(Math.max(0, n));
  }

  getReviews() {
    this.apiService.getLastReviews()
      .subscribe(
        reviews => {
          this.reviews = reviews;
          this.plusSlides(1);
        }
      );
  }

  plusSlides(n) {
    this.showSlides(this.slideIndex += n);
  }

  currentSlide(n) {
    this.showSlides(this.slideIndex = n);
  }

  showSlides(n) {
    let i;
    const slides = document.getElementsByClassName('mySlides') as HTMLCollectionOf<HTMLElement>;
    const dots = document.getElementsByClassName('dot') as HTMLCollectionOf<HTMLElement>;
    if (n > slides.length) {this.slideIndex = 1; }
    if (n < 1) {this.slideIndex = slides.length; }
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = 'none';
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(' active', '');
    }
    slides[this.slideIndex - 1].style.display = 'block';
    dots[this.slideIndex - 1].className += ' active';
    // if (n === 3) {
    //   window.setTimeout(() => this.plusSlides(n - (n - 1)), 4000);
    // } else {
    //   window.setTimeout(() => this.plusSlides(n + 1), 4000);
    // }
  }

}
