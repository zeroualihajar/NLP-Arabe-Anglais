import { LoginService } from './../../services/login/login.service';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  form!: FormGroup;
  public static id : String = "603196b53af15dfe6dc4174b";
  public static isLogged: boolean;
  public  er: String = "";
  public static ts : String = "";

  constructor(private formBuilder: FormBuilder, private loginService:LoginService) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      email : new FormControl('', Validators.required),
      password : new FormControl('', Validators.required),
    })
  }

  confirm() {
    this.loginService.loginQuery(this.form)
    if(LoginComponent.ts == "1"){
      this.er = "Le mot de passe est incorrecte"

    }
    }

}
