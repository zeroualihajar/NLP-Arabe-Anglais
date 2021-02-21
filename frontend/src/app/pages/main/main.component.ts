import { Component, OnInit } from '@angular/core';
import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';
import { map } from 'rxjs/operators';
import { Data } from 'src/app/models/Data';
import { Observable } from 'rxjs/Observable';
import { Router } from '@angular/router';


const ScrapQuery = gql`
  query
  {
    data
    {
      id
      title
    }
  }
`;


interface Response{
  data : Data[];
}


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  data$: Observable<Data[]> | undefined;
  public static id: String="";

  constructor(private apollo: Apollo, private router: Router) { }

  ngOnInit() {
    this.data$ = this.apollo.watchQuery<Response>({
          query: ScrapQuery,
        }).valueChanges.pipe(map(result => result.data.data ));
  }


  more(event: any, id: any){
    MainComponent.id = id
    console.log(MainComponent.id)
    this.router.navigate(['/details']);
  }
}
