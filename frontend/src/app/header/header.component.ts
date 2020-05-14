import {Component, Input, OnInit} from '@angular/core';
import {AuthService} from '../auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  @Input() current = 'main';
  constructor(
    public authService: AuthService
  ) { }

  ngOnInit(): void {
  }
}
