import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import {ApiService} from '../api.service';
import {Comment} from '../comment';

@Component({
  selector: 'app-professor-detail',
  templateUrl: './professor-detail.component.html',
  styleUrls: ['./professor-detail.component.css']
})
export class ProfessorDetailComponent implements OnInit {

  professor;
  comment = new Comment();
  bookName;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private apiService: ApiService
  ) { }

  ngOnInit(): void {
    this.getProfessor();
  }

  getProfessor() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.apiService.getProfessor(id).subscribe(professor => this.professor = professor);
  }

  addComment(): void {
    this.comment.professor = this.professor.id;
    this.apiService.addComment(this.comment)
      .subscribe( book => {
        this.bookName = book;
      });
  }


}
