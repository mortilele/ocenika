import { Component, OnInit } from '@angular/core';
import {AuthService} from '../auth.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {
  username = '';
  email = '';
  password = '';
  firstName = '';
  lastName = '';
  file;
  university;
  phone;
  constructor(
    private authService: AuthService,
    private router: Router,
  ) { }

  ngOnInit(): void {
  }

  registerUser() {
    const registerUserData = {
      username: this.username,
      email: this.email,
      password: this.password,
      first_name: this.firstName,
      last_name: this.lastName,
      transcript: this.file,
      phone: this.phone,
      university: this.university
    };
    console.log(registerUserData);
    this.authService.registerUser(registerUserData)
      .subscribe(
        response => {
          this.router.navigate(['/login']);
        },
        error => console.log(error)
      );
  }

  onFileChange(event) {
    this.file = event.target.files[0];
    console.log(event);
  }

}
