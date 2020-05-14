import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {ApiService} from '../api.service';
import {Comment} from '../comment';
import {AuthService} from '../auth.service';

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
      this.comment.subject = professor.subjects[0].name;
    });
  }

  getProfessorRatingFilter() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.apiService.getProfessorRatingCount(id).subscribe(ratings => this.ratings = ratings);
  }

  addComment(): void {
    this.comment.professor = this.professor.id;
    this.apiService.addComment(this.comment)
      .subscribe(
        comment => {
        this.getProfessorRatingFilter();
        alert(comment.moderator_message);
      },
        error => {
          alert(error.error);
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
      alert('Зарегистро чтобы видеть все отзывы');
    }
  }


}
