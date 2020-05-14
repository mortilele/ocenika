import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  lastReviews;
  constructor(
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.lastReviews = this.route.snapshot.data.lastReviews;
  }
}
