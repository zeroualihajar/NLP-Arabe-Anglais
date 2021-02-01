import { Observable } from 'rxjs/Observable';
import { Apollo } from 'apollo-angular';
import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/models/User';
import gql from 'graphql-tag';
import { map } from 'rxjs/operators';


const UserQuery = gql`
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

interface Response{
  users : User[];
}

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.scss'],

})

export class TestComponent implements OnInit{

  users$: Observable<User[]> | undefined;

  constructor(private apollo: Apollo){
   }


  ngOnInit() {


     this.users$ = this.apollo.watchQuery<Response>({
          query: UserQuery,
        }).valueChanges.pipe(map(result => result.data.users ));

    // this.users = this.testService.all().valueChanges.subscribe((data: { allUsers: User[]; }) => {
    //   this.users = data.allUsers;
    //   console.log(data.allUsers);
    // });

  // this.apollo.watchQuery<any>({ query: PostQuery }).valueChanges.pipe(map (result => result.data.users));
    // console.log(this.users)



  //   this.apollo.watchQuery<Query>({
  //     query: gql`
  //       query allUsers {
  //          user {
  //         id,
  //         email,
  //         password
  //       }
  // }`
  //   })
  //     .valueChanges
  //     .pipe(
  //       map(result => result.data.allUsers)
  //     );

    //  this.apollo
    //   .query<any>({
    //     query: gql`
    //       {
    //         adduser {
    //           name
    //           email
    //           password
    //         }
    //       }
    //     `
    //   })
    //   .subscribe(
    //     ({ data, loading }) => {
    //       this.user = data && data.user;
    //       this.loading = loading;
    //     }
    //   );
  // }

  // onSubmit()
  // {
  //   this.error = "";
  //   this.loading = true;
  //   this.apollo
  //     .query<any>({
  //       query: gql`
  //         query() {
  //           user {
  //             email
  //             password
  //           }
  //         }
  //       `
  //     })
  //     .subscribe(({ data, loading }) => {
  //      this.user = data.user;
  //       this.loading = loading;
  //     });
  }



  onSubmit(){

  //   console.log(this.user.email)
  //   this.apollo.query
  //   fetch(`/graphql`, {
  //   method: "POST",
  //   headers: {
  //     "Content-Type": "application/json",
  //   },
  //   body: JSON.stringify({
  //     query: `mutation {
  //       adduser(email: ${this.user.email}, password: ${this.user.password}) {
  //         email
  //         password
  //       }
  //     }`,
  //   }),
  // })
  //   .then(res => res.json())
  //   .then(res => res.data.user)
  //   .catch(console.error)
  }

}
