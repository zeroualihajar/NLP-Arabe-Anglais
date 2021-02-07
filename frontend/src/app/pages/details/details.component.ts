import { Component, OnInit } from '@angular/core';
import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';
import { MainComponent } from '../main/main.component';

const details = gql`
  query getDetails($id: String)
  {
    getDetails(id: $id)
    {
      id
      title
      url
      content
    }
  }
`;

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.scss']
})
export class DetailsComponent implements OnInit {

  id: String ="";
  title: String ="";
  content: String ="";
  source: String = "";
  data: any;

  constructor(private apollo:Apollo) { }

  ngOnInit(): void {
    this.id = MainComponent.id

    this.apollo.watchQuery({
        query: details,
        variables: {
          id : this.id
        }
      }).valueChanges.subscribe((result) => {

        this.data = result.data
        this.title = this.data['getDetails']['title']
        this.content = this.data['getDetails']['content']
        this.source = this.data['getDetails']['url']


      }, (error) => {
        console.log(error)
      });

  }

}
