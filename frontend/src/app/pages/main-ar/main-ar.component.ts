import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-main-ar',
  templateUrl: './main-ar.component.html',
  styleUrls: ['./main-ar.component.scss']
})
export class MainArComponent implements OnInit {

  public lang = "arabic";
  constructor() { }

  ngOnInit(): void {
  }

}
