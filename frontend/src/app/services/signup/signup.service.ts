import { Injectable } from '@angular/core';
import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { LoginService } from '../login/login.service';
import { LoginComponent } from 'src/app/pages/login/login.component';
import { Router } from '@angular/router';

const addUser = gql`
  mutation AddUser($username: String!, $email: String!, $password: String!)
  {
    addUser(username: $username, email: $email, password: $password)
    {
        user {
          id,
          username,
          email,
          password
        }
    }
}
`;


@Injectable({
  providedIn: 'root'
})
export class SignupService {


  password: String = "";
  ps: any ;
  constructor(private apollo: Apollo, private loginService:LoginService, private router: Router) { }


  add(form: FormGroup){
    this.password = this.loginService.set('123456$#@$^@1ERF', form.value.password);

      this.apollo.mutate({
        mutation: addUser,
        variables: {
          username: form.value.username,
          email : form.value.email,
          password : this.password,
        }
      }).subscribe(({data}) => {
        console.log('AddUser : ', data)
        this.ps = data
        LoginComponent.id = this.ps['addUser']['user']['id']
        this.router.navigate(['/principal']);
        
      },
      () => console.error('Error : ', Error))
  }
}
