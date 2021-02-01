import { LoginService } from './../../services/login.service';
import { Apollo } from 'apollo-angular';
import { Component, OnInit } from '@angular/core';
import gql from 'graphql-tag';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { User } from 'src/app/models/User';


const confirm = gql`
  mutation Login($username: String! , $email: String! , $password: String)
  {
    login(username: $username, email: $email, password: $password){
    user
    {
      username
      email
      password
    }
  }
}
`;

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  form!: FormGroup;
  user: User | undefined;
  pass: string | undefined;
  username : String ="";
  constructor(private apollo:Apollo, private formBuilder: FormBuilder, private loginService:LoginService) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      email : new FormControl('', Validators.required),
      password : new FormControl('', Validators.required),
    })
  }

  confirm() {

      //this.pass = this.loginService.set('123456$#@$^@1ERF', this.form.value.password);
      // console.log('Encrypted :' +  this.pass);
      // var decrypted = this.loginService.get('123456$#@$^@1ERF',  this.pass);
      // console.log('Decrypted :' + decrypted);


      this.apollo.mutate({
        mutation: confirm,
        variables: {
          username:"",
          email : this.form.value.email,
          password :this.form.value.password,
        }
      }).subscribe((result) => {
        console.log('Confirm : ', result)

      }, (error) => {
        console.log(error)
      });

    }
}
