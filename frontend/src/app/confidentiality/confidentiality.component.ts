import { Component, OnInit } from '@angular/core';
import {ApiService} from '../api.service';

@Component({
  selector: 'app-confidentiality',
  templateUrl: './confidentiality.component.html',
  styleUrls: ['./confidentiality.component.css']
})
export class ConfidentialityComponent implements OnInit {

  pdfsrc;
  constructor(
    private apiService: ApiService
  ) { }

  ngOnInit(): void {
    this.getPDFSrc();
  }

  getPDFSrc() {
    this.apiService.getPolicyURL()
      .subscribe(data => {
        this.pdfsrc = data;
        this.pdfsrc = this.pdfsrc.file;
      });
  }

}
