import { Component, OnInit } from '@angular/core';
import {AuthService} from '../auth.service';
import {Location} from '@angular/common';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent implements OnInit {
  email;
  password;

  constructor(
    private authService: AuthService,
    private location: Location
  ) { }

  ngOnInit(): void {
  }

  login() {
    this.authService.loginUser(this.email, this.password)
      .subscribe(
        response => {
          // @ts-ignore
          localStorage.setItem('token', response.token);
          this.location.back();
        },
        error => console.log(error)
      );
  }




}
