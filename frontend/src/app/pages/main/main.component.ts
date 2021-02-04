import { Component, OnInit } from '@angular/core';
import gql from 'graphql-tag';



const ScrapQuery = gql`
  query
  {
    users
    {
      id
      email
      password
    }
  }
`;


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  public lang : Boolean = true;
  constructor() { }

  ngOnInit() {
  }


  tokenization(){
    console.log("hh")
  }
}
