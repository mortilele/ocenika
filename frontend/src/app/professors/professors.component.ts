import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';

@Component({
  selector: 'app-professors',
  templateUrl: './professors.component.html',
  styleUrls: ['./professors.component.css']
})
export class ProfessorsComponent implements OnInit {
  professors;
  universities;

  constructor(
    private apiService: ApiService
  ) { }

  ngOnInit(): void {
    this.getProfessors();
    this.getUniversities();
  }

  getProfessors() {
    this.apiService.getProfessors().subscribe(professors => this.professors = professors);
  }

  toStringJoin(data) {
    return data.map(r => r.abbreviation).join(', ');
  }

  getUniversities() {
    this.apiService.getAllUniversities().subscribe(universities => this.universities = universities)
  }



}
