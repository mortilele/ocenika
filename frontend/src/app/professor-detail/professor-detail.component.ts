import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {ApiService} from '../api.service';
import {Comment} from '../comment';
import {AuthService} from '../auth.service';
import {validateEmail} from '../utils';

@Component({
  selector: 'app-professor-detail',
  templateUrl: './professor-detail.component.html',
  styleUrls: ['./professor-detail.component.css']
})
export class ProfessorDetailComponent implements OnInit {

  professor;
  ratings;
  reviews;
  comment = new Comment();
  showPopup = false;
  popupContent = '';
  popupHeader = '';

  constructor(
    private route: ActivatedRoute,
    public router: Router,
    private apiService: ApiService,
    public authService: AuthService,
  ) { }

  ngOnInit(): void {
    this.getUserData();
    this.getProfessor();
    this.getProfessorRatingFilter();
  }

  getProfessor() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.apiService.getProfessor(id).subscribe(professor => {
      this.professor = professor;
      this.reviews = professor.ratings;
      this.comment.subject = professor.subjects[0].id;
    });
  }

  toggleShowPopup() {
    this.showPopup = false;
    this.popupHeader = '';
    this.popupContent = '';
  }

  getProfessorRatingFilter() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.apiService.getProfessorRatingCount(id).subscribe(ratings => this.ratings = ratings);
  }

  addComment(): void {
    this.comment.professor = this.professor.id;
    if ((this.authService.loggedIn() && !this.comment.review) || (!this.comment.email || !this.comment.review)) {
      this.popupHeader = 'Пожалуйста заполните все данные!';
      this.showPopup = true;
      return;
    }
    if (!validateEmail(this.comment.email)) {
      this.popupHeader = 'Неправильный email';
      this.showPopup = true;
      return;
    }
    this.apiService.addComment(this.comment)
      .subscribe(
        comment => {
        this.getProfessorRatingFilter();
        this.popupHeader = 'Ваш отзыв успешно отправлен';
        this.popupContent = comment.moderator_message;
        this.showPopup = true;
      },
        error => {
          this.popupHeader = 'Произошла ошибка';
          this.popupContent = 'Вы уже оставляли отзыв данному преподавателю';
          this.showPopup = true;
        }
      );
  }

  statsReviews(total, value) {
    return value * 100 / total;
  }

  convertDate(date) {
    let convertedDateString = date.toLocaleString();
    convertedDateString = convertedDateString.replace('at ', '');
    return new Date(convertedDateString);
  }

  range(n) {
      return Array(Math.max(0, Math.min(5, n)));
  }

  getUserData() {
    if (this.authService.loggedIn()) {
      this.authService.getUserData()
        .subscribe(
          user => {
            // @ts-ignore
            return this.comment.email = user.email;
          },
          error => console.log(error)
        );
    }
  }

  getAllReviews() {
    if (this.authService.loggedIn()) {
      this.apiService.getProfessorRatings(this.professor.id).subscribe(reviews => this.reviews = reviews);
      document.getElementById('get_reviews').style.display = 'none';
    } else {
      this.popupHeader = 'Авторизуйтесь';
      this.popupContent = 'Пожалуйста, зарегистрируйтесь или войдите, чтобы увидеть все отзывы';
      this.showPopup = true;
    }
  }


}
