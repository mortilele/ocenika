import { Component, OnInit } from '@angular/core';
import {AuthService} from '../auth.service';
import {ApiService} from '../api.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  userData;
  fullName;
  transcript;
  universities;
  constructor(
    private authService: AuthService,
    private apiService: ApiService
  ) { }

  ngOnInit(): void {
    this.getUserData();
    this.getUniversities();
  }

  getUniversities() {
    this.apiService.getAllUniversities()
      .subscribe(
        universities => {
          this.universities = universities;
        }
      );
  }

  getUserData() {
    this.authService.getUserData()
      .subscribe(
        data => {
          this.userData = data;
          this.fullName = this.userData.first_name + ' ' + this.userData.last_name;
        }
      );
  }

  goToLink(url) {
    window.open(url, '_blank');
  }

  updateUserProfile() {
    const formData = new FormData();
    formData.append('email', this.userData.email);
    formData.append('first_name', this.userData.first_name);
    formData.append('last_name', this.userData.last_name);
    formData.append('phone', this.userData.phone);
    if (this.userData.university) {
      formData.append('university', this.userData.university);
    }
    if (this.transcript) {
      formData.append('transcript', this.transcript);
    }
    if (this.userData.password) {
      formData.append('password', this.userData.password);
    }
    this.authService.updateUserData(this.userData.id, formData)
      .subscribe(
        response => {
          alert('suces');
        }
      );
  }

  onFileChange(event) {
    this.transcript = event.target.files[0];
  }

}
