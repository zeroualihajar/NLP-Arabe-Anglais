import { LoginComponent } from './../../pages/login/login.component';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Apollo } from 'apollo-angular';
import * as CryptoJS from 'crypto-js';
import gql from 'graphql-tag';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { User } from 'src/app/models/User';


const login = gql`
  query getUser($email: String)
  {
    getUser(email: $email)
    {
      id
      username
      email
      password

    }
  }
`;



@Injectable({
  providedIn: 'root'
})
export class LoginService {

  pass: string ="";
  ps: any ;
  cryp: any;

  
  username: String ="";
  email: String = "";


  constructor(private apollo:Apollo, private router: Router) { }


  loginQuery(form: FormGroup){
     this.apollo.watchQuery<User>({
        query: login,
        variables: {
          email : form.value.email,
        }
      }).valueChanges.subscribe((result) => {

        this.ps = result.data
        this.pass = this.ps['getUser']['password']
        var decrypted = this.get('123456$#@$^@1ERF',  this.pass);


        this.username = this.ps['getUser']['username']
        this.email = this.ps['getUser']['email']


        if(form.value.password == decrypted){

        LoginComponent.id = this.ps['getUser']['id']
        console.log("LoginComponent.id")
        LoginComponent.isLogged = true;

        this.router.navigate(['/principal']);


      }
      else{
        LoginComponent.ts = "1"
        
      }

      }, (error) => {
        console.log(error)
      });

  }












  //----------------- Cryptage -----------------
  //The set method is use for encrypt the value.
  set(keys: string, value: string){
    var key = CryptoJS.enc.Utf8.parse(keys);
    var iv = CryptoJS.enc.Utf8.parse(keys);
    var encrypted = CryptoJS.AES.encrypt(CryptoJS.enc.Utf8.parse(value.toString()), key,
    {
        keySize: 128/8,
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });

    return encrypted.toString();
  }

    //The get method is use for decrypt the value.
  get(keys: string, value: string){
    var key = CryptoJS.enc.Utf8.parse(keys);
    var iv = CryptoJS.enc.Utf8.parse(keys);
    var decrypted = CryptoJS.AES.decrypt(value, key, {
        keySize: 128/8,
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });

    return decrypted.toString(CryptoJS.enc.Utf8);
  }

}
