import { Apollo } from 'apollo-angular';
import { Injectable } from '@angular/core';
import gql from 'graphql-tag';

const PostQuery = gql`
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

@Injectable({
  providedIn: 'root'
})
export class TestService {

  constructor(private apollo:Apollo) { }

  public all():any{
    console.log(this.apollo.watchQuery<any>({ query: PostQuery }))
    return this.apollo.watchQuery<any>({ query: PostQuery });
  }
}
