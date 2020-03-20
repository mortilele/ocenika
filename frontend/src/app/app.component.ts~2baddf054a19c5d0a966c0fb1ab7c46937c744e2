import { Component } from '@angular/core';
import {ApiService} from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
  universities: any;

  constructor(private api: ApiService) {
    this.getUniversities();
    console.log(this.universities);
  }

  getUniversities() {
    this.api.getAllUniversities().subscribe(
      data => {
        this.universities = data;
      },
      error => {
        console.error(error);
      });
  }

}
