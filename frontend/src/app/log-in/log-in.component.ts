import { Component, OnInit } from '@angular/core';
import {AuthService} from '../auth.service';
import {Location} from '@angular/common';
import {Router} from '@angular/router';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent implements OnInit {
  email;
  password;
  showPopup;
  popupHeader;
  popupContent;
  constructor(
    private authService: AuthService,
    private location: Location,
    private route: Router,
  ) { }

  ngOnInit(): void {
  }

  toggleShowPopup() {
    this.showPopup = false;
  }

  login() {
    if (!this.email || !this.password) {
      this.popupHeader = 'Заполните все поля';
      this.showPopup = true;
    } else {
      this.authService.loginUser(this.email, this.password)
        .subscribe(
          response => {
            // @ts-ignore
            localStorage.setItem('token', response.token);
            this.route.navigate(['/']);
            // this.location.back();
          },
          error => {
            this.popupHeader = 'Неправильные данные';
            this.showPopup = true;
          }
        );
      }
    }





}
