import { LoginService } from './../../services/login.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';
import * as CryptoJS from 'crypto-js';

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

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  form!: FormGroup;



  constructor(private apollo: Apollo, private formBuilder: FormBuilder, private loginService:LoginService) { }

  ngOnInit(): void {
     this.form = this.formBuilder.group({
      username : new FormControl('', Validators.required),
      email : new FormControl('', Validators.required),
      password : new FormControl('', Validators.required),
    })
  }

  addUser(){

    // let password = this.loginService.set('123456$#@$^@1ERF', this.form.value.password);
    //   console.log('Encrypted :' + password);
    //   var decrypted = this.loginService.get('123456$#@$^@1ERF', password);
    //   console.log('Decrypted :' + decrypted);


    this.apollo.mutate({
      mutation: addUser,
      variables: {
        username: this.form.value.username,
        email : this.form.value.email,
        password : this.form.value.password,
      }
    }).subscribe(({data}) => {
      console.log('AddUser : ', data)
    },
    () => console.error('Error : ', Error))
  }
}
