import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Apollo } from 'apollo-angular';
import gql from 'graphql-tag';
import { LoginService } from 'src/app/services/login/login.service';
import { SignupService } from 'src/app/services/signup/signup.service';
import { LoginComponent } from '../login/login.component';

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

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  form!: FormGroup;
  password: String = "";
  ps: any ;

  constructor(private apollo: Apollo, private formBuilder: FormBuilder, private router: Router, private loginService: LoginService) { }

  ngOnInit(): void {
     this.form = this.formBuilder.group({
      username : new FormControl('', Validators.required),
      email : new FormControl('', Validators.required),
      password : new FormControl('', Validators.required),
    })
  }

  addUser(){
    this.password = this.loginService.set('123456$#@$^@1ERF', this.form.value.password);

      this.apollo.mutate({
        mutation: addUser,
        variables: {
          username: this.form.value.username,
          email : this.form.value.email,
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
