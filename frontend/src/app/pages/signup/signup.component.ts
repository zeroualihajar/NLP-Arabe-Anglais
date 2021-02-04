import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';
import { SignupService } from 'src/app/services/signup/signup.service';

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
  password: String = "";


  constructor(private apollo: Apollo, private formBuilder: FormBuilder, private signupService:SignupService) { }

  ngOnInit(): void {
     this.form = this.formBuilder.group({
      username : new FormControl('', Validators.required),
      email : new FormControl('', Validators.required),
      password : new FormControl('', Validators.required),
    })
  }

  addUser(){

      this.signupService.add(this.form)
  }
}
