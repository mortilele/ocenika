import { Component, OnInit } from '@angular/core';
import {AuthService} from '../auth.service';
import {Router} from '@angular/router';
import {ApiService} from '../api.service';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {
  email = '';
  password = '';
  firstName = '';
  lastName = '';
  file;
  selectedUniversity;
  phone;
  universities;
  showPopup;
  popupContent;
  popupHeader;
  constructor(
    private authService: AuthService,
    private router: Router,
    private apiService: ApiService,
  ) { }

  ngOnInit(): void {
    this.getUniversities();
  }

  getUniversities() {
    this.apiService.getAllUniversities()
      .subscribe(
        universities => {
          this.universities = universities;
          this.selectedUniversity = this.universities[0].id;
        }
      );
  }

  toggleShowPopup() {
    this.showPopup = false;
  }

  registerUser() {
    if (!this.email || !this.firstName || !this.lastName || !this.password) {
      this.popupHeader = 'Ошибка!';
      this.popupContent = 'Пожалуйста, введите все обязательные поля';
      this.showPopup = true;
    } else {
      const formData = new FormData();
      formData.append('email', this.email);
      formData.append('first_name', this.firstName);
      formData.append('last_name', this.lastName);
      formData.append('phone', this.phone);
      formData.append('university', this.selectedUniversity);
      formData.append('password', this.password);
      if (this.file) {
        formData.append('transcript', this.file);
      }
      this.authService.registerUser(formData)
        .subscribe(
          response => {
            this.router.navigate(['/login']);
          },
          error => {
            this.showPopup = true;
            this.popupHeader = 'Неправильные данные';
            this.popupContent = 'Пожалуйста, проверьте корректность своих данных';
          }
        );
    }

  }

  onFileChange(event) {
    this.file = event.target.files[0];
    console.log(this.file.data);
    console.log(this.file);
  }

}
