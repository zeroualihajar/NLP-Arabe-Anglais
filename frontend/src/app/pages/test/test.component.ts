import { Observable } from 'rxjs/Observable';
import { Apollo } from 'apollo-angular';
import { Component, OnInit } from '@angular/core';
import gql from 'graphql-tag';
import { map } from 'rxjs/operators';
import { His } from 'src/app/models/His';
import { LoginComponent } from '../login/login.component';


const getHis = gql`
  query getHis($id: String)
  {
    getHis(id: $id)
    {
      text{
        content
        operation{
          nameOp
          resultOp
          dateOp
        }
      }

    }
  }
`;

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.scss'],

})

export class TestComponent implements OnInit{

  ps: any ;
  pass : string ="";
  histo: His[] | undefined;
  er: String="";

  constructor(private apollo: Apollo){
   }


  ngOnInit() {
    if(LoginComponent.id != "603196b53af15dfe6dc4174b"){
    this.apollo.watchQuery<His>({
          query: getHis,
          variables: {
          id : LoginComponent.id,
        }
        }).valueChanges.subscribe((result) => {

        this.ps = result.data
        this.histo = this.ps['getHis']['text']
        console.log(this.histo)

      }, (error) => {
        console.log(error)
      });
    }
    else{
      this.er = "أنت غير متصل الآن، بإمكانك تسجيل الدخول أو إنشاء حساب خاص إن لو تكن تتوفر عليه. ندعوك للإنضمام إلى منصتنا. "
    }


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
