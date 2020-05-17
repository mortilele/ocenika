import {Component, EventEmitter, HostListener, Input, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-popup',
  templateUrl: './popup.component.html',
  styleUrls: ['./popup.component.css']
})
export class PopupComponent implements OnInit {
  @Input() showModel: boolean;
  @Output() outputToParent = new EventEmitter();
  @Input() header;
  @Input() content;
  constructor() { }

  ngOnInit(): void {
  }

  @HostListener('document:click', ['$event'])
  onDocumentClick(event: MouseEvent) {
    const x = document.getElementById('myModal');
    if (event.target === x) {
      this.toggleShowModel();
    }
  }

  toggleShowModel() {
    this.showModel = false;
    this.outputToParent.emit(this.showModel);
  }


}
