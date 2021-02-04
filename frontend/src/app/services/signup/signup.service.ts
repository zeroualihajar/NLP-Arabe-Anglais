import { Injectable } from '@angular/core';
import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { LoginService } from '../login/login.service';

const addUser = gql`
  mutation AddUser($username: String!, $email: String!, $password: String!)
  {
    addUser(username: $username, email: $email, password: $password)
    {
        user {
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
  constructor(private apollo: Apollo, private loginService:LoginService) { }


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
      },
      () => console.error('Error : ', Error))
  }
}
